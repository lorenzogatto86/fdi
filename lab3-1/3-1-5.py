s1 = input("Inserisci la prima stringa (s1): ")
s2 = input("Inserisci la seconda stringa (s2): ")

trovata = False
i = 0

# j non è indipendente: se la fetta deve essere uguale a s2,
# la sua lunghezza deve essere len(s2), quindi j = i + len(s2)
while i <= len(s1) - len(s2) and not trovata:
    j = i + len(s2)
    if s1[i:j] == s2:
        trovata = True
    else:
        i = i + 1

if trovata:
    print("s2 è una sottostringa di s1 (trovata all'indice", i, ").")
else:
    print("s2 NON è una sottostringa di s1.")