Nixos snippet to block domains from ABP-formatted lists obtained from some URL.

Add it to your `configuration.nix` like this:

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
