# Alter your program by adding a function that decrypts a user file. 
# For this functionality, the user must provide the following (as program parameters or by request or any other suitable method): 
#   (i) the name of the file to decrypt, 
#   (ii) the name of the file to store the decryption result. 
# The key must be requested.


import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def read_data(filename):
    with open(filename, "rb") as file:
        data= file.read()

    return data

def store_data(data, output):
    with open(output, "wb") as out:
        out.write(data)

def decrypt_file(filename, output, algoritm, mode):
    data= read_data(filename)
    iv = data[:16]
    key = data[16: 16+32]
    data= data[16+32:]
    #print("iv: ",iv,"\n\nkey: ", key, "\n\ndata: ", data )
    decrypted_data= decrypt_data(data, key, iv, algoritm, mode)
    store_data(decrypted_data, output)


def unpadd_data(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data)
    data += unpadder.finalize()
    return data

def decrypt_data(data, key, iv, algoritm, mode):
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
    
    decryptor = cipher.decryptor()
    padded_data= decryptor.update(data) + decryptor.finalize()
    decrypted_data= unpadd_data(padded_data)
    
    return decrypted_data



def main(args):
    #breakpoint()

    if len(args) < 4:
        print("ERROR! Invalid Args: filename output algoritm mode")
        exit()

    filename= args[1]
    output= args[2]
    algoritm= args[3]
    mode= args[4]
    
    decrypt_file(filename, output, algoritm, mode)

    return 0


main(sys.argv)

