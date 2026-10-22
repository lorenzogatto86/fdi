# 03-guessNumber.py
import random

a = int(input("Inserisci l'estremo inferiore a (intero positivo): "))
b = int(input("Inserisci l'estremo superiore b (intero positivo, con a < b): "))

if a <= 0 or b <= 0 or a >= b:
    print("Errore: devono essere interi positivi con a < b.")
else:
    segreto = random.randint(a, b)
    tentativi = 0
    indovinato = False

    while not indovinato:
        tentativo = int(input("Fai un tentativo: "))
        tentativi = tentativi + 1

        if tentativo == segreto:
            indovinato = True
            print("Complimenti! Hai indovinato il numero in", tentativi, "tentativi!")
        elif tentativo < segreto:
            print("Troppo piccolo!")
        else:
            print("Troppo grande!")