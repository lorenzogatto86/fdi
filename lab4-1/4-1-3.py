def vigenereCipher(text, password):
    risultato = ""
    password = password.lower()
    n_pass = len(password)
    idx_pass = 0

    for char in text:
        # Calcola lo shift (da 0 a 25) dato dal carattere corrente della password
        shift = ord(password[idx_pass % n_pass]) - ord("a")

        if "a" <= char <= "z":
            pos = ord(char) - ord("a")
            risultato += chr(ord("a") + (pos + shift) % 26)
            idx_pass += 1
        elif "A" <= char <= "Z":
            pos = ord(char) - ord("A")
            risultato += chr(ord("A") + (pos + shift) % 26)
            idx_pass += 1
        else:
            risultato += char
            # Nota: se nella versione vista a lezione (04-EncodeVigenere.py) l'indice
            # della password avanza anche sui caratteri non alfabetici, sposta
            # 'idx_pass += 1' fuori dall'if/else.
    return risultato


def vigenereDecipher(text, password):
    risultato = ""
    password = password.lower()
    n_pass = len(password)
    idx_pass = 0

    for char in text:
        shift = ord(password[idx_pass % n_pass]) - ord("a")

        if "a" <= char <= "z":
            pos = ord(char) - ord("a")
            risultato += chr(ord("a") + (pos - shift) % 26)
            idx_pass += 1
        elif "A" <= char <= "Z":
            pos = ord(char) - ord("A")
            risultato += chr(ord("A") + (pos - shift) % 26)
            idx_pass += 1
        else:
            risultato += char
    return risultato


# --- Programma Principale ---
operazione = input("Vuoi eseguire una cifratura (c) o una decifratura (d)? ")
password = input("Inserisci la password di cifratura/decifratura: ")
file_in = input("Inserisci il percorso/nome del file di input: ")
file_out = input("Inserisci il percorso/nome del file di output: ")

if operazione == "c" or operazione == "d":
    f_in = open(file_in, "r", encoding="utf-8")
    testo = f_in.read()
    f_in.close()

    if operazione == "c":
        testo_elaborato = vigenereCipher(testo, password)
    else:
        testo_elaborato = vigenereDecipher(testo, password)

    f_out = open(file_out, "w", encoding="utf-8")
    f_out.write(testo_elaborato)
    f_out.close()