# 02-twoNumbers.py

n1 = int(input("Primo numero? "))
n2 = int(input("Secondo numero? "))

somma = n1 + n2
prodotto = n1 * n2
media = somma / 2

# Calcolo di massimo e minimo con la selezione
if n1 >= n2:
    massimo = n1
    minimo = n2
else:
    massimo = n2
    minimo = n1

# Calcolo del valore assoluto della differenza con la selezione
differenza = n1 - n2
if differenza < 0:
    diff_assoluta = -differenza
else:
    diff_assoluta = differenza

# In alternativa, puoi far notare ai ragazzi che diff_assoluta è sempre uguale a (massimo - minimo)!

print("Somma:", somma)
print("Prodotto:", prodotto)
print("Valore medio:", media)
print("Valore massimo:", massimo)
print("Valore minimo:", minimo)
print("Differenza (in valore assoluto):", diff_assoluta)