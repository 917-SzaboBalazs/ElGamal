import random

class ElGamal:

    def __init__(self) -> None:
        """
        Initialize the object with None public and private keys and generate new keys.

        The alphabet used for encoding and decoding is: (' ', 'a', 'b', 'c', ..., 'z')
        """
        self.__public_key = None
        self.__private_key = None
        self._generate_public_and_private_key()

    def encrypt(self, msg: str) -> int:
        """
        Encrypts the input message and returns the encrypted code.

        @param msg: The input string message to be encrypted.
        @return: The integer code representing the encrypted message.
        """
        pass

    def decrypt(self, encryp_msg: int) -> str:
        """
        Decrypts the input code and returns the original message.

        @param encryp_msg: The input integer code to be decrypted.
        @return: The decrypted string message.
        """
        pass

    def _generate_public_and_private_key(self) -> None:
        """
        Generate and set the public and private keys for ElGamal encryption.
        """
        pass

    def _message_to_int(self, msg: str) -> int:
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

    def _encryption_code_to_str(self, encryp_msg: int) -> str:
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
