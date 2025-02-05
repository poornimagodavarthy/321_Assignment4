from hashlib import sha256
import random
import string

#part a, b
# check if sha's equal
def hash(str1, input):
    #convert to bytes
    str1_bytes = ''.join(format(ord(c), '08b') for c in str1)
    print(sha256(str1.encode()).hexdigest()[:input]) # unflipped hash
    #flip bits
    flipped = list(str1_bytes)
    index = random.randint(0, len(flipped)-1)
    flipped[index] = '1' if flipped[index] == '0' else '0'
    binary_string = "".join(flipped)
    #convert back to str
    flipped_chars = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(flipped), 8)]
    flipped_str = "".join(flipped_chars)
    #hash and print to screen in hex format
    flipped_hash = sha256(flipped_str.encode()).hexdigest()[:input]
    print(flipped_hash) #print flipped hash

# go thru all possible bit combinations

#part c
def collisions(bits, sha_m0):
    #hash and print to screen in hex format
    sha_bits = sha256(bits.encode()).digest()[0]
    return sha_bits == sha_m0

def bit_combinations(m0):
    sha_m0 = sha256(m0.encode()).digest()[0] #modify later
    m0_binary = ''.join(format(ord(c), '08b') for c in m0)
    m0_int = int(m0_binary, 2)
    out_string = ""
    for i in range(256):
        if m0_int != i:
            bits = format(i, '08b')
            output = collisions(bits, sha_m0)
            if output == True:
                #binary str, then string
                bin_str = format(i, '08b')
                mod = len(bin_str) % 8
                for y in range(mod, len(bin_str), 8):
                    integer = int(y)
                    char = chr(integer)
                    out_string += char
                print(out_string)
                break


def add_to_table():

    pass

            
def main():
    bits = 00000000
    str1 = "turtle"
    #output = bit_combinations(str1)
    #print(output)
    hash(str1, 8)

if __name__ == "__main__":
    main()