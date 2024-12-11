import string


def alphabet():
    data = []
    alphabets = string.ascii_uppercase;
    for char in alphabets:
        data.append(char)
    return data

def encrypt(text: str, num: int)->str:
    all_alphabet = alphabet()
    modified_text = text.replace(" ", "").replace("_", "")
    modified_text_uppercase = modified_text.upper()
    encrypted_text = ""
    for data in range(len(modified_text_uppercase)):
        for letter in range(len(all_alphabet)):
            if all_alphabet[letter] == modified_text[data]:
                digit = letter + num
                encrypted_text += all_alphabet[digit]
    return encrypted_text;

def decryption(text: str, num: int)-> str:
    all_alphabet = alphabet()
    modified_text = text.replace(" ", "").replace("_", "")
    modified_text_uppercase = modified_text.upper()
    encrypted_text = ""
    digit = 0
    for data in range(len(modified_text_uppercase)):
        for letter in range(len(all_alphabet)):
            if all_alphabet[letter] == modified_text[data]:
                digit = letter - num
                encrypted_text += all_alphabet[digit]
    return encrypted_text;




