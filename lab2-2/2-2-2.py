# 04-standardDeviation2.py

numeri = []

# Fase 1: Acquisizione dati nella lista fino alla sentinella "STOP"
riga = input("Inserisci un numero intero (scrivi STOP per terminare): ")
while riga != "STOP":
    numeri.append(int(riga))
    riga = input("Inserisci un numero intero (scrivi STOP per terminare): ")

n = len(numeri)

if n < 2:
    print("Errore: sono necessari almeno due numeri.")
else:
    # Primo passaggio sulla lista: calcolo della media m
    somma = 0
    for x in numeri:
        somma = somma + x
    media = somma / n

    # Secondo passaggio sulla lista: somma degli scarti quadratici dalla media
    somma_scarti_quad = 0.0
    for x in numeri:
        scarto = x - media
        somma_scarti_quad = somma_scarti_quad + (scarto * scarto)

    # Calcolo finale della deviazione standard
    D = (somma_scarti_quad / (n - 1)) ** 0.5
    print("Deviazione standard:", D)