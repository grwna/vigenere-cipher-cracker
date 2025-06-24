

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
        numerator += (occurences.get(chr(i+65), 0)*(occurences.get(chr(i+65), 0)-1))
    return numerator/denominator


english_letter_frequency = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

# uses Chi-Squared Correlation Test
def goodness_of_fit(text : str):
    expected : list[float] = [0 for _ in range(c)]
    observed : list[float] = [0 for _ in range(c)]

    occurences = get_letter_occurences(text)
    sums = 0
    for i in range(c):
        expected[i] = (english_letter_frequency[chr(i+65)]/100) * len(text)
        observed[i] = occurences.get(chr(i+65), 0)

        sums += pow(expected[i]-observed[i], 2)/expected[i]
    return sums

def calculate_levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    len_s1 = len(s1)
    len_s2 = len(s2)
    previous_row = list(range(len_s1 + 1))

    for i in range(1, len_s2 + 1):
        current_row = [i]
        
        for j in range(1, len_s1 + 1):
            ins_cost = current_row[j-1] + 1
            del_cost = previous_row[j] + 1
            
            subs_cost = previous_row[j-1]
            if s1[j-1] != s2[i-1]:
                subs_cost += 1
            
            current_row.append(min(ins_cost, del_cost, subs_cost))
        previous_row = current_row
    return previous_row[len_s1]

def calculate_similarity_percentage(s1: str, s2: str) -> float:
    if (len(s1) == 0 and len(s2) == 0) : return 1

    max_len : int = max(len(s1), len(s2))
    distance : int = calculate_levenshtein_distance(s1, s2)
    return 1 - (distance/max_len)
