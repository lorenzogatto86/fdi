s = input("Inserisci una riga di testo: ")

if len(s) == 0:
    risultato = ""
else:
    risultato = s[0]
    i = 1
    while i < len(s):
        if s[i] != s[i - 1]:
            risultato = risultato + s[i]
        i = i + 1

print(risultato)