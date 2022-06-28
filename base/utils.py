# standard library
import random
import re
import string

from itertools import cycle


def format_rut(rut):
    if not rut:
        return ""

    rut = rut.replace(" ", "").replace(".", "").replace("-", "")
    rut = rut[:9]

    if not rut:
        return ""

    verifier = rut[-1]
    if type(verifier) == str:
        verifier = verifier.upper()

    code = rut[0:-1][::-1]

    code = re.sub("(.{3})", "\\1.", code, 0, re.DOTALL)

    code = code[::-1]

    return "%s-%s" % (code, verifier)


def rut_verifying_digit(rut):
    """
    Uses a mod11 algorithm to compute RUT's check digit.
    Returns a value from 0 to 9 or k.
    """

    rev = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(rev, factors))
    mod = (-s) % 11
    return "0123456789k"[mod]


def validate_rut(rut):
    rut = rut.lower()
    rut = rut.replace("-", "")
    rut = rut.replace(".", "")
    rut = rut.replace(" ", "")
    aux = rut[:-1]
    dv = rut[-1:]

    res = rut_verifying_digit(aux)

    return res == dv


def random_rut(minimum=1000000, maximum=99999999):
    """
    Generates a random but valid RUT number
    """

    digits = str(random.randint(minimum, maximum))
    return format_rut(digits + rut_verifying_digit(digits))


def random_string(length=6, chars=None, include_spaces=True):
    if chars is None:
        chars = string.ascii_uppercase + string.digits

    if include_spaces:
        chars += " "

    return "".join(random.choice(chars) for x in range(length))


def random_phone():
    return f"+56 9 {random.randint(10000000, 99999999)}"
