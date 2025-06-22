def clean_text(text: str) -> str:
    text = text.upper()
    newtext : str = ""
    for char in text:
        if ord(char) >= 65 and ord(char) <= 65+26:
            newtext += char
    return newtext


# takes a matrix of text, then decrypt a certain column, TEXTS ARE UPPERCASE
def caesar_decrypt(text: list, shift : int) -> str:
    result = ""
    for char in text:
        result += chr(((ord(char) - 65 - shift) % 26) + 65)
    return result


def create_text_matrix(text: str, row_len: int) -> list[list[str]]:
    text_only_alphabets = ''.join(char for char in text if char.isalpha())
    return [list(text_only_alphabets[i:i+row_len]) for i in range(0, len(text_only_alphabets), row_len)]


def get_column(matrix : list[list[str]], column : int) -> str:
    column_chars = [row[column] for row in matrix if column < len(row)]
    return "".join(column_chars)


# turns newkeynewkeynewkey into newkey
def get_shortest_non_repeating_sequence(text: str) -> str:
    n = len(text)
    for length in range(1, n+1):
        prefix = text[:length]
        if n % length == 0:
            if (prefix*(n//length) == text):
                return prefix
    return text

    
if __name__ == "__main__":
    print(clean_text(" aksjdaiwuj!8* ad ?.;\";"))
