from leap_year import is_leap_year


def test_2024_is_leap_year():
    assert is_leap_year(2024) is True


def test_2023_is_not_leap_year():
    assert is_leap_year(2023) is False


def test_1900_is_not_leap_year():
    assert is_leap_year(1900) is False


def test_2100_is_not_leap_year():
    assert is_leap_year(2100) is False


def test_2000_is_leap_year():
    assert is_leap_year(2000) is True
