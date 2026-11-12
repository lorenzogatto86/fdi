def linearSearch(lista, valore):
    """Ricerca lineare: scorre la lista elemento per elemento."""
    for i in range(len(lista)):
        if lista[i] == valore:
            return i
    return -1


def iterativeBinarySearch(lista, valore):
    """Ricerca binaria iterativa (richiede che la lista sia ordinata)."""
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == valore:
            return mid
        elif valore < lista[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def recursiveBinarySearch(lista, valore):
    """
    Ricerca binaria ricorsiva con due soli parametri (lista, valore).
    Gestisce il ricalcolo dell'indice quando si effettua lo slicing a destra.
    """
    # Caso base 1: lista vuota -> elemento non trovato
    if len(lista) == 0:
        return -1

    mid = len(lista) // 2

    # Caso base 2: elemento trovato al centro
    if lista[mid] == valore:
        return mid
    # Passo ricorsivo sinistro: cerco nella metà sinistra
    elif valore < lista[mid]:
        return recursiveBinarySearch(lista[:mid], valore)
    # Passo ricorsivo destro: cerco nella metà destra
    else:
        risultato_destra = recursiveBinarySearch(lista[mid + 1 :], valore)
        if risultato_destra == -1:
            return -1
        else:
            # Sommo lo spiazzamento (mid + 1) per ottenere l'indice nella lista originale!
            return (mid + 1) + risultato_destra


# --- Collaudo ---
if __name__ == "__main__":
    numeri_ordinati = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    for target in [23, 2, 91, 50]:
        print(f"\nRicerca del valore {target}:")
        print("  linearSearch:         ", linearSearch(numeri_ordinati, target))
        print("  iterativeBinarySearch:", iterativeBinarySearch(numeri_ordinati, target))
        print("  recursiveBinarySearch:", recursiveBinarySearch(numeri_ordinati, target))