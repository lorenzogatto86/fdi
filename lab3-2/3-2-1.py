# 05-newPassword.py

def rule1(pwd):
    """Deve contenere almeno 8 caratteri."""
    return len(pwd) >= 8


def rule2(pwd):
    """Deve contenere almeno una lettera maiuscola dell'alfabeto inglese."""
    for ch in pwd:
        if "A" <= ch <= "Z":
            return True
    return False


def rule3(pwd):
    """Deve contenere almeno una lettera minuscola dell'alfabeto inglese."""
    for ch in pwd:
        if "a" <= ch <= "z":
            return True
    return False


def rule4(pwd):
    """Deve contenere almeno una cifra numerica."""
    for ch in pwd:
        if "0" <= ch <= "9":
            return True
    return False


def rule5(pwd):
    """Deve contenere almeno un carattere che non sia né lettera né cifra."""
    for ch in pwd:
        is_letter = ("A" <= ch <= "Z") or ("a" <= ch <= "z")
        is_digit = "0" <= ch <= "9"
        if not is_letter and not is_digit:
            return True
    return False


def rule6(pwd):
    """Non deve contenere spazi."""
    return " " not in pwd


def rule7(pwd):
    """Non deve contenere caratteri ripetuti."""
    for i in range(len(pwd)):
        for j in range(i + 1, len(pwd)):
            if pwd[i] == pwd[j]:
                return False
    return True


def isValid(pwd):
    """
    Verifica tutte le regole nell'ordine stabilito, stampa i messaggi
    per ogni regola violata e restituisce True se e solo se sono tutte rispettate.
    """
    valid = True

    if not rule1(pwd):
        print("La password non contiene almeno 8 caratteri")
        valid = False
    if not rule2(pwd):
        print("La password non ha almeno una lettera maiuscola")
        valid = False
    if not rule3(pwd):
        print("La password non ha almeno una lettera minuscola")
        valid = False
    if not rule4(pwd):
        print("La password non ha almeno una cifra numerica")
        valid = False
    if not rule5(pwd):
        print("La password non ha almeno un carattere che non sia una lettera né una cifra")
        valid = False
    if not rule6(pwd):
        print("La password contiene almeno uno spazio")
        valid = False
    if not rule7(pwd):
        print("La password contiene almeno un carattere ripetuto")
        valid = False

    return valid


def main():
    password = input("Inserire una nuova password: ")
    while not isValid(password):
        password = input("Inserire una nuova password: ")
    print("Password OK")


main()