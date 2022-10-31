import sys

from cryptography.hazmat.primitives import hashes


def main(args):

    possible_hash_functions= {'MD5': hashes.MD5(), 'SHA256': hashes.SHA256(), 'SHA384': hashes.SHA384(), 'SHA512': hashes.SHA512(), 'BLAKE2': hashes.BLAKE2b(64)}

    file_name, hash_function= check_args(args, possible_hash_functions)

    data= read_file(file_name)

    hashed_data= hash_data(data, hash_function)

    flipped_bit_data= flip_bit(data)

    flipped_bit_hashed_data= hash_data(flipped_bit_data, hash_function)


    save_hash(hashed_data, False)
    save_hash(flipped_bit_hashed_data, True)

    print_hash(hashed_data)
    print_hash(flipped_bit_hashed_data)



def flip_bit(data):
    array_data= bytearray(data)
    array_data[0]= array_data[0] ^ 0x80

    return bytes(array_data)

def save_hash(hashed_data, flipped_bit):
    if flipped_bit:
        with open ('flipped_bit_hash.txt', 'w') as f:
            f.write(hashed_data.hex())
    else:
        with open('original_hash.txt', 'w') as f2:
            f2.write(hashed_data.hex())

def print_hash(hashed_data):
    print( hashed_data.hex())

def hash_data(data, hash_function):
    digest= hashes.Hash(hash_function)
    digest.update(data)
    return digest.finalize()


def read_file(file_name):
    with open(file_name, 'rb') as f:
        data= f.read()
    return data


def check_args(args, possible_hash_functions):
    if len(args) != 3:
        print("ERROR: Invalid args! Correct usage: \"python3 hash.py file_name hash_function\"")
        exit(0)
    elif args[2].upper() not in possible_hash_functions.keys():
        print("ERROR: Invalid hash function! possible choices: MD5, SHA256, SHA384, SHA512, Blake2")
        exit(0)
    return args[1], possible_hash_functions[args[2].upper()]



if __name__ == "__main__":
    main(sys.argv)
