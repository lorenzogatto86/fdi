# 02-isLeapYear.py

anno = int(input("Inserisci un anno (intero positivo): "))

if anno <= 0:
    print("Errore: l'anno deve essere un numero intero positivo.")
else:
    if anno < 1582:
        # Calendario Giuliano: basta la divisibilità per 4
        bisestile = (anno % 4 == 0)
    else:
        # Calendario Gregoriano: attenzione all'ordine dal più specifico al più generale!
        if anno % 400 == 0:
            bisestile = True
        elif anno % 100 == 0:
            bisestile = False
        elif anno % 4 == 0:
            bisestile = True
        else:
            bisestile = False

    if bisestile:
        print("L'anno", anno, "è bisestile.")
    else:
        print("L'anno", anno, "NON è bisestile.")