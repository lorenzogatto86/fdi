# Aprire l'interprete Python e definire queste variabili
a = 25
b = 25.0
c = -7
d = 3.14
e = "Hello there"
f = "General Kenobi"
g = True
h = False

# ==============================================================
# ESERCIZIO 1: Tipo di ogni variabile e conversioni
# ==============================================================

variabili = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h}

for nome, val in variabili.items():
    print(f"\n--- Variabile {nome} = {repr(val)} ---")
    print(f"  type()  -> {type(val)}")

    # Conversione a int
    try:
        print(f"  int()   -> {int(val)}")
    except (ValueError, TypeError) as err:
        print(f"  int()   -> ERRORE: {err}")

    # Conversione a float
    try:
        print(f"  float() -> {float(val)}")
    except (ValueError, TypeError) as err:
        print(f"  float() -> ERRORE: {err}")

    # Conversione a str
    try:
        print(f"  str()   -> {str(val)}")
    except (ValueError, TypeError) as err:
        print(f"  str()   -> ERRORE: {err}")

    # Conversione a bool
    try:
        print(f"  bool()  -> {bool(val)}")
    except (ValueError, TypeError) as err:
        print(f"  bool()  -> ERRORE: {err}")

# ==============================================================
# ESERCIZIO 2: Operatori aritmetici su coppie di variabili numeriche
# ==============================================================

coppie = [("a", a), ("b", b), ("c", c), ("d", d)]
operatori = [
    ("+",  lambda x, y: x + y),
    ("-",  lambda x, y: x - y),
    ("*",  lambda x, y: x * y),
    ("/",  lambda x, y: x / y),
    ("//", lambda x, y: x // y),
    ("%",  lambda x, y: x % y),
    ("**", lambda x, y: x ** y),
]

print("\n\n==============================================================")
print("ESERCIZIO 2: Operatori aritmetici tra coppie di variabili")
print("==============================================================")

for i in range(len(coppie)):
    for j in range(len(coppie)):
        if i == j:
            continue
        n1, v1 = coppie[i]
        n2, v2 = coppie[j]
        print(f"\n  [{n1}={v1}] op [{n2}={v2}]")
        for simbolo, op in operatori:
            try:
                risultato = op(v1, v2)
                print(f"    {v1} {simbolo} {v2} = {risultato}  (type: {type(risultato).__name__})")
            except Exception as err:
                print(f"    {v1} {simbolo} {v2} -> ERRORE: {err}")

# ==============================================================
# ESERCIZIO 3: Sperimentare operatori con diversi tipi di dato
# ==============================================================

print("\n\n==============================================================")
print("ESERCIZIO 3: Operatori su stringhe e tipi misti")
print("==============================================================")

# Somma di due stringhe (concatenazione)
print(f'\n"Hello there" + "General Kenobi" = {e + f}')
print(f'  type -> {type(e + f).__name__}')

# Moltiplicazione stringa per intero (ripetizione)
print(f'\n"Hello there" * 3 = {e * 3}')
print(f'  type -> {type(e * 3).__name__}')

# Moltiplicazione stringa per float (non permessa)
print(f'\n"Hello there" * 3.14 -> ', end="")
try:
    risultato = e * d
    print(risultato)
except TypeError as err:
    print(f"ERRORE: {err}")

# Sottrazione tra stringhe (non permessa)
print(f'\n"Hello there" - "General Kenobi" -> ', end="")
try:
    risultato = e - f
    print(risultato)
except TypeError as err:
    print(f"ERRORE: {err}")

# Divisione tra stringhe (non permessa)
print(f'\n"Hello there" / "General Kenobi" -> ', end="")
try:
    risultato = e / f
    print(risultato)
except TypeError as err:
    print(f"ERRORE: {err}")

# Somma stringa + intero (non permessa)
print(f'\n"Hello there" + 25 -> ', end="")
try:
    risultato = e + a
    print(risultato)
except TypeError as err:
    print(f"ERRORE: {err}")

# bool si comporta come int negli operatori aritmetici
print(f"\nTrue + True  = {True + True}  (type: {type(True + True).__name__})")
print(f"True * 5     = {True * 5}  (type: {type(True * 5).__name__})")
print(f"False + 10   = {False + 10}  (type: {type(False + 10).__name__})")
