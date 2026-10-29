# myinput.py

def _allDigits(s):
    """Funzione ausiliaria: True se tutti i caratteri di s sono cifre decimali (0-9)."""
    for ch in s:
        if not ("0" <= ch <= "9"):
            return False
    return True


def isDecimalInteger(s):
    """
    Restituisce True se e solo se s contiene un intero decimale:
    spazi iniziali opzionali, segno +/- opzionale, una o più cifre (0-9), spazi finali opzionali.
    """
    s = s.strip()
    if len(s) == 0:
        return False

    if s[0] == "+" or s[0] == "-":
        s = s[1:]

    return len(s) >= 1 and _allDigits(s)


def isFloating(s):
    """
    Restituisce True se e solo se s contiene un numero in virgola mobile valido.
    """
    s = s.strip()
    if len(s) == 0:
        return False

    # 1. Gestione dell'eventuale esponente ('e' oppure 'E')
    s_lower = s.lower()
    if "e" in s_lower:
        e_index = s_lower.find("e")
        mantissa = s[:e_index]
        exponent = s[e_index + 1:]

        # L'esponente non può avere spazi, può avere un segno e deve avere almeno una cifra
        if len(exponent) == 0:
            return False
        if exponent[0] == "+" or exponent[0] == "-":
            exponent = exponent[1:]
        if len(exponent) == 0 or not _allDigits(exponent):
            return False
    else:
        mantissa = s

    # 2. Gestione della mantissa (segno opzionale, cifre e al più un punto decimale)
    if len(mantissa) == 0:
        return False
    if mantissa[0] == "+" or mantissa[0] == "-":
        mantissa = mantissa[1:]

    if "." in mantissa:
        dot_index = mantissa.find(".")
        before_dot = mantissa[:dot_index]
        after_dot = mantissa[dot_index + 1:]
        # Non devono esserci altri punti e ci deve essere almeno una cifra in totale
        if "." in after_dot:
            return False
        if len(before_dot) + len(after_dot) == 0:
            return False
        return _allDigits(before_dot) and _allDigits(after_dot)
    else:
        return len(mantissa) >= 1 and _allDigits(mantissa)


def inputYesNo(message, yes, no):
    """
    Restituisce True se l'utente digita 'yes', False se digita 'no' (case-insensitive).
    """
    yes_low = yes.lower()
    no_low = no.lower()
    ans = input(message).lower()
    while ans != yes_low and ans != no_low:
        ans = input(message).lower()
    return ans == yes_low


def inputStringStartingWith(message, startingString):
    """Restituisce una stringa digitata dall'utente che inizia con startingString."""
    s = input(message)
    while not s.startswith(startingString):
        s = input(message)
    return s


def inputStringEndingWith(message, endingString):
    """Restituisce una stringa digitata dall'utente che termina con endingString."""
    s = input(message)
    while not s.endswith(endingString):
        s = input(message)
    return s


def inputStringContaining(message, substring):
    """Restituisce una stringa digitata dall'utente che contiene substring."""
    s = input(message)
    while substring not in s:
        s = input(message)
    return s


def inputDecimalInteger(message):
    """Restituisce un numero intero decimale digitato dall'utente."""
    s = input(message)
    while not isDecimalInteger(s):
        s = input(message)
    return int(s)


def inputPositiveDecimalInteger(message):
    """Restituisce un numero intero positivo (> 0) digitato dall'utente."""
    n = inputDecimalInteger(message)
    while n <= 0:
        n = inputDecimalInteger(message)
    return n


def inputNegativeDecimalInteger(message):
    """Restituisce un numero intero negativo (< 0) digitato dall'utente."""
    n = inputDecimalInteger(message)
    while n >= 0:
        n = inputDecimalInteger(message)
    return n


def inputNonPositiveDecimalInteger(message):
    """Restituisce un numero intero non positivo (<= 0) digitato dall'utente."""
    n = inputDecimalInteger(message)
    while n > 0:
        n = inputDecimalInteger(message)
    return n


