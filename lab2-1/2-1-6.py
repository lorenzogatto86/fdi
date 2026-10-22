# 03-factoring-1.py

n = int(input("Inserisci un numero intero maggiore di 1: "))

if n <= 1:
    print("Errore: il numero deve essere maggiore di 1.")
else:
    fattore = 2
    while n > 1:
        if n % fattore == 0:
            print(fattore)
            n = n // fattore  # Divido n e NON incremento fattore (potrebbe dividerlo ancora!)
        else:
            fattore = fattore + 1  # Passo al divisore successivo solo quando non divide più