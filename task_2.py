import bcrypt
from nltk.corpus import words
import fitz

def crack_password(word, hash_val, salt, algorithm):
    word_bytes, salt = word.encode(), salt.encode()
    hashed = bcrypt.hashpw(word_bytes, salt)
    return hashed == hash_val

def extract_shadow(bcrypt_str):
    parts = bcrypt_str.split("$")
    algorithm = parts[1]
    workfactor = int(parts[2])
    salt = parts[3]
    hash_val = parts[4]
    return algorithm, workfactor, salt, hash_val

def try_passwords(algorithm, salt, hash_val):
    word_list = words.words()
    for word in word_list:
        # compute hash
        if 6 <= len(word) and 10 >= len(word):
            if crack_password(word, hash_val, salt, algorithm) == True:
                return word

def main():
    shadow_path = './shadow.pdf'
    txt_path = './shadow_text.txt'
    pdf_doc = fitz.open(shadow_path)
    with open(txt_path, 'w', encoding="utf-8") as text_file:
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc.load_page(page_num)
            text = page.get_text("text")
            text_file.write(text)
    pdf_doc.close()
'''
    with open(txt_path, 'r') as text_file:
        lines = text_file.readlines()
        for line in lines:
            algorithm, workfactor, salt, hash_val = extract_shadow(line)
            print(try_passwords(bcrypt, salt, hash_val))
            #call stuff'''
main()