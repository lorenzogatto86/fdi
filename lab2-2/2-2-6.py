# 04-tictactoe.py

def crea_scacchiera():
    scacchiera = []
    for r in range(3):
        scacchiera.append([".", ".", "."])
    return scacchiera

def stampa_scacchiera(scacchiera):
    print("Situazione")
    print()
    for r in range(3):
        for c in range(3):
            print(scacchiera[r][c], end="")
        print()
    print()

def leggi_coordinata(prompt):
    # Accetta solo le stringhe "0", "1" o "2", evitando crash su input come "pippo" o "3xx"
    val = input(prompt)
    while val != "0" and val != "1" and val != "2":
        val = input(prompt)
    return int(val)

def verifica_vittoria(scacchiera, s):
    # Controllo le 3 righe e le 3 colonne
    for i in range(3):
        if scacchiera[i][0] == s and scacchiera[i][1] == s and scacchiera[i][2] == s:
            return True
        if scacchiera[0][i] == s and scacchiera[1][i] == s and scacchiera[2][i] == s:
            return True
    # Controllo le 2 diagonali
    if scacchiera[0][0] == s and scacchiera[1][1] == s and scacchiera[2][2] == s:
        return True
    if scacchiera[0][2] == s and scacchiera[1][1] == s and scacchiera[2][0] == s:
        return True
    return False

def scacchiera_piena(scacchiera):
    for r in range(3):
        for c in range(3):
            if scacchiera[r][c] == ".":
                return False
    return True

# --- Programma Principale ---
ancora = "SI"

while ancora == "SI":
    griglia = crea_scacchiera()
    stampa_scacchiera(griglia)
    
    giocatore = "X"
    partita_finita = False
    
    while not partita_finita:
        print("Inserire la mossa del giocatore", giocatore)
        r = leggi_coordinata("Riga (0, 1, 2, dall'alto): ")
        c = leggi_coordinata("Colonna (0, 1, 2, da sinistra): ")
        
        if griglia[r][c] != ".":
            print("Mossa errata")
            stampa_scacchiera(griglia)
        else:
            griglia[r][c] = giocatore
            stampa_scacchiera(griglia)
            
            if verifica_vittoria(griglia, giocatore):
                print("Vittoria del giocatore", giocatore)
                partita_finita = True
            elif scacchiera_piena(griglia):
                print("Parità")
                partita_finita = True
            else:
                # Cambio turno solo se la mossa era valida e la partita continua
                if giocatore == "X":
                    giocatore = "O"
                else:
                    giocatore = "X"
                    
    ancora = input("Un'altra partita? (SI o NO) ")
    while ancora != "SI" and ancora != "NO":
        ancora = input("Un'altra partita? (SI o NO) ")