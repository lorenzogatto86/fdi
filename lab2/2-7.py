# 02-romanNumeral.py

n = int(input("Inserisci un numero intero positivo minore di 4000: "))

if n <= 0 or n >= 4000:
    print("Errore: il numero deve essere compreso tra 1 e 3999.")
else:
    # 1. Scomposizione del numero nelle singole cifre decimali
    migliaia = n // 1000
    centinaia = (n % 1000) // 100
    decine = (n % 100) // 10
    unita = n % 10

    romano = ""

    # 2. Conversione delle migliaia (da 1 a 3 -> M, MM, MMM)
    if migliaia == 1:
        romano = romano + "M"
    elif migliaia == 2:
        romano = romano + "MM"
    elif migliaia == 3:
        romano = romano + "MMM"

    # 3. Conversione delle centinaia (usando C, D, M)
    if centinaia == 1:
        romano = romano + "C"
    elif centinaia == 2:
        romano = romano + "CC"
    elif centinaia == 3:
        romano = romano + "CCC"
    elif centinaia == 4:
        romano = romano + "CD"
    elif centinaia == 5:
        romano = romano + "D"
    elif centinaia == 6:
        romano = romano + "DC"
    elif centinaia == 7:
        romano = romano + "DCC"
    elif centinaia == 8:
        romano = romano + "DCCC"
    elif centinaia == 9:
        romano = romano + "CM"

    # 4. Conversione delle decine (usando X, L, C)
    if decine == 1:
        romano = romano + "X"
    elif decine == 2:
        romano = romano + "XX"
    elif decine == 3:
        romano = romano + "XXX"
    elif decine == 4:
        romano = romano + "XL"
    elif decine == 5:
        romano = romano + "L"
    elif decine == 6:
        romano = romano + "LX"
    elif decine == 7:
        romano = romano + "LXX"
    elif decine == 8:
        romano = romano + "LXXX"
    elif decine == 9:
        romano = romano + "XC"

    # 5. Conversione delle unità (usando I, V, X)
    if unita == 1:
        romano = romano + "I"
    elif unita == 2:
        romano = romano + "II"
    elif unita == 3:
        romano = romano + "III"
    elif unita == 4:
        romano = romano + "IV"
    elif unita == 5:
        romano = romano + "V"
    elif unita == 6:
        romano = romano + "VI"
    elif unita == 7:
        romano = romano + "VII"
    elif unita == 8:
        romano = romano + "VIII"
    elif unita == 9:
        romano = romano + "IX"

    print("Numero romano:", romano)