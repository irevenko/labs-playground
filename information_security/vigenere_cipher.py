LETTERS = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # russian alphabet lol
MESSAGE_TO_ENCRYPT = "ИНФОРМАЦИЯ"
KEY = "КОД"


def encrypt(msg, key):
    cipher = ""
    msg_char_pos = [LETTERS.find(i) for i in msg]
    key_char_pos = [LETTERS.find(i) for i in key]
    msg_len = len(msg)
    key_length = len(key)

    for i in range(msg_len):
        letter = (msg_char_pos[i] + key_char_pos[i % key_length]) % len(LETTERS)
        cipher += LETTERS[letter]

    return cipher


def decrypt(cipher, key):
    decryptedMsg = ""
    cipher_char_pos = [LETTERS.find(i) for i in cipher]
    key_char_pos = [LETTERS.find(i) for i in key]
    cipher_length = len(cipher)
    key_length = len(key)

    for i in range(cipher_length):
        letter = (cipher_char_pos[i] - key_char_pos[i % key_length]) % len(LETTERS)
        decryptedMsg += LETTERS[letter]

    return decryptedMsg


e = encrypt(MESSAGE_TO_ENCRYPT, KEY)
d = decrypt(e, KEY)

print(e)
print(d)