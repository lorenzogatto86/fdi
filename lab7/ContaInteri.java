import java.util.InputMismatchException;
import java.util.Scanner;

public class ContaInteri {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int contatore = 0;

        // hasNext() controlla se ci sono ancora dati nello standard input (fino a EOF: Ctrl+Z su Windows, Ctrl+D su Linux/Mac).
        // NON usare hasNextInt() come condizione del while, altrimenti il ciclo si fermerebbe al primo dato non intero!
        while (scan.hasNext()) {
            try {
                // Prova a leggere il prossimo token come intero
                scan.nextInt();
                contatore++;
            } catch (InputMismatchException e) {
                // nextInt() fallisce SENZA consumare il dato errato dal flusso di input.
                // Chiamiamo scan.next() per scartare il token non valido ed evitare un ciclo infinito.
                scan.next();
            }
        }

        System.out.println("Numero di interi letti: " + contatore);
        scan.close();
    }
}
