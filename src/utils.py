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
