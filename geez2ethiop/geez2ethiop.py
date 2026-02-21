"""Conversion from Geez script to Ethiopian Latin transcription and IPA.

Functions:
    geez2ethiop: Geez script -> Ethiopian Latin transcription
    ethiop2ipa: Ethiopian Latin transcription -> IPA (LaTeX tipa format)
    main: CLI entry point
"""

import argparse
import re
import sys

from geez2ethiop.mapping import map_ethiop2ipa, map_geez2ethiop


def geez2ethiop(geez: str) -> str:
    """Convert Geez characters to Ethiopian Latin transcription.

    Parameters
    ----------
    geez : str
        Input string containing Geez characters.

    Returns
    -------
    str
        String converted to Ethiopian Latin transcription.
    """
    return "".join(map_geez2ethiop.get(g, g) for g in geez)


def ethiop2ipa(ethiop: str) -> str:
    """Convert Ethiopian Latin transcription to IPA (LaTeX tipa format).

    Parameters
    ----------
    ethiop : str
        Ethiopian Latin transcription string.

    Returns
    -------
    str
        String converted to IPA (LaTeX tipa format).
    """
    regex = "|".join(map(re.escape, map_ethiop2ipa))
    return re.sub(regex, lambda m: map_ethiop2ipa[m.group()], ethiop)


def main() -> None:
    """CLI entry point. Read Geez text from stdin and print conversion results.

    Options:
        -l, --latex: Output in LaTeX format.
    """
    parser = argparse.ArgumentParser(description="Convert Geez script to Ethiopian and IPA")
    parser.add_argument("-l", "--latex", action="store_true", help="output in LaTeX format")
    args = parser.parse_args()

    geez = sys.stdin.readline().strip()
    ethiop = geez2ethiop(geez)
    ipa = ethiop2ipa(ethiop)

    if args.latex:
        print("\\geeztext{" + ethiop + "}")
        print("\\textipa{" + ipa + "}")
    else:
        print(geez)
        print(ethiop)
        print(ipa)
