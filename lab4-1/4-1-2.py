def caesarCipher(text, key):
    risultato = ""
    for char in text:
        # Cifra le lettere minuscole dell'alfabeto inglese
        if "a" <= char <= "z":
            pos = ord(char) - ord("a")
            nuova_pos = (pos + key) % 26
            risultato += chr(ord("a") + nuova_pos)
        # Cifra le lettere maiuscole dell'alfabeto inglese
        elif "A" <= char <= "Z":
            pos = ord(char) - ord("A")
            nuova_pos = (pos + key) % 26
            risultato += chr(ord("A") + nuova_pos)
        # Lascia inalterati spazi, punteggiatura, a capo, ecc.
        else:
            risultato += char
    return risultato


def caesarDecipher(text, key):
    # Decifrare con chiave 'key' equivale a cifrare con chiave '-key'
    return caesarCipher(text, -key)


# --- Programma Principale ---
operazione = input("Vuoi eseguire una cifratura (c) o una decifratura (d)? ")
chiave = int(input("Inserisci la chiave (numero intero): "))
file_in = input("Inserisci il percorso/nome del file di input: ")
file_out = input("Inserisci il percorso/nome del file di output: ")

if operazione == "c" or operazione == "d":
    # Lettura dal file sorgente
    f_in = open(file_in, "r", encoding="utf-8")
    testo = f_in.read()
    f_in.close()

    # Elaborazione tramite le funzioni
    if operazione == "c":
        testo_elaborato = caesarCipher(testo, chiave)
    else:
        testo_elaborato = caesarDecipher(testo, chiave)

    # Scrittura sul file di destinazione
    f_out = open(file_out, "w", encoding="utf-8")
    f_out.write(testo_elaborato)
    f_out.close()