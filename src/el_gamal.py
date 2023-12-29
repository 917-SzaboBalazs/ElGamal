import random
from typing import Tuple
from utils import message_to_int, encryption_code_to_str, find_first_generator


class ElGamal:

    def __init__(self, p: int) -> None:
        """
        Initialize the ElGamal encryption object.

        :param p: The prime number used for encryption.
        """
        self.__public_key = None
        self.__private_key = None
        self.__p = p
        self._generate_public_and_private_key()

    def encrypt(self, msg: str) -> Tuple[int, int]:
        """
        Encrypt the input message using ElGamal encryption.

        :param msg: The input string message to be encrypted.
        :return: A tuple (c1, c2) representing the encrypted message.
        """
        p, g, g_a = self.__public_key
        m = message_to_int(msg)

        # Choose a random k such that 1 <= k <= p-2
        k = random.randint(1, p - 2)

        # Calculate c1 and c2
        c1 = pow(g, k, p)
        c2 = (pow(g_a, k, p) * m) % p

        return c1, c2

    def decrypt(self, encryp_msg: Tuple[int, int]) -> str:
        """
        Decrypt the input code using ElGamal decryption.

        :param encryp_msg: A tuple (c1, c2) representing the encrypted message.
        :return: The decrypted string message.
        """
        p = self.__public_key[0]
        a = self.__private_key

        # Extract c1 and c2 from the encrypted message
        c1, c2 = encryp_msg

        # Calculate s = (c1^a) mod p
        s = pow(c1, a, p)

        # Calculate m = (c2 * s^-1) mod p
        m = (c2 * pow(s, -1, p)) % p

        # Convert the integer message back to a string
        msg = encryption_code_to_str(m)

        return msg

    def _generate_public_and_private_key(self) -> None:
        """
        Generate and set the public and private keys for ElGamal encryption.
        """
        p = self.__p
        g = find_first_generator(p)
        a = random.randint(1, p - 2)
        g_a = pow(g, a, p)

        self.__public_key = p, g, g_a
        self.__private_key = a
