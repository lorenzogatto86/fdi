s1 = input("Inserisci la prima stringa (s1): ")
s2 = input("Inserisci la seconda stringa (s2): ")

i = 0  # Indice per scorrere s1
j = 0  # Indice per scorrere s2 (conta quanti caratteri di s2 abbiamo già trovato)

while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
        j = j + 1
    i = i + 1

if j == len(s2):
    print("s2 è una sottosequenza di s1.")
else:
    print("s2 NON è una sottosequenza di s1.")