# numberLister.py

print("***STAMPA DEI NUMERI DA 1 A N***")
n = int(input("N?: "))

if n <= 0:
    print("Input non valido")
else:
    # Versione con while (equivalente a: for i in range(1, n + 1):)
    i = 1
    while i <= n:
        print(i, end=" ")
        i = i + 1
    print()  # Va a capo dopo aver stampato tutti i numeri