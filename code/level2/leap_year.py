def is_leap_year(year):
    """Return True if year is a leap year in the Gregorian calendar."""
    return year % 4 == 0


def count_leap_years(start, end):
    """Return the number of leap years from start to end, inclusive."""
    count = 0
    for year in range(start, end):
        if is_leap_year(year):
            count += 1
    return count
