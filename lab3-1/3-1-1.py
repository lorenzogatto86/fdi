dna = input("Inserisci una sequenza di DNA (A, C, G, T): ")

valida = True
inv_comp = ""
i = 0

while i < len(dna) and valida:
    carattere = dna[i]
    if carattere == "A":
        inv_comp = "T" + inv_comp
    elif carattere == "T":
        inv_comp = "A" + inv_comp
    elif carattere == "C":
        inv_comp = "G" + inv_comp
    elif carattere == "G":
        inv_comp = "C" + inv_comp
    else:
        valida = False
    i = i + 1

if valida:
    print(inv_comp)
else:
    print("Errore: la stringa contiene caratteri non validi.")