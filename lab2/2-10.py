# 02-baseConversion.py

# Nella prima parte dell'esercizio i ragazzi fissano b = 7 e n = 256 nel codice;
# questa è la versione finale richiesta con lettura da standard input:
b = int(input("Inserisci la base di arrivo (b > 1): "))
max_val = (b ** 3) - 1
n = int(input("Inserisci il numero da convertire (tra 0 e " + str(max_val) + "): "))

if b <= 1 or n < 0 or n > max_val:
    print("Errore: valori fuori dall'intervallo consentito.")
else:
    valore_iniziale = n

    # Cifra meno significativa (posizione b^0)
    c0 = n % b
    n = n // b

    # Cifra intermedia (posizione b^1)
    c1 = n % b
    n = n // b

    # Cifra più significativa (posizione b^2)
    c2 = n % b

    print("Il numero", valore_iniziale, "in base", b, "si scrive:", str(c2) + str(c1) + str(c0))
    # Verifica opzionale come da testo:
    print("Verifica:", c2, "*", b, "^2 +", c1, "*", b, "^1 +", c0, "*", b, "^0 =", c2 * (b**2) + c1 * b + c0)