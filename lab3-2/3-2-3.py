# 05-nim2.py
import random


def randomBoolean():
    """Genera e restituisce un valore booleano casuale con probabilità uniforme."""
    return random.randint(0, 1) == 0


def askUserBalls(numBalls):
    """
    Comunica al giocatore il numero di biglie presenti, chiede quante prenderne
    finché la quantità non rispetta le regole (tra 1 e metà del mucchio) e la restituisce.
    """
    max_take = numBalls // 2
    if max_take < 1:
        max_take = 1

    print(f"Ci sono {numBalls} biglie nel mucchio.")
    taken = int(input(f"Quante biglie vuoi prendere (da 1 a {max_take})? "))
    while taken < 1 or taken > max_take:
        print(f"Mossa non valida! Devi prendere tra 1 e {max_take} biglie.")
        taken = int(input(f"Quante biglie vuoi prendere (da 1 a {max_take})? "))

    return taken


def takeComputerBalls(computerPlayerIsExpert, numBalls):
    """
    Calcola e restituisce il numero di biglie prese dal computer senza stampare nulla.
    """
    max_take = numBalls // 2
    if max_take < 1:
        return 1

    if not computerPlayerIsExpert:
        return random.randint(1, max_take)

    # Strategia esperta: lasciare una quantità pari a (2^k - 1), cioè 63, 31, 15, 7, 3
    target = 63
    while target > numBalls:
        target = target // 2

    # Se numBalls è già una potenza di 2 meno 1 (es. 63, 31, 15, 7, 3),
    # qualsiasi mossa lasci almeno metà mucchio non può raggiungere il target inferiore:
    # in questo caso il computer muove a caso.
    if target == numBalls:
        return random.randint(1, max_take)
    else:
        return numBalls - target


def playAgain():
    """Restituisce True se e solo se l'utente vuole fare un'altra partita."""
    ans = input("Vuoi giocare un'altra partita (s/n)? ").strip().lower()
    while ans != "s" and ans != "n":
        ans = input("Risposta non valida. Vuoi giocare un'altra partita (s/n)? ").strip().lower()
    return ans == "s"


def main():
    playing = True
    while playing:
        numBalls = random.randint(10, 100)
        humanTurn = randomBoolean()
        computerPlayerIsExpert = randomBoolean()

        print("\n--- NUOVA PARTITA A NIM ---")
        if computerPlayerIsExpert:
            print("Il computer gioca in modalità ESPERTO.")
        else:
            print("Il computer gioca in modalità PRINCIPIANTE.")

        while numBalls > 1:
            if humanTurn:
                taken = askUserBalls(numBalls)
            else:
                taken = takeComputerBalls(computerPlayerIsExpert, numBalls)
                print(f"Ci sono {numBalls} biglie. Il computer prende {taken} biglie.")

            numBalls -= taken
            humanTurn = not humanTurn

        # Chi si trova con 1 sola biglia rimasta è costretto a prenderla e perde
        if humanTurn:
            print("Rimane 1 sola biglia. Sei costretto a prenderla: hai perso!")
        else:
            print("Rimane 1 sola biglia. Il computer è costretto a prenderla: hai vinto!")

        playing = playAgain()


main()