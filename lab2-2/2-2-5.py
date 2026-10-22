# 04-printPerfectMagicSquare.py

# Lettura "silenziosa" di n (senza prompt per l'utente, come da specifica)
n = int(input())

# Creazione corretta della matrice n x n inizializzata a 0 (0 = casella vuota)
matrice = []
for i in range(n):
    matrice.append([0] * n)

# Posizione iniziale: ultima riga, colonna centrale
riga = n - 1
colonna = n // 2

# Inserimento dei numeri da 1 a n*n
for k in range(1, n * n + 1):
    matrice[riga][colonna] = k
    
    # Salvo i valori attuali prima di spostarmi
    prec_riga = riga
    prec_colonna = colonna
    
    # Incremento riga e colonna con effetto "pacman" (wrap-around sul bordo)
    riga = riga + 1
    colonna = colonna + 1
    if riga == n:
        riga = 0
    if colonna == n:
        colonna = 0
        
    # Se la nuova casella è già occupata (diversa da 0), ripristino e salgo di una riga
    if matrice[riga][colonna] != 0:
        riga = prec_riga
        colonna = prec_colonna
        riga = riga - 1

# Visualizzazione della sola matrice
for r in range(n):
    for c in range(n):
        print(f"{matrice[r][c]:4d}", end="")
    print()