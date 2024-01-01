''' This module provides functions for converting Geez characters to Ethiopian characters and 
Ethiopian characters to IPA (International Phonetic Alphabet).

The module contains the following functions:
- `geez2ethiop(geez)`: Converts Geez characters to Ethiopian characters.
- `ethiop2ipa(ethiop)`: Converts Ethiopian characters to IPA.
- `main()`: The main function that handles command line options and performs the conversion.
'''

import sys
import re
import argparse
from geez2ethiop.mapping import map_geez2ethiop, map_ethiop2ipa

def geez2ethiop(geez):
    """
    Convert Geez characters to Ethiopian characters.

    Parameters:
    geez (str): The input string containing Geez characters.

    Returns:
    str: The converted string with Ethiopian characters.
    """
    ethiop = ""
    for g in geez:
        if g in map_geez2ethiop:
            ethiop += map_geez2ethiop[g]
        else:
            ethiop += g
    return ethiop

def ethiop2ipa(ethiop):
    """
    Convert ethiop to ipa

    Args:
        ethiop (str): The ethiop string to be converted to IPA.

    Returns:
        str: The IPA representation of the ethiop string.
    """
    keys = map_ethiop2ipa.keys()
    regex = "|".join(map(re.escape, keys))
    ipa = re.sub(regex, lambda m: map_ethiop2ipa[m.group()], ethiop)
    return ipa


def main():
    """
    Convert geez text to ethiop and ipa.

    This function reads geez text from stdin, converts it to ethiop and ipa,
    and prints the results to stdout. The output format can be customized
    using command line options.

    Command line options:
    -l, --latex: Output the results in LaTeX style.

    Example usage:
    $ python geez2ethiop.py -l < input.txt
    """

    # command line option
    parser = argparse.ArgumentParser(description="Convert geez to ethiop and ipa")
    parser.add_argument("-l", "--latex", action="store_true", help="output by latex style")
    args = parser.parse_args()

    # get geez from stdin
    # print reactively to stdout
    geez = sys.stdin.readline()
    geez = geez.strip()
    ethiop = geez2ethiop(geez)
    ipa = ethiop2ipa(ethiop)


    if args.latex:
        print("\\geeztext{" + ethiop + "}")
        print("\\textipa{" + ipa + "}")
    else:
        print(geez)
        print(ethiop)
        print(ipa)
