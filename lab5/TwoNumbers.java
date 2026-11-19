import java.util.Scanner;

public class TwoNumbers {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Inserisci il primo numero reale: ");
        double a = in.nextDouble();

        System.out.print("Inserisci il secondo numero reale: ");
        double b = in.nextDouble();

        // 1. Somma
        double somma = a + b;

        // 2. Prodotto
        double prodotto = a * b;

        // 3. Valore medio
        double media = (a + b) / 2.0;

        // 4 e 5. Valore massimo e valore minimo (senza usare Math.max / Math.min)
        double massimo;
        double minimo;
        if (a >= b) {
            massimo = a;
            minimo = b;
        } else {
            massimo = b;
            minimo = a;
        }

        // 6. Valore assoluto della differenza (senza usare Math.abs)
        double diffAssoluta = a - b;
        if (diffAssoluta < 0) {
            diffAssoluta = -diffAssoluta; // oppure: diffAssoluta = b - a;
        }
        // Nota: un'alternativa ancora più furba è fare direttamente:
        // double diffAssoluta = massimo - minimo;

        // Stampa dei risultati
        System.out.println("\n--- Risultati ---");
        System.out.println("Somma:                          " + somma);
        System.out.println("Prodotto:                       " + prodotto);
        System.out.println("Valore medio:                   " + media);
        System.out.println("Valore massimo:                 " + massimo);
        System.out.println("Valore minimo:                  " + minimo);
        System.out.println("Valore assoluto della diff.:    " + diffAssoluta);

        in.close();
    }
}