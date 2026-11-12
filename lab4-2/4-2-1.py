def sommaRicorsiva(n):
    # Caso base: la somma del primo numero intero positivo (1) è 1
    if n == 1:
        return 1
    # Passo ricorsivo: n + somma dei primi (n - 1) numeri
    else:
        return n + sommaRicorsiva(n - 1)


# --- Programma Principale ---
n = int(input("Inserisci un numero intero positivo n: "))

if n <= 0:
    print("Errore: il valore inserito deve essere un intero positivo (> 0).")
else:
    risultato = sommaRicorsiva(n)
    print(f"La somma dei primi {n} numeri interi è: {risultato}")