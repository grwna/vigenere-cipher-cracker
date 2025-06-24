import key_cracker as KR
import vigenere as VC
from text_processor import calculate_alphabetic_lengths
from statistics_tools import calculate_similarity_percentage
import random, time

def main():
    texts = [line.strip() for line in open("test/text.txt", "r").readlines()]
    keys = [line.strip() for line in open("test/keys.txt", "r").readlines()]

    filename = f"test/results.txt" 
    with open(filename, "w") as f:
        f.write("================================= TEXTS USED ===================================\n")
        for i in range(3):
            f.write(f"Text {i+1}" + "\n")
            f.write(texts[i] + "\n")
            f.write(f"String Length: " + str(len(texts[i])) + "\n")
            f.write(f"Alphabetic Length: " + str(calculate_alphabetic_lengths(texts[i])) + "\n\n")
        f.write("================================= KEYS USED ====================================\n")
        for i in range(3):
            f.write(f"Key {i+1}: " + keys[i] + ",   length: " + str(len(keys[i])) + "\n")
        f.write("\n\n================================ RESULTS =======================================\n\n")

    total_runtime = time.time()
    for i in range(6):
        if i < 3:
            original_key = keys[1]
            ciphertext = VC.encrypt(texts[i], original_key)
        else:
            original_key = keys[i % 3]
            ciphertext = VC.encrypt(texts[0], original_key)

        cracktime = time.time() 
        cracked_key = KR.crack_key(ciphertext)
        cracktime = time.time() - cracktime
        
        plaintext = VC.decrypt(ciphertext, cracked_key)

        with open(filename, "a") as f:
            f.write("Original Key: " + original_key + "\n")
            f.write("Ciphertext" + "\n" + ciphertext + "\n")
            f.write("\n")
            f.write("Cracked Key: " + cracked_key + "\n")
            f.write("Cracked Text" + "\n" + plaintext + "\n")
            f.write("\n")
            f.write("Accuracy: " + str(round(calculate_similarity_percentage(original_key, cracked_key), 6) * 100)  + "%\n")
            f.write("Cracking Time: " + str(cracktime) + "ms")
            f.write("\n================================================================================\n\n")

    open(filename, "a").write("Total program runtime: " + str(time.time() - total_runtime)) 

if __name__=="__main__":
    main()
    
