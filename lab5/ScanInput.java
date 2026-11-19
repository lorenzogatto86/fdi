import java.util.Scanner;

public class ScanInput {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Inserisci almeno tre parole separate da spazio:");

        // Il metodo next() legge un singolo token (fino al prossimo spazio o a capo)
        String parola1 = in.next();
        String parola2 = in.next();
        String parola3 = in.next();

        // Stampa delle tre parole, una per riga
        System.out.println(parola1);
        System.out.println(parola2);
        System.out.println(parola3);

        in.close();
    }
}