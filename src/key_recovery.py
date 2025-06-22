import text_processor as TP
import index_of_coincidence as IC

ENGLISH_IC = 0.067

# finds the most probable key lengths
def calculate_key_length(ciphertext: str, max_key_length=20) -> int:
    # the core of DP
    key_length_scores : dict[int, float] = {}
    for L in range(1, max_key_length+1):
        ciphertext_matrix : list[list[str]] = TP.create_text_matrix(ciphertext, L)

        column_ics : list[float] = []
        for col in range(L):
            column = TP.get_column(ciphertext_matrix, col)
            if (len(column) > 1): column_ics.append(IC.calculate_ic(column))

        avg_ic = sum(column_ics) / len(column_ics) if len(column_ics) > 0 else 0.0
        key_length_scores[L] = avg_ic

    return min(key_length_scores, key=lambda l: abs(key_length_scores[l] - ENGLISH_IC))


def crack_key(ciphertext: str) -> str:
    ciphertext = ciphertext.upper()
    key_length = calculate_key_length(ciphertext)

    ciphertext_matrix : list[list[str]] = TP.create_text_matrix(ciphertext, key_length)

    key = ["" for _ in range(key_length)]
    for i in range(key_length):
        curr_col = TP.get_column(ciphertext_matrix, i)
        scores = [0 for i in range(26)]

        for shift in range (26):
            scores[shift] = IC.text_frequency_score(TP.caesar_decrypt(curr_col, shift))
        key[i] = chr(scores.index(min(scores)) + 65)

    return TP.get_shortest_non_repeating_sequence(''.join(key).lower())