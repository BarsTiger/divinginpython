import sys

etashi = int(sys.argv[1])

probels = etashi
symb = input("Введите символ, из которого хотите получить лестницу:     ")
lestnitsa_lvl = ""

for symbols in range(1, etashi+1):
    lestnitsa_lvl = " "*probels + symb*symbols
    print(lestnitsa_lvl)
    probels = probels - 1
    
