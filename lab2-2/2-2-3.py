# 04-eratostene.py

# Validazione dell'input: richiede un intero positivo (MAX > 0)
MAX = int(input("Inserisci il valore MAX (intero positivo): "))
while MAX <= 0:
    MAX = int(input("Valore non valido. Inserisci un intero positivo MAX: "))

# Predispongo una lista di MAX valori booleani inizializzati a True
crivello = [True] * MAX

# I numeri da considerare partono da 2 (0 e 1 vengono ignorati)
for i in range(2, MAX):
    # Se i non è stato eliminato, allora è primo: elimino tutti i suoi multipli
    if crivello[i]:
        multiplo = i * 2  # Parto dal doppio di i per NON eliminare i stesso!
        while multiplo < MAX:
            crivello[multiplo] = False
            multiplo = multiplo + i

# Stampa dei numeri primi rimasti (indici >= 2 il cui valore è ancora True)
print("Numeri primi minori di", MAX, ":")
for i in range(2, MAX):
    if crivello[i]:
        print(i)