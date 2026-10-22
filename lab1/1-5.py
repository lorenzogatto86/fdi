# Calcolo di Fib(6) usando variabili distinte per ogni elemento della sequenza
# L'unico numero esplicito utilizzato nel codice è 1

fib1 = 1
fib2 = 1
fib3 = fib2 + fib1
fib4 = fib3 + fib2
fib5 = fib4 + fib3
fib6 = fib5 + fib4

print(fib6)

# Calcolo di Fib(6) riutilizzando le variabili per gli ultimi due valori calcolati
# L'unico numero esplicito utilizzato nel codice è 1

precedente = 1
corrente = 1

# Calcolo Fib(3)
successivo = corrente + precedente

# Calcolo Fib(4)
precedente = corrente
corrente = successivo
successivo = corrente + precedente

# Calcolo Fib(5)
precedente = corrente
corrente = successivo
successivo = corrente + precedente

# Calcolo Fib(6)
precedente = corrente
corrente = successivo
successivo = corrente + precedente

print(successivo)