from caesar import crack_caesar


def test_docstring_example():
    assert crack_caesar("Phhw dw qrrq", "noon") == 3


def test_shift_of_5():
    assert crack_caesar("rjjy fy stts", "noon") == 5


def test_shift_that_wraps_around():
    assert crack_caesar("xyz", "abc") == 23


def test_unencrypted_message():
    assert crack_caesar("hello world", "world") == 0


def test_no_shift_works():
    assert crack_caesar("abcde fghij", "hello") is None
