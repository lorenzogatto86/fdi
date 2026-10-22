# 03-printPrimes.py

# Fase 1: Validazione dell'input
valore_max = int(input("Inserisci il valore massimo, intero maggiore di uno: "))
while valore_max <= 1:
    valore_max = int(input("Inserisci il valore massimo, intero maggiore di uno: "))

print("Numeri primi non maggiori di " + str(valore_max) + ":")

# Fase 2: Ciclo esterno su tutti i candidati i da 2 a valore_max
i = 2
while i <= valore_max:
    
    # Fase 3: Ciclo interno per verificare se i è primo
    primo = True
    j = 2
    while j < i and primo:  # Ancora più veloce: while j * j <= i and primo:
        if i % j == 0:
            primo = False
        j = j + 1
        
    if primo:
        print(i)
        
    i = i + 1