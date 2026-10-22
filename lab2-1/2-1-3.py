# 03-standardDeviation.py

n = 0
B = 0  # Somma di tutti i valori
A = 0  # Somma dei quadrati di tutti i valori

riga = input("Inserisci un numero intero (scrivi STOP per terminare): ")

while riga != "STOP":
    valore = int(riga)
    
    n = n + 1
    B = B + valore
    A = A + (valore * valore)
    
    riga = input("Inserisci un numero intero (scrivi STOP per terminare): ")

if n < 2:
    print("Errore: sono necessari almeno due numeri per calcolare la deviazione standard.")
else:
    D = ((A - B * B / n) / (n - 1)) ** (1 / 2)
    print("Deviazione standard:", D)