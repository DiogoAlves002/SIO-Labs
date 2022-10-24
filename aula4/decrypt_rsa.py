import sys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key



def main(args):

    check_args(args)

    encrypted_file= args[1]
    private_key_file= args[2]
    decrypted_file= args[3]

    encrypted_msg= get_message(encrypted_file)

    private_key= get_private_key(private_key_file)

    msg= decrypt(private_key, encrypted_msg)

    write_to_file(decrypted_file, msg)


def check_args(args):
    if len(args) < 4:
        print("ERROR: Invalid args! Correct usage: \"python3 encrypt_rsa.py encrypted_file private_key_file decrypted_file\"")
        exit(0)

def get_private_key(file):
    with open(file, "rb") as key_file:
        key = serialization.load_pem_private_key(key_file.read(), password=b'mypassword')
    return key


def decrypt(private_key, msg):

    decrypted_msg= private_key.decrypt(
        msg,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
    )
    return decrypted_msg


def write_to_file(file, msg):
    with open(file, "wb") as f:
        f.write(msg)



def get_message(msg_file):
    with open(msg_file, "rb") as f:
        msg= f.read()
    return msg



if __name__ == "__main__":
    main(sys.argv)
