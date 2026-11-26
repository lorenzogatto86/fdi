import java.util.Scanner;

// Variante dell'Esercizio 1 usando Integer.parseInt() e NumberFormatException
public class ContaInteriParse {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int contatore = 0;

        while (scan.hasNext()) {
            // Qui il token viene sempre consumato subito come stringa da scan.next()
            String token = scan.next();
            try {
                Integer.parseInt(token);
                contatore++;
            } catch (NumberFormatException e) {
                // Il token non rappresenta un intero valido: lo ignoriamo.
                // Non serve chiamare scan.next() qui, perche' il token e' gia' stato estratto.
            }
        }

        System.out.println("Numero di interi letti: " + contatore);
        scan.close();
    }
}