def inputNonNegativeDecimalInteger(message):
    """Restituisce un numero intero non negativo (>= 0) digitato dall'utente."""
    n = inputDecimalInteger(message)
    while n < 0:
        n = inputDecimalInteger(message)
    return n


def inputFloating(message):
    """Restituisce un numero in virgola mobile digitato dall'utente."""
    s = input(message)
    while not isFloating(s):
        s = input(message)
    return float(s)


# Sezione di collaudo ad esecuzione condizionata
if __name__ == "__main__":
    print("=== COLLAUDO AUTOMATICO DI isDecimalInteger e isFloating ===")
    print("Test isDecimalInteger('  -42 '):", isDecimalInteger("  -42 "), "(atteso: True)")
    print("Test isDecimalInteger('+ 23'):", isDecimalInteger("+ 23"), "(atteso: False)")
    print("Test isFloating(' -3.14e-2 '):", isFloating(" -3.14e-2 "), "(atteso: True)")
    print("Test isFloating(' .5 '):", isFloating(" .5 "), "(atteso: True)")
    print("Test isFloating(' . '):", isFloating(" . "), "(atteso: False)")
    print("Test isFloating(' 12e '):", isFloating(" 12e "), "(atteso: False)")

    print("\n=== COLLAUDO INTERATTIVO DELLE FUNZIONI DI INPUT ===")

    print("\n1) Collaudo della funzione inputDecimalInteger")
    print('Scrivi, nell\'ordine, le seguenti stringhe, senza le virgolette ma con attenzione agli spazi,')
    print('in risposta alle richieste del programma: "+ 23", "- 34", "x", "12x", "12".')
    print("Soltanto l'ultima stringa deve essere accettata e visualizzata dal programma.")
    val = inputDecimalInteger("Numero: ")
    print("OK", val)

    print("\n2) Collaudo della funzione inputPositiveDecimalInteger")
    print('Scrivi nell\'ordine: "0", "-5", "abc", "7". Solo "7" deve essere accettato.')
    val = inputPositiveDecimalInteger("Numero positivo: ")
    print("OK", val)

    print("\n3) Collaudo della funzione inputNegativeDecimalInteger")
    print('Scrivi nell\'ordine: "0", "4", "-3". Solo "-3" deve essere accettato.')
    val = inputNegativeDecimalInteger("Numero negativo: ")
    print("OK", val)

    print("\n4) Collaudo della funzione inputNonPositiveDecimalInteger")
    print('Scrivi nell\'ordine: "5", "0". Solo "0" deve essere accettato.')
    val = inputNonPositiveDecimalInteger("Numero non positivo: ")
    print("OK", val)

    print("\n5) Collaudo della funzione inputNonNegativeDecimalInteger")
    print('Scrivi nell\'ordine: "-2", "0". Solo "0" deve essere accettato.')
    val = inputNonNegativeDecimalInteger("Numero non negativo: ")
    print("OK", val)

    print("\n6) Collaudo della funzione inputFloating")
    print('Scrivi nell\'ordine: ".", "1.2.3", "1e+", "-1.5e2". Solo "-1.5e2" deve essere accettato.')
    val = inputFloating("Numero float: ")
    print("OK", val)

    print("\n7) Collaudo della funzione inputYesNo")
    print('Scrivi nell\'ordine: "forse", "si", "s". Solo "s" deve essere accettato.')
    val = inputYesNo("Vuoi continuare? (S/N) ", "S", "N")
    print("OK", val)

    print("\n8) Collaudo di inputStringStartingWith, inputStringEndingWith, inputStringContaining")
    print('Per StartingWith("py"): scrivi "java", poi "python".')
    val = inputStringStartingWith("Stringa che inizia con 'py': ", "py")
    print("OK", val)

    print('Per EndingWith(".txt"): scrivi "file.doc", poi "dati.txt".')
    val = inputStringEndingWith("Stringa che termina con '.txt': ", ".txt")
    print("OK", val)

    print('Per Containing("@"): scrivi "utente.it", poi "utente@mail.it".')
    val = inputStringContaining("Stringa che contiene '@': ", "@")
    print("OK", val)