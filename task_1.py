from hashlib import sha256
import random
import string
import time

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

#part c: find 2 distinct str m0, m1 that hash to same truncated hash
# CHANGE to handle diff size bits later
def collisions(bits, sha_m0, input_bits):
    #hash and print to screen in hex format
    sha_bits = sha256(bits.encode()).hexdigest()[:(input_bits // 4)]
    return sha_bits == sha_m0

def bit_combinations(m0, input_bits):
    sha_m0 = sha256(m0.encode()).hexdigest()[:(input_bits // 4)] #modify later
    start_time = time.time()
    attempts = 0
    while True:
        m1 = "".join(random.choices(string.ascii_letters + string.digits, k=len(m0)))
        if collisions(m1, sha_m0, input_bits):
            print("Collision: ", "m0: ", m0, "m1: ", m1, "hash: ", sha_m0)
            end_time = time.time()
            return m1, attempts, end_time-start_time
        attempts +=1
 
def add_to_table():

    pass

            
def main():
    bits = 00000000
    str1 = "aleez"
    (m1, attempts, total_time) = bit_combinations(str1, 8)
    print(m1, attempts, total_time)
    #hash(str1, 8)

if __name__ == "__main__":
    main()