# Hosts blocklist for NixOS

Nixos snippet to block domains from ABP-formatted lists obtained from some URL.

See also, [toot](https://recurse.social/@redmp/113193934563178408).

# How does it work?

* `default.nix` file makes a nixpkgs derivation (a package) which fetches a url
  and pipes it through the python `list.py` program out to an `/etc/hosts` file
  in the resulting package.
* `list.py` program reads lines from stdin, removes some metadata cruft, parses
  the domains out of adblockpro format, and outputs them in `/etc/hosts` format
  as `"127.0.0.1 domain"` per line.
* `configuration.nix` imports this repo with some url parameter and includes the output in `networking.hostFiles` (shown below).

# How to use it?

Add it to your `configuration.nix` like below, except you need to replace the string `<path-to-this-repo>` with either a literal path on your system (i.e. by cloning this repo) or with some nix fetcher to dynamically obtain this repo from github.

* If you obtain the repo manually, be safe about it and store it under a user that you don't usually use (e.g. root).
* If you obtain the repo dynamically, be safe about it and specify a content hash.

```nix
{
  ...

  networking.hostFiles = [
    ("${import <path-to-this-repo> { url="https://small.oisd.nl/"; }}/etc/hosts")
    # ... more urls ...
  ];

  # disabled to avoid autocompleting spam hostnames
  programs.bash.enableCompletion = false;

  networking.extraHosts = ''
    # manually-curated list of hostnames that you want to block, in "127.0.0.1 hostname" format
  '';

  ...
}
```
