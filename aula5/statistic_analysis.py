import random
import sys
import hash as h
from cryptography.hazmat.primitives import hashes
import os

def main(args):

    file_name, n= check_args(args)

    data= read_file(file_name)

    messages= new_messages(data, n)

    hashed_messages= hash_array(messages)

    avg_similarity= compare(hashed_messages, bytearray(data))

    print(avg_similarity)


def hash_array(array):
    hashed_array= []
    for i in range(len(array)):
        hashed_data= h.hash_data(array[i], hashes.SHA256())
        hashed_array.append(hashed_data)
    return hashed_array


def compare(messages, original):
    avg_similarity= 0
    for m in messages:
        s= h.similarity(original, m)
        #print("similarity: ", s)
        avg_similarity+= s
    return avg_similarity / len(messages)



def read_file(file_name):
    with open(file_name, 'rb') as f:
        data= f.read()
        return data

def new_messages(data, n):
    original_data= bytearray(data)
    size= len(original_data)
    messages= [original_data]
    for i in range(0, n):
        new_data= original_data[:]
        random_byte_index= random.randint(0, size-1)
        new_data[random_byte_index]= new_data[random_byte_index] ^ 0x80
        #byte= new_data[random_byte_index]
        #random_bit_index= random.randint(0, 7)
        #print((original_data))
        #byte[random_bit_index]= (byte[random_bit_index] + 1)%2 # flip bit
        #new_data[random_byte_index]= byte
        messages.append(new_data)
        #print(new_data, '\n')
    return messages



def check_args(args):
    if len(args) != 3:
        print("ERROR: Invalid args! Correct usage: \"python3 statistic_analysis.py file_name number_of_messages\"")
        exit(0)

    file_name= args[1]
    n= int(args[2])
    return file_name, n

if __name__ == "__main__":
    main(sys.argv)