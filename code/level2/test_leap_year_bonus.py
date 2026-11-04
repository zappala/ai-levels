from leap_year import count_leap_years


def test_count_2000_to_2024():
    assert count_leap_years(2000, 2024) == 7


def test_count_single_leap_year():
    assert count_leap_years(2020, 2020) == 1


def test_count_no_leap_years():
    assert count_leap_years(2001, 2003) == 0


def test_count_another_range_with_no_leap_years():
    assert count_leap_years(2021, 2023) == 0
