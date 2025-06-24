# Vigenère Cipher Cracker with Index of Coincidence

## 📖 Description
This project containts Python implementation of a **Vigenère cipher cracker**. The cracker works by finding key length through **Index of Coincidence** calculation with **Dynammic Programming**

After key length is determined, the string is structured as a matrix, and for each column in that matrix,  test each possible shift (0-25) to see which shift is the most english-like. The English-like calculation is done using **Chi-Squared Goodness Of Fit test**. The recovered key is then tested against the original key used using the **Levenshtein Edit Distance** to measure accuracy of the solver.

This project is a part of IF2211 Algorithmic Strategy course's paper titled "*Attack on the Vigenère Cipher Key Through Index of Coincidence Optimization Based on Dynamic Programming*" 

## Concepts Used
- Dynammic Programming
- Index of Coincidence
- Chi-Squared Goodness of Fit test
- Levenshtein Edit Distance

## 📂 Program Structure
```
.
├── doc
│   └── Attack on the Vigenère Cipher Key Through Index of Coincidence Optimization Based on Dynamic Programming.pdf
├── LICENSE
├── README.md
├── src
│   ├── key_cracker.py
│   ├── main.py
│   ├── statistics_tools.py
│   ├── text_processor.py
│   └── vigenere.py
└── test
    ├── keys.txt
    ├── results.txt
    └── text.txt

4 directories, 11 files
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

