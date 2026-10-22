# 02-checkCircles.py

x1 = float(input("Coordinata x del centro della prima circonferenza: "))
y1 = float(input("Coordinata y del centro della prima circonferenza: "))
r1 = float(input("Raggio della prima circonferenza: "))

x2 = float(input("Coordinata x del centro della seconda circonferenza: "))
y2 = float(input("Coordinata y del centro della seconda circonferenza: "))
r2 = float(input("Raggio della seconda circonferenza: "))

# Calcolo distanza tra i centri (usando ** 0.5 senza bisogno di import math)
d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#alternativa sqrt
# import math
# d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
somma_raggi = r1 + r2

# Valore assoluto della differenza dei raggi
if r1 >= r2:
    diff_raggi = r1 - r2
else:
    diff_raggi = r2 - r1
#alternativa
# diff_raggi = abs(r1 - r2)

# Selezione dei 7 casi (attenzione all'ordine!)
if d == 0 and r1 == r2:
    print("Le due circonferenze sono coincidenti")
elif d == 0 and r1 != r2:
    print("Le due circonferenze sono concentriche (ma non coincidenti)")
elif d == somma_raggi:
    print("Le due circonferenze sono tangenti esternamente")
elif d == diff_raggi:
    # Qui siamo già sicuri che d > 0 perché i casi d == 0 sono stati intercettati sopra!
    print("Le due circonferenze sono tangenti internamente")
elif d > somma_raggi:
    print("Le due circonferenze sono (reciprocamente) esterne")
elif d < diff_raggi:
    # Anche qui siamo sicuri che d > 0
    print("Le due circonferenze sono una interna all'altra, ma non concentriche")
else:
    # Rimane solo il caso: diff_raggi < d < somma_raggi
    print("Le due circonferenze sono secanti")