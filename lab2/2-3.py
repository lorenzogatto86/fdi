# 02-oddNumber.py

n = int(input("Scrivi un numero dispari: "))

if n % 2 != 0:
    # Primo tentativo andato a buon fine
    print("Complimenti! Il numero", n, "è dispari!")
else:
    # Primo tentativo fallito: segnalo errore e chiedo di nuovo
    print("Ho detto dispari! Riprova")
    n = int(input("Scrivi un numero dispari: "))
    
    if n % 2 != 0:
        # Secondo tentativo andato a buon fine
        print("Complimenti! Il numero", n, "è dispari!")
    else:
        # Anche il secondo tentativo è fallito
        print("Ripassa il concetto di numero dispari, ti saluto.")