# Calcolo della data della domenica di Pasqua (Algoritmo di Gauss)

# 1. Chiedi all'utente l'anno (intero non negativo)
y = int(input("Inserisci l'anno: "))

# 2. Dividi y per 19, ottenendo il resto a. Ignora il quoziente.
a = y % 19

# 3. Dividi y per 100, ottenendo quoziente b e resto c.
b = y // 100
c = y % 100

# 4. Dividi b per 4, ottenendo quoziente d e resto e.
d = b // 4
e = b % 4

# 5. Dividi (8b+13) per 25, ottenendo il quoziente g. Ignora il resto.
g = (8 * b + 13) // 25

# 6. Dividi (19a+b-d-g+15) per 30, ottenendo il resto h. Ignora il quoziente.
h = (19 * a + b - d - g + 15) % 30

# 7. Dividi c per 4, ottenendo quoziente j e resto k.
j = c // 4
k = c % 4

# 8. Dividi (a+11h) per 319, ottenendo il quoziente m. Ignora il resto.
m = (a + 11 * h) // 319

# 9. Dividi (2e+2j-k-h+m+32) per 7, ottenendo il resto r. Ignora il quoziente.
r = (2 * e + 2 * j - k - h + m + 32) % 7

# 10. Dividi (h-m+r+90) per 25, ottenendo il quoziente n. Ignora il resto.
n = (h - m + r + 90) // 25

# 11. Dividi (h-m+r+n+19) per 32, ottenendo il resto p. Ignora il quoziente.
p = (h - m + r + n + 19) % 32

# Visualizzazione del risultato nel formato: giorno / mese / anno
# Nota: print() inserisce automaticamente uno spazio tra gli argomenti separati da virgola
print(p, "/", n, "/", y)