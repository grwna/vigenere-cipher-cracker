import key_cracker as KR
import vigenere as VC
import sys, random, time

def main(ciphertext_count: int):
    text = open("test/text.txt", "r").read()
    keys = [line.strip() for line in open("test/keys.txt", "r").readlines()]
    
    for i in range(int(ciphertext_count)):
        original_key = keys[random.randint(1, len(keys))]
        ciphertext = VC.encrypt(text, original_key)

        cracktime = time.time() 
        cracked_key = KR.crack_key(ciphertext)
        cracktime = time.time() - cracktime
        
        plaintext = VC.decrypt(ciphertext, cracked_key)

        with open(f"test/result{i+1}.txt", "w") as f:
            f.write("Original Key: " + original_key + "\n")
            f.write("Ciphertext: " + ciphertext + "\n")
            f.write("\n")
            f.write("Cracked Key: " + cracked_key + "\n")
            f.write("Cracked Text: " + plaintext + "\n")
            f.write("\n")
            f.write("Cracking Time: " + str(cracktime) + "ms")



if __name__=="__main__":
    main(sys.argv[1])
    
