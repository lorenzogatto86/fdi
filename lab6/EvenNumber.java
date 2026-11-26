import java.util.Scanner;

public class EvenNumber {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Inserisci un numero intero pari: ");
        int num = in.nextInt();

        // Un numero è pari se il resto della divisione per 2 è 0
        if (num % 2 == 0) {
            System.out.println("Bravo! Il numero " + num + " è pari.");
        } else {
            // Secondo (e ultimo) tentativo

            System.out.println("Errore: il numero inserito è dispari.");
            System.out.print("Riprova, inserisci un numero intero pari: ");
            num = in.nextInt();

            if (num % 2 == 0) {
                System.out.println("Bravo! Il numero " + num + " è pari.");
            } else {
                System.out.println("Peccato! Neanche il secondo numero è pari.");
            }
        }

        in.close();
    }
}