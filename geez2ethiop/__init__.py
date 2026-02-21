"""Module for converting Geez (Ethiopic) scripts into PDFLaTeX commands."""

from .geez2ethiop import ethiop2ipa, geez2ethiop
from .mapping import map_ethiop2ipa, map_geez2ethiop

__all__ = ["geez2ethiop", "ethiop2ipa", "map_geez2ethiop", "map_ethiop2ipa"]
