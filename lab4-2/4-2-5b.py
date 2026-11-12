def fibonacciRicorsivo(n):
    # Casi base: F(0) = 0, F(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Passo ricorsivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacciRicorsivo(n - 1) + fibonacciRicorsivo(n - 2)


# --- Programma Principale ---
n = int(input("Inserisci il valore di n (intero >= 0): "))
print(f"Fibonacci({n}) = {fibonacciRicorsivo(n)}")