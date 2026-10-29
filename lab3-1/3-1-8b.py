cifrato = input("Inserisci il testo cifrato: ").upper()
password = input("Inserisci la password: ").upper()

decifrato = ""
i = 0

while i < len(cifrato):
    c = cifrato[i]
    if "A" <= c <= "Z":
        p = password[i % len(password)]
        chiave = ord(p) - ord("A")
        
        pos = ord(c) - ord("A")
        nuova_pos = (pos - chiave) % 26
        decifrato = decifrato + chr(ord("A") + nuova_pos)
    else:
        decifrato = decifrato + c
    i = i + 1

print("Testo decifrato:", decifrato)