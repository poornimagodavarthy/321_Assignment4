from hashlib import sha256
import random
import string
import time
import matplotlib.pyplot as plt
import csv

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
 
def add_to_table(str1):
    collision_times, num_attempts = [], []
    sizes = list(range(8, 51, 2))
    for size in sizes:
        print(f"--size: {size}--")
        (m1, attempts, total_time) = bit_combinations(str1, size)
        collision_times.append(total_time)
        num_attempts.append(attempts)

    with open('collisions.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Digest Size (bits)", "Collision Time (seconds)", "Attempts"])
        for size, time, attempt in zip(sizes, collision_times, num_attempts):
            writer.writerow([size, time, attempt])

    return sizes, collision_times, num_attempts

def plot_graph(sizes, collision_times, attempts):
    #collision time vs hash size
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, collision_times, marker='o', color='b')
    plt.xlabel("Digest Size (bits)")
    plt.ylabel("Collision Time (seconds)")
    plt.title("Collision Time vs Digest Size")

    plt.subplot(1, 2, 2)
    plt.plot(sizes, attempts, marker='o', color='r')
    plt.xlabel("Digest Size (bits)")
    plt.ylabel("Number of Attempts")
    plt.title("Attempts vs Digest Size")
    plt.tight_layout()
    plt.show()

        
def main():
    str1 = "Aleeeeeez"
    sizes, collision_times, attempts = add_to_table(str1)
    plot_graph(sizes, collision_times, attempts)

if __name__ == "__main__":
    main()