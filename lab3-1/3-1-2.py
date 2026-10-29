s = input("Inserisci una stringa: ")

is_palindrome = True
i = 0
j = len(s) - 1

while i < j and is_palindrome:
    if s[i] != s[j]:
        is_palindrome = False
    i = i + 1
    j = j - 1

if is_palindrome:
    messaggio = "La stringa è un palindromo."
else:
    messaggio = "La stringa NON è un palindromo."

print(messaggio)