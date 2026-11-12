def selectionSort(lista):
    """Ordinamento per selezione (Selection Sort)."""
    # Creiamo una copia per restituire una versione ordinata senza alterare l'originale
    a = list(lista)
    n = len(a)

    for i in range(n - 1):
        # Trova l'indice del minimo nella parte non ancora ordinata [i .. n-1]
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Scambia il minimo trovato con l'elemento in posizione i
        a[i], a[min_idx] = a[min_idx], a[i]

    return a


def insertionSort(lista):
    """Ordinamento per inserimento (Insertion Sort)."""
    a = list(lista)
    n = len(a)

    for i in range(1, n):
        valore_da_inserire = a[i]
        j = i - 1
        # Sposta a destra gli elementi della parte ordinata che sono maggiori di valore_da_inserire
        while j >= 0 and a[j] > valore_da_inserire:
            a[j + 1] = a[j]
            j -= 1
        # Inserisce l'elemento nella posizione corretta
        a[j + 1] = valore_da_inserire

    return a


def merge(sinistra, destra):
    """Funzione ausiliaria che fonde due liste ordinate in un'unica lista ordinata."""
    risultato = []
    i = 0
    j = 0

    # Confronta gli elementi in testa alle due liste e inserisce il minore
    while i < len(sinistra) and j < len(destra):
        if sinistra[i] <= destra[j]:
            risultato.append(sinistra[i])
            i += 1
        else:
            risultato.append(destra[j])
            j += 1

    # Aggiunge gli eventuali elementi rimasti nella lista di sinistra o di destra
    while i < len(sinistra):
        risultato.append(sinistra[i])
        i += 1

    while j < len(destra):
        risultato.append(destra[j])
        j += 1

    return risultato


def mergeSort(lista):
    """Ordinamento ricorsivo Merge Sort (Divide et Impera)."""
    # Caso base: una lista con 0 o 1 elementi è già ordinata
    if len(lista) <= 1:
        return list(lista)

    # 1. Divide: spezza la lista a metà
    mid = len(lista) // 2
    meta_sinistra = mergeSort(lista[:mid])
    meta_destra = mergeSort(lista[mid:])

    # 2. Impera / Combina: fonde le due metà ordinate
    return merge(meta_sinistra, meta_destra)


# --- Collaudo ---
if __name__ == "__main__":
    dati = [38, 27, 43, 3, 9, 82, 10, -4, 0]
    print("Lista originale: ", dati)
    print("Selection Sort:  ", selectionSort(dati))
    print("Insertion Sort:  ", insertionSort(dati))
    print("Merge Sort:      ", mergeSort(dati))