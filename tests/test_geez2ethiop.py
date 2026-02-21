"""Tests for geez2ethiop conversion functions."""

from geez2ethiop import ethiop2ipa, geez2ethiop


class TestGeez2Ethiop:
    """Tests for geez2ethiop()."""

    def test_single_character(self) -> None:
        assert geez2ethiop("ሀ") == "ha"

    def test_word(self) -> None:
        # "አዲስ" -> "'adise"
        assert geez2ethiop("አዲስ") == "'adise"

    def test_multiple_words(self) -> None:
        # "ባ" maps to "bA" (capital A), not "ba"
        result = geez2ethiop("አዲስ አበባ")
        assert result == "'adise 'ababA"

    def test_empty_string(self) -> None:
        assert geez2ethiop("") == ""

    def test_non_geez_characters_pass_through(self) -> None:
        assert geez2ethiop("abc 123") == "abc 123"

    def test_mixed_geez_and_non_geez(self) -> None:
        result = geez2ethiop("ሀ-test")
        assert result == "ha-test"

    def test_space_preserved(self) -> None:
        result = geez2ethiop("ሀ ሁ")
        assert result == "ha hu"


class TestEthiop2IPA:
    """Tests for ethiop2ipa()."""

    def test_simple_vowel(self) -> None:
        # 'a' maps to r'\"a' (LaTeX umlaut notation)
        result = ethiop2ipa("a")
        assert result == r"\"a"

    def test_simple_consonant_vowel(self) -> None:
        result = ethiop2ipa("ha")
        assert "h" in result

    def test_empty_string(self) -> None:
        assert ethiop2ipa("") == ""

    def test_schwa(self) -> None:
        result = ethiop2ipa("e")
        assert result == r"\textschwa{}"

    def test_caron_s(self) -> None:
        # ^s -> \v{s}
        result = ethiop2ipa("^sa")
        assert r"\v{s}" in result


class TestRoundTrip:
    """Tests for geez2ethiop -> ethiop2ipa pipeline."""

    def test_addis_ababa(self) -> None:
        geez = "አዲስ አበባ"
        ethiop = geez2ethiop(geez)
        ipa = ethiop2ipa(ethiop)
        # Verify the pipeline produces non-empty output
        assert len(ethiop) > 0
        assert len(ipa) > 0

    def test_single_syllable(self) -> None:
        ethiop = geez2ethiop("ሀ")
        assert ethiop == "ha"
        ipa = ethiop2ipa(ethiop)
        assert len(ipa) > 0
