def clean_text(text: str) -> str:
    text = text.upper()
    newtext : str = ""
    for char in text:
        if ord(char) >= 65 and ord(char) <= 65+26:
            newtext += char
    return newtext

# takes a matrix of text, then decrypt a certain column, TEXTS ARE UPPERCASE
def caesar_decrypt_columns(texts: list[str], col_idx : int, shift : int) -> None:
    for i in range(len(texts)):
        row = list(texts[i])
        row[col_idx] = chr(((ord(row[col_idx]) - 65) + shift % 26) + 65)
        texts[i] = ''.join(row)



if __name__ == "__main__":
    print(clean_text(" aksjdaiwuj!8* ad ?.;\";"))

    lis = ["abc", "bcd", "cde", "def", "efg"]
    caesar_decrypt_columns(lis, 1, 2)
    print(lis)