# Create a function to encrypt the contents of a file, whose name should be provided by the user. 
# The key should be random, or provided by the user. 
# The user must provide (as program parameters or by request or any other suitable method): 
#   (i) the name of the file to encrypt, 
#   (ii) the name of the file to store the cryptogram, 
#   (iii) the name of the encryption algorithm. 
# Check the documentation and implement functions using multiple ciphers. We recommend AES and ChaCha20.

import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def read_data(filename):
    with open(filename, "rb") as file:
        data= file.read()

    return data

def generate_crypto_materials():
    key = os.urandom(32)
    iv = os.urandom(16)
    #print("iv: ", iv, "\n\nkey: ", key)
    return key, iv

    
def store_data(data, output):
    with open(output, "wb") as out:
        out.write(data)


def encrypt_file(filename, output, algoritm, mode):
    data= read_data(filename)
    key, iv = generate_crypto_materials()
    encrypted_data= encrypt_data(data, key, iv, algoritm, mode)
    store_data(encrypted_data, output)

def padd_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

def encrypt_data(data, key, iv, algoritm, mode):
    if algoritm.upper() == 'AES':
        cipher_algoritm = algorithms.AES(key)

    if mode.upper() == "CBC":
        cipher = Cipher(cipher_algoritm, modes.CBC(iv))
    elif mode.upper() == "OFB":
        cipher = Cipher(cipher_algoritm, modes.OFB(iv))
    elif mode.upper() == "CFB":
        cipher = Cipher(cipher_algoritm, modes.CFB(iv))
    else:
        print("ERROR! invalid mode")
        exit()
    
    encryptor = cipher.encryptor()
    padded_data= padd_data(data)
    ct = iv+key+ encryptor.update(padded_data) + encryptor.finalize()
    return ct



def main(args):
    #breakpoint()

    if len(args) < 4:
        print("ERROR! Invalid Args: filename output algoritm mode")
        exit()

    filename= args[1]
    output= args[2]
    algoritm= args[3]
    mode= args[4]

    encrypt_file(filename, output, algoritm, mode)

    return 0


main(sys.argv)

