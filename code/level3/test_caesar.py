from caesar import caesar_encrypt


def test_basic_shift():
    assert caesar_encrypt("abc", 1) == "bcd"


def test_wraps_around_end_of_alphabet():
    assert caesar_encrypt("xyz", 3) == "abc"


def test_preserves_case():
    assert caesar_encrypt("ABC xyz", 2) == "CDE zab"


def test_leaves_non_letters_unchanged():
    assert caesar_encrypt("a b-c 123!", 1) == "b c-d 123!"


def test_docstring_example():
    assert caesar_encrypt("Hello, World!", 3) == "Khoor, Zruog!"


def test_negative_shift():
    assert caesar_encrypt("abc", -1) == "zab"


def test_shift_larger_than_26():
    assert caesar_encrypt("xyz", 29) == "abc"


def test_shift_of_26_changes_nothing():
    assert caesar_encrypt("Hello", 26) == "Hello"
