def getAllSubstrings(s):
    """Restituisce tutte le sottostringhe di s (incluse '' e s) per lunghezza crescente."""
    # La stringa vuota è l'unica sottostringa di lunghezza 0
    subs = [""]
    n = len(s)
    # Ciclo esterno sulla lunghezza (da 1 a n) per garantire l'ordine di lunghezza crescente
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            subs.append(s[start : start + length])
    return subs


def numSubstrings(s):
    """Calcola il numero di sottostringhe senza generarle: 1 + n*(n+1)//2."""
    n = len(s)
    return 1 + (n * (n + 1)) // 2


def areUnique(ss):
    """Restituisce True se e solo se gli elementi di ss sono tutti diversi."""
    n = len(ss)
    for i in range(n):
        for j in range(i + 1, n):
            if ss[i] == ss[j]:
                return False
    return True


def isSortedByIncreasingLength(ss):
    """Restituisce True se gli elementi sono in ordine di lunghezza non decrescente."""
    for i in range(len(ss) - 1):
        if len(ss[i]) > len(ss[i + 1]):
            return False
    return True


def isSortedByDecreasingLength(ss):
    """Restituisce True se gli elementi sono in ordine di lunghezza non crescente."""
    for i in range(len(ss) - 1):
        if len(ss[i]) < len(ss[i + 1]):
            return False
    return True


def isForwardSorted(ss):
    """Restituisce True se gli elementi sono in ordine lessicografico crescente."""
    for i in range(len(ss) - 1):
        if ss[i] > ss[i + 1]:
            return False
    return True


def isBackwardSorted(ss):
    """Restituisce True se gli elementi sono in ordine lessicografico decrescente."""
    for i in range(len(ss) - 1):
        if ss[i] < ss[i + 1]:
            return False
    return True


def isSorted(ss):
    """Svolge la stessa elaborazione di isForwardSorted senza copiarne il codice."""
    return isForwardSorted(ss)


def isSubstring(s1, s2):
    """Restituisce True se e solo se s1 è sottostringa di s2."""
    return s1 in s2


def isSubsequence(s1, s2):
    """Restituisce True se e solo se s1 è sottosequenza di s2."""
    idx1 = 0
    idx2 = 0
    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] == s2[idx2]:
            idx1 += 1
        idx2 += 1
    return idx1 == len(s1)


def getAllSubsequences(s):
    """Genera tutte le sottosequenze di s usando i vettori caratteristici binari."""
    n = len(s)
    subs = []
    for i in range(2 ** n):
        # Converte i in binario su n bit (aggiungendo zeri a sinistra)
        bin_str = bin(i)[2:].zfill(n)
        sub = ""
        for j in range(n):
            if bin_str[j] == "1":
                sub += s[j]
        subs.append(sub)
    return subs


def numSubsequences(s):
    """Calcola il numero di sottosequenze senza generarle: 2^n."""
    return 2 ** len(s)


def reverse(lista):
    """Inverte il contenuto della lista passata come argomento (in-place)."""
    n = len(lista)
    for i in range(n // 2):
        # Scambio degli elementi simmetrici
        temp = lista[i]
        lista[i] = lista[n - 1 - i]
        lista[n - 1 - i] = temp


# =============================================================================
# SEZIONE DI COLLAUDO
# =============================================================================
if __name__ == "__main__":
    test_strings = ["", "a", "ab", "abc", "abcdefghilm"]

    print("=== COLLAUDO SOTTOSTRINGHE ===")
    for s in test_strings:
        print(f"\nStringa di test: '{s}'")
        ss = getAllSubstrings(s)
        prevista = numSubstrings(s)
        effettiva = len(ss)
        print(f"Lunghezza prevista: {prevista} | Lunghezza effettiva: {effettiva}")

        if prevista != effettiva:
            print("ERRORE: La lunghezza prevista e quella effettiva differiscono!")

        if not areUnique(ss):
            print("ERRORE: Gli elementi di ss non sono tutti unici!")

        if not isSortedByIncreasingLength(ss):
            print("ERRORE: ss non è ordinata per lunghezza crescente!")

        ss.sort()
        if not isForwardSorted(ss):
            print("ERRORE: ss non risulta ordinata in modo lessicografico crescente!")

        reverse(ss)
        if not isBackwardSorted(ss):
            print("ERRORE: ss non risulta ordinata in modo lessicografico decrescente!")

    print("\n=== COLLAUDO SOTTOSEQUENZE ===")
    for s in test_strings:
        print(f"\nStringa di test: '{s}'")
        ss = getAllSubsequences(s)
        prevista = numSubsequences(s)
        effettiva = len(ss)
        print(f"Lunghezza prevista: {prevista} | Lunghezza effettiva: {effettiva}")

        if prevista != effettiva:
            print("ERRORE: La lunghezza prevista e quella effettiva differiscono!")

        if not areUnique(ss):
            print("ERRORE: Gli elementi di ss non sono tutti unici!")