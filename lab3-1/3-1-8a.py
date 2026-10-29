testo = input("Inserisci il testo in chiaro: ").upper()
password = input("Inserisci la password: ").upper()

cifrato = ""
i = 0

while i < len(testo):
    c = testo[i]
    if "A" <= c <= "Z":
        # Carattere corrispondente della password usato ciclicamente
        p = password[i % len(password)]
        chiave = ord(p) - ord("A")  # Usa + 1 se si vuole A=1..Z=26 (output CQWU)
        
        pos = ord(c) - ord("A")
        nuova_pos = (pos + chiave) % 26
        cifrato = cifrato + chr(ord("A") + nuova_pos)
    else:
        cifrato = cifrato + c
    i = i + 1

print("Testo cifrato:", cifrato)