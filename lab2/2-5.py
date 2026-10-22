# 02-printTimeInterval2.py

t1 = int(input("Inserire il primo orario (es. 0930): "))
t2 = int(input("Inserire il secondo orario: "))

# 1. Estrazione ore e minuti dei due orari
h1 = t1 // 100
m1 = t1 % 100

h2 = t2 // 100
m2 = t2 % 100

# 2. Conversione in minuti totali dalla mezzanotte
min_tot1 = h1 * 60 + m1
min_tot2 = h2 * 60 + m2

# 3. Calcolo della differenza con selezione (gestione mezzanotte)
if min_tot2 >= min_tot1:
    diff = min_tot2 - min_tot1
else:
    diff = (24 * 60 - min_tot1) + min_tot2  # oppure: min_tot2 - min_tot1 + 1440

# 4. Riconversione in ore e minuti
ore = diff // 60
minuti = diff % 60

print("Tempo trascorso:", ore, "ore e", minuti, "minuti")