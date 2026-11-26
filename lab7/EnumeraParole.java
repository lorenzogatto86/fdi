import java.util.Scanner;

public class EnumeraParole {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        System.out.println("Inserisci una frase composta da piu' parole:");
        // nextLine() legge l'intera riga fino al carattere di a capo (Invio)
        String riga = console.nextLine();

        // Creiamo un secondo Scanner collegato alla stringa letta, invece che alla tastiera
        Scanner scanline = new Scanner(riga);

        // hasNext() e next() separano automaticamente la stringa sui caratteri di spaziatura (spazi, tab, ecc.)
        while (scanline.hasNext()) {
            String parola = scanline.next();
            System.out.println(parola);
        }

        scanline.close();
        console.close();
    }
}
