testo = input("Inserisci il testo da cifrare: ").upper()
chiave = int(input("Inserisci la chiave (>= 0): "))

cifrato = ""
i = 0

while i < len(testo):
    c = testo[i]
    if "A" <= c <= "Z":
        # Posizione nell'alfabeto tra 0 e 25
        pos = ord(c) - ord("A")
        # Spostamento ciclico tramite operatore modulo
        nuova_pos = (pos + chiave) % 26
        cifrato = cifrato + chr(ord("A") + nuova_pos)
    else:
        # I caratteri non alfabetici (spazi, punteggiatura) restano invariati
        cifrato = cifrato + c
    i = i + 1

print("Testo cifrato:", cifrato)