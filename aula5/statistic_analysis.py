import sys
import hash as h
import os

def main(args):

    file_name, n= check_args(args)

    data= read_file(file_name)

    messages= new_messages(data, n)

    avg_similarity= compare(messages, bytearray(data))

    print(avg_similarity)



def compare(messages, original):
    avg_similarity= 0
    for m in messages:
        s= h.similarity(original, m)
        avg_similarity+= s
    return avg_similarity / len(messages)



def read_file(file_name):
    with open(file_name, 'rb') as f:
        data= f.read()
        return data

def new_messages(data, n):
    array_data= bytearray(data)
    size= len(array_data)
    messages= [array_data]
    for i in range(0, n):
        new_array= array_data
        ind = int.from_bytes(os.urandom(size), "big")
        new_array[0]= array_data[0] ^ (1 << ind)
        messages.appen(new_array)
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