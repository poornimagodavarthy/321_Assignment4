from hashlib import sha256
import random
import string
import time
import matplotlib.pyplot as plt
import csv

#part a, b
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

def collisions(m0, input_bits):
    hash_table = {}
    hashed_m0 = sha256(m0.encode()).hexdigest()[:(input_bits // 4)] 
    hash_table[hashed_m0] = m0
    start_time, end_time = time.time(), time.time()

    attempts = 0
    while True:
        m1 = "".join(random.choices(string.ascii_letters + string.digits, k=len(m0)))
        hashed_m1 = sha256(m1.encode()).hexdigest()[:(input_bits // 4)]
        if hashed_m1 in hash_table:
            end_time = time.time()
            print("Collision: ", "m0: ", m0, "m1: ", m1, "hash: ", hashed_m0)
            break
        hash_table[hashed_m1] = m1
        attempts +=1
    return m1, attempts, end_time-start_time
        
 
def add_to_table(str1):
    collision_times, num_attempts = [], []
    sizes = list(range(8, 51, 2))
    for size in sizes:
        print(f"--size: {size}--")
        (m1, attempts, total_time) = collisions(str1, size)
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