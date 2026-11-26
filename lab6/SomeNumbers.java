
import java.util.Scanner;

public class SomeNumbers {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // Opzionale: forza il punto decimale (es. 3.5) indipendentemente dalla lingua
        // del SO /// --
        // in.useLocale(Locale.US);

        double sum = 0;
        double absSum = 0;
        double product = 1;
        int count = 0;

        System.out.println("Inserisci una sequenza di numeri (termina con EOF):");
        // Legge numeri finché ce ne sono e aggiorna somma, somma assoluta, prodotto e conteggio
        while (in.hasNextDouble()) {
            double value = in.nextDouble();
            sum += value;
            absSum += Math.abs(value);
            product *= value;
            count++;
        }

        // Le statistiche vengono stampate solo con almeno due numeri
        if (count < 2) {
            System.out.println("Errore: è necessario inserire almeno due numeri.");
        } else {
            double average = sum / count;
            System.out.println("Somma: " + sum);
            System.out.println("Somma dei valori assoluti: " + absSum);
            System.out.println("Prodotto: " + product);
            System.out.println("Valore medio: " + average);
        }

        in.close();
    }
}