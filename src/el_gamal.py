import random
from utils import message_to_int, encryption_code_to_str

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
