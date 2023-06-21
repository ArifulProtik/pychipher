def Banner():
    print("Hello There What can i do for you? \n please Choose one Cipher Method")
    print("1) Caesar Cipher")
    print("2) Multiplicative Cipher")
    chosen = int(input("Enter your choice: "))
    return chosen
def Banner2():
    print("1) Encrypt")
    print("2) Decrypt")
    chosen = int(input("Enter your choice: "))
    return chosen

def encrypt_ceaser_text(plaintext,n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    print(ans)


def decrypt_ceaser(encrypted_message, k): 
    letters="abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""
    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    print("Your decrypted message is:\n")
    print(decrypted_message)

def encrypt_multi(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha(): 
            char_code = ord(char.upper()) - ord('A')
            cipher_code = (char_code * key) % 26
            ciphertext += chr(cipher_code + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decrypt_multi(ciphertext, key):
    plaintext = ""
    inverse_key = pow(key, -1, 26)
    for char in ciphertext:
        if char.isalpha():  
            char_code = ord(char.upper()) - ord('A')
            plain_code = (char_code * inverse_key) % 26
            plaintext += chr(plain_code + ord('A'))
        else:
            plaintext += char
    return plaintext


def DoTheJob():
    chosen = Banner()
    if chosen == 1:
        print("You have chosen Caesar Cipher")
        fc = Banner2()
        if fc == 1:
            print("You have chosen Encrypt")
            plaintext = input("Enter your text: ")
            n = int(input("Enter your key: "))
            print("Your encrypted message is: \n")
            encrypt_ceaser_text(plaintext,n)
        elif fc == 2:
            print("You have chosen Decrypt")
            encrypted_message = input("Enter your text: ")
            k = int(input("Enter your key: "))
            print("Your decrypted message is: \n")
            decrypt_ceaser(encrypted_message,k)
    elif chosen == 2:
        print("You have chosen Multiplicative Cipher")
        fc = Banner2()
        if fc == 1:
            print("You have chosen Encrypt")
            plaintext = input("Enter your text: ")
            key = int(input("Enter your key: "))
            print("Your encrypted message is: \n")
            print(encrypt_multi(plaintext, key))
        elif fc == 2:
            print("You have chosen Decrypt")
            ciphertext = input("Enter your text: ")
            key = int(input("Enter your key: "))
            print("Your decrypted message is: \n")
            print(decrypt_multi(ciphertext, key))

DoTheJob()
