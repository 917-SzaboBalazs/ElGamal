import random
from typing import Optional

def message_to_int(msg: str) -> int:
    """
    Convert a string message to an integer code.

    @param msg: The input string message to be converted.
    @return: The integer code generated from the input message.
    """
    code = 0
    power = len(msg) - 1

    for ch in msg:
        if ch != ' ':
            code += (ord(ch) - ord('a') + 1) * pow(27, power)

        power -= 1

    return code


def encryption_code_to_str(encryp_msg: int) -> str:
    """
    Convert an integer code to a string message.

    @param encryp_msg: The input integer code to be converted.
    @return: The string message generated from the input code.
    """
    msg = ""
    power = 0

    while pow(27, power + 1) < encryp_msg:
        power += 1

    while encryp_msg > 0:
        power_res = pow(27, power)
        power -= 1

        next_int = encryp_msg // power_res

        if next_int == 0:
            msg += ' '
        else:
            next_char = chr(next_int + ord('a') - 1)
            msg += next_char

        encryp_msg %= power_res

    return msg


def generate_prime(num_digits: int = 4) -> int:
    """
    Generate a random prime number with a specified number of digits.

    :param num_digits: The number of digits in the prime number.
    :return: Random prime number.
    """
    def isprime(value):
        for i in range(2, value // 2 + 1):
            if value % i == 0:
                return False
        return True
    
    if num_digits < 1:
        return -1
    
    min_value = 10 ** (num_digits - 1)
    max_value = min_value * 10 - 1

    while True:
        candidate = random.randint(min_value, max_value)
        if isprime(candidate):
            return candidate


def find_first_generator(p: int) -> Optional[int]:
    """
    Find a generator for the multiplicative group modulo a prime number.

    :param p: The prime number.
    :return: A generator or None if no generators are found.
    """
    def is_primitive_root(g, p):
        values = set(pow(g, i, p) for i in range(1, p))
        return len(values) == p - 1

    for g in range(2, p):
        if is_primitive_root(g, p):
            return g

    return None
