def caesarDecipher(text, key):
    risultato = ""
    for char in text:
        if "a" <= char <= "z":
            risultato += chr(ord("a") + (ord(char) - ord("a") - key) % 26)
        elif "A" <= char <= "Z":
            risultato += chr(ord("A") + (ord(char) - ord("A") - key) % 26)
        else:
            risultato += char
    return risultato


def trova_lettera_piu_frequente(testo):
    conteggi = [0] * 26
    for char in testo.lower():
        if "a" <= char <= "z":
            conteggi[ord(char) - ord("a")] += 1

    # Trova l'indice del valore massimo
    max_occ = -1
    idx_max = 0
    for i in range(26):
        if conteggi[i] > max_occ:
            max_occ = conteggi[i]
            idx_max = i
    return chr(ord("a") + idx_max)


def valuta_finali_vocali(testo_decifrato):
    """Conta quante parole finiscono con una vocale (a, e, i, o, u)."""
    parole = testo_decifrato.lower().split()
    if len(parole) == 0:
        return 0.0

    vocali = "aeiou"
    conteggio_vocali = 0
    for parola in parole:
        # Rimuove eventuale punteggiatura attaccata a fine parola
        par_pulita = parola.strip(".,;:!?\"'()[]{}")
        if len(par_pulita) > 0 and par_pulita[-1] in vocali:
            conteggio_vocali += 1

    return (conteggio_vocali / len(parole)) * 100


# --- Programma Principale ---
nome_file = input("Inserisci il file cifrato da forzare: ")
f = open(nome_file, "r", encoding="utf-8")
testo_cifrato = f.read()
f.close()

# Metodo 1: La lettera più frequente nel testo cifrato corrisponde probabilmente a 'e', 'a' o 'i'
lettera_max = trova_lettera_piu_frequente(testo_cifrato)
print(f"Lettera cifrata più frequente: '{lettera_max}'")

miglior_chiave = 0
miglior_punteggio = -1.0

print("\n--- Test delle chiavi candidate (combinando Metodo 1 e Metodo 2) ---")
for vocale_ipotesi in ["e", "a", "i"]:
    # Calcola la chiave ipotizzando che 'lettera_max' sia la versione cifrata di 'vocale_ipotesi'
    chiave_ipotesi = (ord(lettera_max) - ord(vocale_ipotesi)) % 26
    tentativo = caesarDecipher(testo_cifrato, chiave_ipotesi)

    # Metodo 2: Verifica quante parole finiscono per vocale nel testo decifrato
    perc_vocali_fine = valuta_finali_vocali(tentativo)
    print(
        f"Ipotesi '{lettera_max}' -> '{vocale_ipotesi}' (Chiave = {chiave_ipotesi}): "
        f"{perc_vocali_fine:.1f}% di parole termina per vocale"
    )

    if perc_vocali_fine > miglior_punteggio:
        miglior_punteggio = perc_vocali_fine
        miglior_chiave = chiave_ipotesi

print(f"\nChiave individuata più probabile: {miglior_chiave}")
print("Anteprima del testo decifrato (primi 300 caratteri):")
print(caesarDecipher(testo_cifrato, miglior_chiave)[:300])