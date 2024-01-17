from el_gamal import ElGamal
from utils import generate_prime


def main():
    p = generate_prime()
    elgamal = ElGamal(p)
    result = []
    encrypted_msg_list = []
    msg = "elgamalforpkc"
    sep = "" #separator

    for m in msg:
        encrypted_msg = elgamal.encrypt(m)
        decrypted_msg = elgamal.decrypt(encrypted_msg)
        encrypted_msg_list.append(encrypted_msg)
        result.append(decrypted_msg)

    print(f"Original message: {msg}")
    print(f"Encrypted message: {encrypted_msg_list}")
    print(f"Decrypted message: {sep.join(result)}")

    # msg_to_int = message_to_int(msg)
    # int_to_msg = encryption_code_to_str(msg_to_int)
    #
    # print(f"Message to int: {msg_to_int} and p: {p}")
    # print(f"Int to Message: {int_to_msg}")

if __name__ == "__main__":
    main()
