# 04-isPerfectMagicSquare.py

valori = []
riga_input = input("Inserisci un numero (oppure STOP per terminare): ")
while riga_input != "STOP":
    valori.append(int(riga_input))
    riga_input = input("Inserisci un numero (oppure STOP per terminare): ")

totale_elementi = len(valori)

# 1. Verifica che la quantità di valori sia un quadrato perfetto (n^2 >= 1)
n = 1
while n * n < totale_elementi:
    n = n + 1

if totale_elementi == 0 or n * n != totale_elementi:
    print("Fallimento: il numero di elementi inseriti non forma una matrice quadrata.")
else:
    # 2. Verifica che contenga tutti e soli i numeri da 1 a n^2
    tutti_presenti = True
    k = 1
    while k <= totale_elementi and tutti_presenti:
        if k not in valori:
            tutti_presenti = False
        k = k + 1

    if not tutti_presenti:
        print("Fallimento: la sequenza non contiene tutti i numeri da 1 a", totale_elementi)
    else:
        # 3. Costruzione e stampa della lista di liste (matrice n x n)
        matrice = []
        indice = 0
        for r in range(n):
            nuova_riga = []
            for c in range(n):
                nuova_riga.append(valori[indice])
                indice = indice + 1
            matrice.append(nuova_riga)

        print("Matrice inserita:")
        for r in range(n):
            for c in range(n):
                print(f"{matrice[r][c]:4d}", end="")
            print()

        # 4. Verifica delle regole del quadrato magico
        # Prendo la somma della prima riga come "costante magica" di riferimento
        costante_magica = 0
        for c in range(n):
            costante_magica = costante_magica + matrice[0][c]

        magico = True

        # Controllo tutte le righe
        r = 0
        while r < n and magico:
            somma_riga = 0
            for c in range(n):
                somma_riga = somma_riga + matrice[r][c]
            if somma_riga != costante_magica:
                magico = False
            r = r + 1

        # Controllo tutte le colonne
        c = 0
        while c < n and magico:
            somma_col = 0
            for r in range(n):
                somma_col = somma_col + matrice[r][c]
            if somma_col != costante_magica:
                magico = False
            c = c + 1

        # Controllo diagonale principale ([i][i]) e secondaria ([i][n - 1 - i])
        if magico:
            somma_diag1 = 0
            somma_diag2 = 0
            for i in range(n):
                somma_diag1 = somma_diag1 + matrice[i][i]
                somma_diag2 = somma_diag2 + matrice[i][n - 1 - i]
            if somma_diag1 != costante_magica or somma_diag2 != costante_magica:
                magico = False

        # 5. Esito finale
        if magico:
            print("Successo! La matrice è un quadrato magico perfetto.")
        else:
            print("Fallimento: le somme di righe, colonne o diagonali non coincidono.")