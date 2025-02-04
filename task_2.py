import bcrypt
import time
#import fitz

import nltk
nltk.download('words')
from nltk.corpus import words

def crack_password(word, hash_val):
    word_bytes = word.encode('utf-8')
    return bcrypt.checkpw(word_bytes, hash_val)

def try_passwords(hash_val):
    word_list = words.words()
    for word in word_list:
        # compute hash
        if 6 <= len(word) and 10 >= len(word):
            if crack_password(word, hash_val):
                return word

def extract_shadow(bcrypt_str):
    parts = bcrypt_str.strip().split(":")
    user = parts[0]
    hash_val = parts[1]
    print("EXTRACTED VALUES: ")
    print("User: ", user)
    print(hash_val)
    return hash_val.encode('utf-8')

def main():
    shadow_path = './shadow.pdf'
    txt_path = './shadow_text.txt'
    '''pdf_doc = fitz.open(shadow_path)
    with open(txt_path, 'w', encoding="utf-8") as text_file:
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc.load_page(page_num)
            text = page.get_text("text")
            text_file.write(text)
    pdf_doc.close()'''

    with open(txt_path, 'r') as text_file:
        lines = text_file.readlines()
        for line in lines:
            hash_val = extract_shadow(line)
            start_time = time.time()
            print("###################")
            print("PASSWORD:", try_passwords(hash_val))
            end_time = time.time()
            print("TIME ELAPSED:", end_time - start_time)
            print("###################")
main()