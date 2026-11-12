def euclideMCD(m, n):
    # Caso base: se n è un divisore di m (resto 0), allora n è il M.C.D.
    if m % n == 0:
        return n
    # Passo ricorsivo: M.C.D. tra n e il resto della divisione intera di m per n
    else:
        return euclideMCD(n, m % n)


# --- Programma Principale ---
m = int(input("Inserisci il primo numero intero positivo m: "))
n = int(input("Inserisci il secondo numero intero positivo n (con m > n): "))

if m <= 0 or n <= 0:
    print("Errore: entrambi i numeri devono essere positivi.")
else:
    # Se l'utente inserisce m < n, li scambiamo per rispettare m > n
    if m < n:
        m, n = n, m
    risultato = euclideMCD(m, n)
    print(f"Il M.C.D. tra {m} e {n} è: {risultato}")