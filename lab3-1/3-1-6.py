s1 = input("Inserisci la prima stringa: ")
s2 = input("Inserisci la seconda stringa: ")

max_sub = ""

i = 0
while i < len(s1):
    # Partiamo da una lunghezza minima pari a len(max_sub) + 1:
    # è inutile testare sottostringhe più corte o uguali a quella già trovata!
    j = i + len(max_sub) + 1
    while j <= len(s1):
        candidata = s1[i:j]
        
        # Verifichiamo se 'candidata' è sottostringa di s2 (logica di 04-isSubstring.py)
        trovata = False
        k = 0
        while k <= len(s2) - len(candidata) and not trovata:
            if s2[k : k + len(candidata)] == candidata:
                trovata = True
            else:
                k = k + 1
        
        if trovata:
            max_sub = candidata
        j = j + 1
    i = i + 1

print("La più lunga sottostringa comune è:", max_sub)