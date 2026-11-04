def caesar_encrypt(text, shift):
    """Encrypt text with a Caesar cipher.

    Shift each letter forward in the alphabet by `shift` positions,
    wrapping around from z back to a. Uppercase letters stay uppercase
    and lowercase letters stay lowercase. Characters that aren't letters
    (spaces, digits, punctuation) are left unchanged.

    Example: caesar_encrypt("Hello, World!", 3) returns "Khoor, Zruog!"
    """
    pass


def crack_caesar(ciphertext, crib):
    """Find the shift used to encrypt ciphertext.

    `crib` is a word you know appears in the original message. Return the
    shift (0-25) that was used with caesar_encrypt to produce ciphertext,
    or None if no shift produces a message containing crib.

    Example: crack_caesar("Phhw dw qrrq", "noon") returns 3
    """
    pass
