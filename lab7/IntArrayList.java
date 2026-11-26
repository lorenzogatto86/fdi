public class IntArrayList {
    // Dimensione fisica iniziale dell'array interno
    private static final int INITIAL_SIZE = 1;

    private int[] v;     // Array fisico (puo' contenere celle libere in fondo)
    private int vSize;   // Dimensione logica: numero di elementi validi attualmente presenti

    // Costruttore: inizializza l'array con dimensione INITIAL_SIZE e 0 elementi validi
    public IntArrayList() {
        v = new int[INITIAL_SIZE];
        vSize = 0;
    }

    // Raddoppia la capacita' fisica dell'array interno copiando gli elementi validi
    public void resize() {
        int[] newV = new int[v.length * 2];
        for (int i = 0; i < vSize; i++) {
            newV[i] = v[i];
        }
        // Sostituisce il riferimento al vecchio array con quello al nuovo array piu' grande
        v = newV;
    }

    // Restituisce l'elemento in posizione index
    public int get(int index) {
        // Gli indici validi vanno da 0 a vSize - 1 (non fino a v.length - 1!)
        if (index < 0 || index >= vSize) {
            throw new IllegalArgumentException("Indice non valido: " + index);
        }
        return v[index];
    }

    // Restituisce la dimensione logica (numero di elementi inseriti)
    public int size() {
        return vSize;
    }

    // Aggiunge element in coda all'array
    public void add(int element) {
        if (vSize == v.length) {
            resize();
        }
        v[vSize] = element;
        vSize++;
    }

    // Verifica se element e' presente nella parte valida dell'array
    public boolean contains(int element) {
        // Attenzione: il ciclo si ferma a vSize, NON a v.length
        // (altrimenti cercando 0 si troverebbero gli zeri di default nelle celle libere)
        for (int i = 0; i < vSize; i++) {
            if (v[i] == element) {
                return true;
            }
        }
        return false;
    }

    // Rappresentazione testuale nel formato "[1,2,5,4]"
    public String toString() {
        String result = "[";
        for (int i = 0; i < vSize; i++) {
            result += v[i];
            if (i < vSize - 1) {
                result += ",";
            }
        }
        result += "]";
        return result;
    }

    // Inserisce element nella posizione indicata, spostando a destra gli elementi successivi
    public void add(int position, int element) {
        // position == vSize e' valido: corrisponde a inserire in coda
        if (position < 0 || position > vSize) {
            throw new IllegalArgumentException("Posizione di inserimento non valida: " + position);
        }
        if (vSize == v.length) {
            resize();
        }
        // Spostamento a destra: si parte DALLA FINE per non sovrascrivere i valori non ancora spostati
        for (int i = vSize; i > position; i--) {
            v[i] = v[i - 1];
        }
        v[position] = element;
        vSize++;
    }

    // Rimuove e restituisce l'elemento in posizione position, mantenendo compatto l'array
    public int remove(int position) {
        if (position < 0 || position >= vSize) {
            throw new IllegalArgumentException("Posizione di rimozione non valida: " + position);
        }
        int removed = v[position];
        // Spostamento a sinistra: si parte da position verso la fine per chiudere il "buco"
        for (int i = position; i < vSize - 1; i++) {
            v[i] = v[i + 1];
        }
        vSize--;
        return removed;
    }
}
