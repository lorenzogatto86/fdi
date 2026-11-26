import java.util.Scanner;

public class ReverseWords {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String result = "";

        // Legge una parola alla volta fino a EOF
        while (in.hasNext()) {
            String word = in.next();
            String reversedWord = "";
            
            // Inverte i caratteri della parola corrente
            for (int i = word.length() - 1; i >= 0; i--) {
                reversedWord = reversedWord + word.charAt(i);
            }

            // Aggiunge uno spazio solo tra una parola e l'altra
            if (!result.isEmpty()) {
                result = result + " ";
            }
            result = result + reversedWord;
        }

        System.out.println(result);
        in.close();
    }
}