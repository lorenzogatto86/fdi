import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Leggi1 {
    public static void main(String[] args) {
        String fileName = "input.txt";

        // try-with-resources: le risorse aperte tra parentesi (FileReader e Scanner)
        // vengono chiuse automaticamente all'uscita dal blocco try, anche in caso di errore.
        try (FileReader r = new FileReader(fileName);
             Scanner scan = new Scanner(r)) {

            // Legge il file una riga alla volta fino alla fine del file
            while (scan.hasNextLine()) {
                String riga = scan.nextLine();
                System.out.println(riga);
            }

        } catch (FileNotFoundException e) {
            // Eccezione piu' specifica: il file non esiste nella cartella corrente o non e' leggibile
            System.out.println("Errore: il file '" + fileName + "' non e' stato trovato.");
        } catch (IOException e) {
            // Eccezione piu' generale (superclasse di FileNotFoundException),
            // necessaria per gestire eventuali errori di I/O in fase di chiusura del FileReader
            System.out.println("Errore di I/O durante la lettura del file: " + e.getMessage());
        }
    }
}
