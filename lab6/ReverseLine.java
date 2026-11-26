import java.util.Scanner;

public class ReverseLine {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Inserisci una riga di testo: ");
        String line = in.nextLine();

        String reversed = "";
        // Scorre la riga dall'ultimo carattere al primo, costruendo la stringa invertita
        for (int i = line.length() - 1; i >= 0; i--) {
            reversed = reversed + line.charAt(i);
        }

        System.out.println(reversed);
        in.close();
    }
}