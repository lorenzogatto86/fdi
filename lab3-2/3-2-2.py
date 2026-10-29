# 05-numberName.py

def under100Name(n):
    """Restituisce il nome in italiano di un intero positivo n (1 <= n <= 99)."""
    if n == 1: return "uno"
    if n == 2: return "due"
    if n == 3: return "tre"
    if n == 4: return "quattro"
    if n == 5: return "cinque"
    if n == 6: return "sei"
    if n == 7: return "sette"
    if n == 8: return "otto"
    if n == 9: return "nove"
    if n == 10: return "dieci"
    if n == 11: return "undici"
    if n == 12: return "dodici"
    if n == 13: return "tredici"
    if n == 14: return "quattordici"
    if n == 15: return "quindici"
    if n == 16: return "sedici"
    if n == 17: return "diciassette"
    if n == 18: return "diciotto"
    if n == 19: return "diciannove"

    tens_digit = n // 10
    unit_digit = n % 10

    if tens_digit == 2: tens_str = "venti"
    elif tens_digit == 3: tens_str = "trenta"
    elif tens_digit == 4: tens_str = "quaranta"
    elif tens_digit == 5: tens_str = "cinquanta"
    elif tens_digit == 6: tens_str = "sessanta"
    elif tens_digit == 7: tens_str = "settanta"
    elif tens_digit == 8: tens_str = "ottanta"
    elif tens_digit == 9: tens_str = "novanta"

    if unit_digit == 0:
        return tens_str

    # Elisione della vocale finale della decina davanti a 1 (uno) e 8 (otto)
    if unit_digit == 1 or unit_digit == 8:
        tens_str = tens_str[:-1]

    return tens_str + under100Name(unit_digit)


def under1000Name(n):
    """Restituisce il nome in italiano di un intero positivo n (1 <= n <= 999)."""
    if n < 100:
        return under100Name(n)

    hundreds_digit = n // 100
    remainder = n % 100

    if hundreds_digit == 1:
        hundreds_str = "cento"
    else:
        hundreds_str = under100Name(hundreds_digit) + "cento"

    if remainder == 0:
        return hundreds_str

    # Elisione della 'o' di cento davanti a 'ottanta' (80..89)
    if 80 <= remainder <= 89:
        hundreds_str = hundreds_str[:-1]

    return hundreds_str + under100Name(remainder)


def numberName(n):
    """Restituisce il nome in italiano di un intero positivo n (1 <= n < 1000000)."""
    thousands = n // 1000
    remainder = n % 1000

    if thousands == 0:
        result = under1000Name(remainder)
    else:
        if thousands == 1:
            thousands_str = "mille"
        else:
            thousands_str = under1000Name(thousands) + "mila"

        if remainder == 0:
            result = thousands_str
        else:
            result = thousands_str + under1000Name(remainder)

    # Regola dell'accento: tutti i composti che terminano in "-tre" (n > 3)
    # prendono l'accento acuto finale ("-tré")
    if n > 3 and result.endswith("tre"):
        result = result[:-1] + "é"

    return result


def main():
    n = int(input("Inserire un numero intero positivo minore di un milione: "))
    while n <= 0 or n >= 1000000:
        print("Errore: il numero deve essere compreso tra 1 e 999999.")
        n = int(input("Inserire un numero intero positivo minore di un milione: "))

    print(numberName(n))


main()