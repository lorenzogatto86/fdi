
#chieda all'utente di fornire un numero intero positivo avente al massimo cinque cifre
n = int(input("Inserisci un numero intero positivo: "))

# Estrazione della cifra delle decine di migliaia
c1 = n // 10000
n = n % 10000

# Estrazione della cifra delle migliaia
c2 = n // 1000
n = n % 1000

# Estrazione della cifra delle centinaia
c3 = n // 100
n = n % 100

# Estrazione della cifra delle decine e delle unità
c4 = n // 10
c5 = n % 10

print("Le cifre sono:")
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)


#alternativa
c5 = n % 10
n = n // 10

c4 = n % 10
n = n // 10

c3 = n % 10
n = n // 10

c2 = n % 10
n = n // 10

c1 = n % 10

print("Le cifre sono:")
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)