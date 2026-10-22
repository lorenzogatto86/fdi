# 03-someNumbers.py

somma = 0
somma_assoluti = 0
prodotto = 1
contatore = 0

riga = input("Inserisci un numero intero (invio a vuoto per terminare): ")

while riga != "":
    numero = int(riga)
    
    somma = somma + numero
    if numero < 0:
        somma_assoluti = somma_assoluti - numero
    else:
        somma_assoluti = somma_assoluti + numero
        
    prodotto = prodotto * numero
    contatore = contatore + 1
    
    riga = input("Inserisci un numero intero (invio a vuoto per terminare): ")

if contatore < 2:
    print("Errore: devi inserire almeno due numeri.")
else:
    media = somma / contatore
    print("Somma:", somma)
    print("Somma dei valori assoluti:", somma_assoluti)
    print("Prodotto:", prodotto)
    print("Valore medio:", media)