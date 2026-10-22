# 04-someNumbers2.py

numeri = []

# Fase 1: Acquisizione dell'intera sequenza nella lista
riga = input("Inserisci un numero intero (invio a vuoto per terminare): ")
while riga != "":
    numeri.append(int(riga))
    riga = input("Inserisci un numero intero (invio a vuoto per terminare): ")

# Fase 2: Controllo validità ed elaborazione
if len(numeri) < 2:
    print("Errore: devi inserire almeno due numeri.")
else:
    somma = 0
    somma_assoluti = 0
    prodotto = 1

    for n in numeri:
        somma = somma + n
        if n < 0:
            somma_assoluti = somma_assoluti - n
        else:
            somma_assoluti = somma_assoluti + n
        prodotto = prodotto * n

    media = somma / len(numeri)

    print("Somma:", somma)
    print("Somma dei valori assoluti:", somma_assoluti)
    print("Prodotto:", prodotto)
    print("Valore medio:", media)