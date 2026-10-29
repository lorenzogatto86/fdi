s1 = input("Inserisci la prima stringa: ")
s2 = input("Inserisci la seconda stringa: ")
s3 = input("Inserisci la terza stringa: ")

if s1 <= s2:
    # Qui sappiamo già che s1 <= s2 (1° confronto effettuato)
    if s2 <= s3:
        # 2° confronto: s1 <= s2 <= s3
        min = s1
        mid = s2
        max = s3
    else:
        # 2° confronto fallito: s3 < s2, quindi s2 è sicuramente il massimo!
        max = s2
        if s1 <= s3:
            # 3° confronto: s1 <= s3 < s2
            min = s1
            mid = s3
        else:
            # 3° confronto: s3 < s1 <= s2
            min = s3
            mid = s1
else:
    # Qui sappiamo già che s2 < s1 (1° confronto effettuato)
    if s1 <= s3:
        # 2° confronto: s2 < s1 <= s3
        min = s2
        mid = s1
        max = s3
    else:
        # 2° confronto fallito: s3 < s1, quindi s1 è sicuramente il massimo!
        max = s1
        if s2 <= s3:
            # 3° confronto: s2 <= s3 < s1
            min = s2
            mid = s3
        else:
            # 3° confronto: s3 < s2 < s1
            min = s3
            mid = s2

print("Le stringhe in ordine crescente sono:")
print(min)
print(mid)
print(max)