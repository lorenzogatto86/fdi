nome_file = input("Inserisci il nome del file di testo da elaborare: ")

f = open(nome_file, "r", encoding="utf-8")
testo = f.read().lower()
f.close()

# Lista di 26 contatori, uno per ciascuna lettera da 'a' (indice 0) a 'z' (indice 25)
conteggi = [0] * 26
totale_lettere = 0

for char in testo:
    # Controllo esplicito su 'a'..'z' per ignorare punteggiatura, spazi e lettere accentate
    if "a" <= char <= "z":
        indice = ord(char) - ord("a")
        conteggi[indice] += 1
        totale_lettere += 1

# Stampa della tabella con due cifre decimali
for i in range(26):
    lettera = chr(ord("a") + i)
    if totale_lettere > 0:
        percentuale = (conteggi[i] / totale_lettere) * 100
    else:
        percentuale = 0.0
    print(f"{lettera} {percentuale:.2f}%")