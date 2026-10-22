# 02-printTimeInterval3.py (Approccio per casi espliciti)

t1 = int(input("Inserire il primo orario (es. 0930): "))
t2 = int(input("Inserire il secondo orario: "))

min_tot1 = (t1 // 100) * 60 + (t1 % 100)
min_tot2 = (t2 // 100) * 60 + (t2 % 100)

if min_tot2 >= min_tot1:
    diff = min_tot2 - min_tot1
else:
    diff = (24 * 60 - min_tot1) + min_tot2

ore = diff // 60
minuti = diff % 60

# Gestione formattazione output
if ore == 0:
    if minuti == 0:
        print("Tempo trascorso: 0 minuti")
    elif minuti == 1:
        print("Tempo trascorso: un minuto")
    else:
        print("Tempo trascorso:", minuti, "minuti")
elif ore == 1:
    if minuti == 0:
        print("Tempo trascorso: un'ora")
    elif minuti == 1:
        print("Tempo trascorso: un'ora e un minuto")
    else:
        print("Tempo trascorso: un'ora e", minuti, "minuti")
else:
    if minuti == 0:
        print("Tempo trascorso:", ore, "ore")
    elif minuti == 1:
        print("Tempo trascorso:", ore, "ore e un minuto")
    else:
        print("Tempo trascorso:", ore, "ore e", minuti, "minuti")






'''
# 02-printTimeInterval3.py (Approccio modulare con stringhe)

t1 = int(input("Inserire il primo orario (es. 0930): "))
t2 = int(input("Inserire il secondo orario: "))

min_tot1 = (t1 // 100) * 60 + (t1 % 100)
min_tot2 = (t2 // 100) * 60 + (t2 % 100)

if min_tot2 >= min_tot1:
    diff = min_tot2 - min_tot1
else:
    diff = (24 * 60 - min_tot1) + min_tot2

ore = diff // 60
minuti = diff % 60

# 1. Preparo il testo delle ore
if ore == 0:
    testo_ore = ""
elif ore == 1:
    testo_ore = "un'ora"
else:
    testo_ore = str(ore) + " ore"

# 2. Preparo il testo dei minuti
if minuti == 0:
    testo_minuti = ""
elif minuti == 1:
    testo_minuti = "un minuto"
else:
    testo_minuti = str(minuti) + " minuti"

# 3. Combino i due testi
if ore > 0 and minuti > 0:
    risultato = testo_ore + " e " + testo_minuti
elif ore > 0 and minuti == 0:
    risultato = testo_ore
elif ore == 0 and minuti > 0:
    risultato = testo_minuti
else:
    risultato = "0 minuti"

print("Tempo trascorso:", risultato)'''