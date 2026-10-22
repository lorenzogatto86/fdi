# 03-euclideMCD.py

a = int(input("Inserisci il primo numero intero positivo: "))
b = int(input("Inserisci il secondo numero intero positivo: "))

if a <= 0 or b <= 0:
    print("Errore: entrambi i numeri devono essere interi positivi.")
else:
    # Copio a e b in m ed n per non perdere i valori originali per la stampa finale
    if a >= b:
        m = a
        n = b
    else:
        m = b
        n = a

    # Algoritmo di Euclide
    resto = m % n
    while resto != 0:
        m = n
        n = resto
        resto = m % n

    # Stampa rigorosamente senza spazi come richiesto dalle specifiche
    print("MCD(", a, ",", b, ")=", n, sep="")