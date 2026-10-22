# planetWeight.py

peso_terra = float(input("Inserisci il tuo peso sulla terra (in Kg): "))
pianeta = input("Inserisci il pianeta a cui sei interessato/a: ")

# Uso una variabile per il fattore di gravità
fattore = 0.0
pianeta_valido = True

if pianeta == "Mercurio":
    fattore = 0.38
elif pianeta == "Venere":
    fattore = 0.91
elif pianeta == "Terra":
    fattore = 1.00
elif pianeta == "Marte":
    fattore = 0.38
elif pianeta == "Giove":
    fattore = 2.34
elif pianeta == "Saturno":
    fattore = 1.06
elif pianeta == "Urano":
    fattore = 0.92
elif pianeta == "Nettuno":
    fattore = 1.19
else:
    pianeta_valido = False

if pianeta_valido:
    peso_pianeta = peso_terra * fattore
    # Se sulla terra inseriscono un intero (es. 82), per avere un output identico
    # all'esempio si può usare int() o float() a seconda di come avete impostato il lab
    print("Sulla terra il tuo peso è", peso_terra, "Kg, mentre su", pianeta, "il tuo peso è", peso_pianeta)
else:
    print("Il pianeta inserito non è valido.")