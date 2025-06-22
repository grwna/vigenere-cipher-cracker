# Vigenère Cipher Cracker with Index of Coincidence

## 📖 Description
This project containts Python implementation of a Vigenère cipher cracker. The cracker works by finding the most probable length of the key through Index of Coincidence calculation that utilizes Dynammic Programming to speed up the process by tabulating each IC values found and then solving the minimization. <br>
After the IC values are found, and the length of the key is determined, it then separates the string into a matrix where each row is as long as the determined length of the key, and for each column in that matrix, we test out each possible shift (0-25) to see which shift is the most english-like. The English-like calculation is done using Chi-Squared Goodness Of Fit test

This project is a part of Algorthmic Strategy course's paper titled "*Attack on the Vigenère Cipher Key Through Index of Coincidence Optimization Based on Dynamic Programming*" 

## Concepts Used
- Dynammic Programming
- Index of Coincidence
- Chi-Squared Goodness of Fit test


## 📂 Program Structure
```
.
├── doc
├── LICENSE
├── README.md
├── src
│   ├── calculation.py
│   ├── key_cracker.py
│   ├── main.py
│   ├── text_processor.py
│   └── vigenere.py
└── test
    ├── keys.txt
    ├── result1.txt
    ├── result2.txt
    ├── result3.txt
    ├── result4.txt
    ├── result5.txt
    └── text.txt

4 directories, 14 files
```

## 🚀 How to Use
> [!note]
> Make sure you have `Python 3.11` installed before running

1. Clone the repository
2. run the app using  `python src/main.py [N]` or `python3 src/main.py [N]`, where *N* is the amount of keys to test
3. If you wish to change the plaintext to be tested, you may modify the `text.txt` file inside the `test` folder

## 🧑‍💻 Author
 | NIM | Name | Github |
 | --- | ---- | ------ |
 | 13523035 | M.Rayhan Farrukh | [@grwna](https://github.com/grwna) |

