def isPalindrome(s):
    # Caso base: una stringa di lunghezza 0 o 1 è sempre palindroma
    if len(s) <= 1:
        return True
    
    # Se il primo e l'ultimo carattere sono diversi, non è palindroma
    if s[0] != s[-1]:
        return False
    
    # Passo ricorsivo: controlla la sottostringa interna (escludendo primo e ultimo carattere)
    return isPalindrome(s[1:-1])


# --- Programma Principale (senza alcun ciclo) ---
stringa_utente = input("Inserisci una stringa per verificare se è palindroma: ")
if isPalindrome(stringa_utente):
    print(f"'{stringa_utente}' è palindroma.")
else:
    print(f"'{stringa_utente}' NON è palindroma.")

# --- Verifica dei casi richiesti dalla traccia (senza cicli) ---
print("\n--- Test casi di verifica ---")
print("'omordotuanuoraoarounautodromo':", isPalindrome("omordotuanuoraoarounautodromo"))
print("Palindroma pari ('anna'):", isPalindrome("anna"))
print("Palindroma dispari ('radar'):", isPalindrome("radar"))
print("Non palindroma pari ('casa'):", isPalindrome("casa"))
print("Non palindroma dispari ('albero'):", isPalindrome("albero"))
print("Lunghezza unitaria ('a'):", isPalindrome("a"))
print("Lunghezza zero (''):", isPalindrome(""))