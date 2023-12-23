from el_gamal import ElGamal
from utils import generate_prime

def main():
    p = generate_prime()
    elgamal = ElGamal(p)

    msg = "hi"
    encrypted_msg = elgamal.encrypt(msg)
    decrypted_msg = elgamal.decrypt(encrypted_msg)

    print(f"Original message: {msg}")
    print(f"Encrypted message: {encrypted_msg}")
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()
