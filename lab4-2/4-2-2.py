def recMin(lista):
    # Caso base: una lista di un solo elemento ha quell'elemento come minimo
    if len(lista) == 1:
        return lista[0]
    
    # Passo ricorsivo: trova il minimo della sottolista (dal secondo elemento in poi)
    min_resto = recMin(lista[1:])
    
    # Confronta il primo elemento con il minimo del resto della lista
    if lista[0] < min_resto:
        return lista[0]
    else:
        return min_resto


# --- Collaudo ---
if __name__ == "__main__":
    valori = [14, 7, 23, -5, 0, 12, -3]
    print("Lista:", valori)
    print("Valore minimo:", recMin(valori))