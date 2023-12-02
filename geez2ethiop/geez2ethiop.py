from geez2ethiop.mapping import map_geez2ethiop, map_ethiop2ipa
import sys
import re

def geez2ethiop(geez):
    """
    Convert geez to ethiop
    """
    ethiop = ""
    for g in geez:
        if g in map_geez2ethiop.keys():
            ethiop += map_geez2ethiop[g]
        else:
            ethiop += g
    return ethiop

def ethiop2ipa(ethiop):
    """
    Convert ethiop to ipa
    """
    keys = map_ethiop2ipa.keys()
    regex = "|".join(map(re.escape, keys))
    ipa = re.sub(regex, lambda m: map_ethiop2ipa[m.group()], ethiop)
    return ipa


def main():
    geez = sys.stdin.read().strip()
    ethiop = geez2ethiop(geez)
    ipa = ethiop2ipa(ethiop)
    print("\n".join([geez, ethiop, ipa]))
