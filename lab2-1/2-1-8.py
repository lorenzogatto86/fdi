# 03-nim.py
import random

print("Programma per giocare a Nim contro il computer")

gioca_ancora = "S"

# 1. Ciclo principale delle partite
while gioca_ancora == "S":
    
    # 2. Inizializzazione dei parametri della nuova partita
    numBalls = random.randint(10, 100)
    computerPlayerIsExpert = (random.randint(0, 1) == 1)
    nextPlayerIsHuman = (random.randint(0, 1) == 1)
    
    print("Inizio della partita")
    
    # 3. Ciclo dei turni della singola partita (continua finché c'è più di 1 biglia)
    while numBalls > 1:
        print("Biglie presenti nel mucchio:", numBalls)
        max_prendibili = numBalls // 2
        
        if nextPlayerIsHuman:
            # Turno del giocatore umano con validazione dell'input
            prese = int(input("Quante ne vuoi prendere? "))
            while prese < 1 or prese > max_prendibili:
                print("Mossa non valida! Devi prenderne tra 1 e", max_prendibili)
                prese = int(input("Quante ne vuoi prendere? "))
                
            numBalls = numBalls - prese
            nextPlayerIsHuman = False  # Passa il turno al computer
            
        else:
            # Turno del computer
            if not computerPlayerIsExpert:
                # Modalità stupida: mossa casuale valida
                prese = random.randint(1, max_prendibili)
            else:
                # Modalità intelligente: lascia 63, 31, 15, 7, 3 o 1 biglie
                if numBalls == 63 or numBalls == 31 or numBalls == 15 or numBalls == 7 or numBalls == 3:
                    # Posizione già "perdente": fa una mossa casuale valida
                    prese = random.randint(1, max_prendibili)
                elif numBalls > 63:
                    prese = numBalls - 63
                elif numBalls > 31:
                    prese = numBalls - 31
                elif numBalls > 15:
                    prese = numBalls - 15
                elif numBalls > 7:
                    prese = numBalls - 7
                elif numBalls > 3:
                    prese = numBalls - 3
                else:
                    # Caso numBalls == 2: lascia 1 biglia
                    prese = numBalls - 1
                    
            print("Il computer ne ha prese:", prese)
            numBalls = numBalls - prese
            nextPlayerIsHuman = True  # Passa il turno all'umano

    # Fine della partita: è rimasta 1 sola biglia, chi ha il turno ora è costretto a prenderla e perde!
    if nextPlayerIsHuman:
        print("Hai perso")
    else:
        print("Hai vinto!")
        
    if computerPlayerIsExpert:
        print("Il computer giocava in modo intelligente")
    else:
        print("Il computer giocava in modo stupido")

    # Richiesta di nuova partita con validazione rigorosa (solo S o N)
    gioca_ancora = input("Vuoi giocare ancora? (S/N) ")
    while gioca_ancora != "S" and gioca_ancora != "N":
        gioca_ancora = input("Vuoi giocare ancora? (S/N) ")