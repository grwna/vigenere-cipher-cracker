def encrypt(text: str, key: str, encrypt=True) -> str:
    ciphertext : str = ""
    text = text.lower()
    key_index : int = 0
    for char in text:
        if (ord(char) >= 97 and ord(char) <= 97+26):
            if encrypt:
                newcharcode : int = (((ord(char) - 97) + (ord(key[key_index]) - 97)) % 26) + 97
            else:
                newcharcode : int = (((ord(char) - 97) - (ord(key[key_index]) - 97)) % 26) + 97
            ciphertext += chr(newcharcode)
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext


def decrypt(text: str, key: str) -> str:
    return encrypt(text, key, False)

if __name__ == "__main__":
    plain = "The quick brown fox jumps over 13 lazy dogs."
    key = "cryptii"
    print(encrypt(plain, key))
    print(decrypt(encrypt(plain, key), key))