import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def main(args):
    
    if check_args(args):
        exit(0)

    generate_key_par(args)


def check_args(args):
    if len(args) < 4: 
        print("ERROR: Invalid args! Correct usage: \"python3 generate_rsa.py length private_file public_file\" ")
        return 1

    length= int(args[1])
    acceptable_length= [1024, 2048, 3072, 4096]

    if length not in acceptable_length:
        print("ERROR! Invalid length! Acceptable choices: 1024, 2048, 3072, 4096")
        return 1

    return 0


def generate_key_par(args):

    length= int(args[1])
    private_file= args[2]
    public_file= args[3]

    private_key = rsa.generate_private_key(65537, length)
    public_key= private_key.public_key()

    pem_private, pem_public = pem(private_key, public_key)

    write_to_file("keys/"+ private_file, pem_private)
    write_to_file("keys/"+ public_file, pem_public)



def write_to_file(file, msg):
    with open(file, "wb") as f:
        f.write(msg)



def pem(private_key, public_key):
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
    )
    
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem_private, pem_public



if __name__ == "__main__":
    main(sys.argv)
