def fibonacciIterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Manteniamo solo gli ultimi due valori calcolati: F(i-2) e F(i-1)
    prec2 = 0  # F(0)
    prec1 = 1  # F(1)
    
    for _ in range(2, n + 1):
        corrente = prec1 + prec2
        prec2 = prec1
        prec1 = corrente
        
    return prec1


# --- Programma Principale ---
n = int(input("Inserisci il valore di n (intero >= 0): "))
print(f"Fibonacci({n}) = {fibonacciIterativo(n)}")