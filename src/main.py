from el_gamal import ElGamal

def main():
    elgamal = ElGamal()

    msg = "hello "
    encrypted_msg = elgamal.encrypt(msg)
    decrypted_msg = elgamal.decrypt(encrypted_msg)

    print(f"Original message: {msg}")
    print(f"Encrypted message: {encrypted_msg}")
    print(f"Decrypted message: {decrypted_msg}")

if __name__ == "__main__":
    main()
