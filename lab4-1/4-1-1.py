import os

# 1. Acquisizione dei nomi dei file dall'utente
file1_name = input("Inserisci il nome del primo file: ")
file2_name = input("Inserisci il nome del secondo file: ")

# 2. Verifica dell'esistenza dei file sul disco
if not os.path.isfile(file1_name):
    print("File assente:", file1_name)
elif not os.path.isfile(file2_name):
    print("File assente:", file2_name)
else:
    # 3. Apertura e lettura del contenuto dei due file
    f1 = open(file1_name, "r", encoding="utf-8")
    contenuto1 = f1.read()
    f1.close()

    f2 = open(file2_name, "r", encoding="utf-8")
    contenuto2 = f2.read()
    f2.close()

    # 4. Confronto dei contenuti
    if contenuto1 == contenuto2:
        print("I file sono uguali")
    else:
        print("I file sono diversi")