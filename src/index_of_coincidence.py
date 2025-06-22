english_letter_frequency = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

c : int = 26  # English Alphabets
def get_letter_occurences(text : str) -> dict[str, int]:
    result = {}
    for char in text:
        if char not in result:
            result[char] = 0
        result[char] += 1
    return result

# operates on uppercases
def calculate_ic(text : str) -> float:
    numerator : int = 0
    denominator : float = len(text)*(len(text)-1)

    occurences : dict[str, int] = get_letter_occurences(text) 

    for i in range(c):
        numerator += (occurences[chr(i+65)]*(occurences[chr(i+65)]-1))
    return numerator/denominator

# uses Chi-Squared Correlation Test
def text_frequency_score(text : str):
    expected : list[float] = [0 for i in range(c)]
    observed : list[float] = [0 for i in range(c)]

    occurences = get_letter_occurences(text)
    sums = 0
    for i in range(c):
        expected[i] = english_letter_frequency[chr(i+65)] * len(text)
        observed[i] = occurences[chr(i+65)]

        sums += pow(expected[i]*observed[i], 2)/expected[i]
    return sums
# HOW TO USE
# To test a column (AFTER finding key length)
# try all 26 caesar shifts on the column
# the decrypted column after, calculate the CHI-Squared score
# the shifts with the lowest score is likely the correct one

    
     