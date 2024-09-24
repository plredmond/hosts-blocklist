{ url ? "https://hosts.oisd.nl/basic/"
}:
let
  nixpkgs = import <nixpkgs> { };
in
nixpkgs.stdenv.mkDerivation {
  pname = "hosts-blocklist";
  version = "0.1";
  src = ./.;
  installPhase = ''
    set -x
    mkdir -p $out/etc
    ${nixpkgs.python3}/bin/python list.py \
      < ${builtins.fetchurl url} \
      > $out/etc/hosts
    set +x
  '';
}
