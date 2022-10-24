import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def main(args):

    if check_args(args):
        exit(0)

    msg_file= args[1]
    public_key_file= args[2]
    encrypted_file= args[3]

    public_key= get_public_key(public_key_file)

    msg= get_message(msg_file)

    cypher_text= encrypt(public_key, msg)

    write_to_file(encrypted_file, cypher_text)


def check_args(args):
    if len(args)< 4:
        print("ERROR: Invalid args! Correct usage: \"python3 encrypt_rsa.py original_file public_key_file encrypted_file\"")
        return 1
    return 0


def get_public_key(public_key_file):
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    return public_key


def encrypt(public_key, msg):

    ciphertext = public_key.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext



def get_message(msg_file):
    with open(msg_file, "rb") as f:
        msg= f.read()
    return msg


def write_to_file(file, msg):
    with open(file, "wb") as f:
        f.write(msg)



if __name__ == "__main__":
    main(sys.argv)
