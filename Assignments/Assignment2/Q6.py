# crypt = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}
# st = list(input("Enter a string to be ciphered: "))
# s_new=''
# for i in range (len(st)):
#     st[i]=crypt[st[i]]
# print("".join(st))


# Original cipher for encryption (shift by +3)
encrypt_cipher = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i',
                  'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o',
                  'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u',
                  's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a',
                  'y': 'b', 'z': 'c'}

# Create reverse cipher for decryption (shift by -3)
decrypt_cipher = {v: k for k, v in encrypt_cipher.items()}



def decrypt_text(text):
    """Decrypt text using Caesar cipher (shift -3)"""
    result = ''
    for char in text.lower():
        if char in decrypt_cipher:
            result += decrypt_cipher[char]
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result



def your_program_fixed():
    st = input("Enter a string to be ciphered: ").lower()  # Convert to lowercase
    s_new = ''

    for char in st:
        if char in encrypt_cipher:
            s_new += encrypt_cipher[char]
        else:
            s_new += char  # Handle spaces, punctuation, etc.

    print(f"Encrypted: {s_new}")
    return s_new



encrypted = 'nbrkrq'
decrypted = decrypt_text(encrypted)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")


