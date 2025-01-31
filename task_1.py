from hashlib import sha256

def hash(str1, str2):
    #hash and print to screen in hex format
    str1_hash = sha256(str1.encode()).digest()
    print(str1_hash)
    str1_hash = sha256(str1.encode()).digest()
    print(str1_hash)
    str2_hash = sha256(str2.encode()).digest()
    str1_bit = str1_hash[0] #8
    str2_bit = str2_hash[0] #8


def main():
    str1 = "turtle"
    str2 = "4urtle"
    hash(str1, str2)

main()