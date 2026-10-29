cifrato = input("Inserisci il testo cifrato: ").upper()
chiave = int(input("Inserisci la chiave usata per cifrare (>= 0): "))

decifrato = ""
i = 0

while i < len(cifrato):
    c = cifrato[i]
    if "A" <= c <= "Z":
        pos = ord(c) - ord("A")
        # Sottraiamo la chiave invece di sommarla
        nuova_pos = (pos - chiave) % 26
        decifrato = decifrato + chr(ord("A") + nuova_pos)
    else:
        decifrato = decifrato + c
    i = i + 1

print("Testo decifrato:", decifrato)