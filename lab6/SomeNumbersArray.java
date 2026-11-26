import java.util.Scanner;

public class SomeNumbersArray {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] data = new int[2]; // Capacità iniziale piccola per testare facilmente il resize
        int vSize = 0; // Dimensione logica (elementi effettivamente inseriti)

        System.out.println("Inserisci una sequenza di numeri interi (termina con EOF):");
        // Legge interi fino a EOF; se l'array è pieno ne raddoppia la capacità
        while (in.hasNextInt()) {
            if (vSize == data.length) {
                data = resize(data, data.length * 2);
            }
            data[vSize] = in.nextInt();
            vSize++;
        }
        in.close();

        if (vSize < 2) {
            System.out.println("Errore: è necessario inserire almeno due numeri.");
            return;
        }

        // Calcolo statistiche dall'array
        long sum = 0;
        long absSum = 0;
        long product = 1;

        for (int i = 0; i < vSize; i++) {
            sum += data[i];
            absSum += Math.abs(data[i]);
            product *= data[i];
        }

        double average = (double) sum / vSize;

        System.out.println("Somma: " + sum);
        System.out.println("Somma dei valori assoluti: " + absSum);
        System.out.println("Prodotto: " + product);
        System.out.println("Valore medio: " + average);

        // Ordinamento per selezione sulla porzione valida [0 .. vSize - 1]
        selectionSort(data, vSize);

        System.out.print("Array ordinato: ");
        for (int i = 0; i < vSize; i++) {
            System.out.print(data[i] + (i < vSize - 1 ? " " : ""));
        }
        System.out.println();
    }

    // Crea un nuovo array di dimensione newLength e copia i vecchi elementi
    public static int[] resize(int[] oldArray, int newLength) {
        int[] newArray = new int[newLength];
        int elementsToCopy = Math.min(oldArray.length, newLength);
        for (int i = 0; i < elementsToCopy; i++) {
            newArray[i] = oldArray[i];
        }
        return newArray;
    }

    // Selection Sort su array parzialmente riempito
    // Il selection ordina un array di interi in modo crescente sort cercando il
    // minimo a ciclo ogni e scambiandolo con l'elemento corrente
    public static void selectionSort(int[] a, int size) {
        for (int i = 0; i < size - 1; i++) {
            // Cerca la posizione del minimo nella parte non ancora ordinata
            int minPos = i;
            for (int j = i + 1; j < size; j++) {
                if (a[j] < a[minPos]) {
                    minPos = j;
                }
            }
            // Scambio (swap) tra a[i] e a[minPos]
            if (minPos != i) {
                int temp = a[i];
                a[i] = a[minPos];
                a[minPos] = temp;
            }
        }
    }
}