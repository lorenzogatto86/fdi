public class ProvaStringa {
    public static void main(String[] args) {
        String s = "Laboratorio di Programmazione Java";

        System.out.println("Stringa originale: \"" + s + "\"");

        // 1. length(): restituisce il numero di caratteri della stringa
        System.out.println("Lunghezza della stringa (length): " + s.length());

        // 2. charAt(index): restituisce il carattere in posizione index (da 0 a
        // length()-1)
        System.out.println("Primo carattere (charAt(0)): " + s.charAt(0));
        System.out.println("Ultimo carattere (charAt(length-1)): " + s.charAt(s.length() - 1));

        // 3. substring(beginIndex, endIndex): estrae da beginIndex (incluso) a endIndex
        // (ESCLUSO)
        String primaParola = s.substring(0, 11);
        System.out.println("Sottostringa (0, 11): \"" + primaParola + "\"");

        // 4. substring(beginIndex): estrae da beginIndex fino alla fine della stringa
        String ultimaParola = s.substring(30);
        System.out.println("Sottostringa da indice 30 alla fine: \"" + ultimaParola + "\"");

        // 5. toUpperCase() e toLowerCase()
        System.out.println("Tutto maiuscolo: " + s.toUpperCase());
        System.out.println("Tutto minuscolo: " + s.toLowerCase());

        // 6. repeat(count): ripete la stringa n volte (disponibile da Java 11+)
        String saluto = "Ciao! ";
        System.out.println("Metodo repeat(3): " + saluto.repeat(3));

        // 7. indexOf() e replace() (altri metodi utili della documentazione)
        System.out.println("Indice della parola 'Java': " + s.indexOf("Java"));
        System.out.println("Sostituzione: " + s.replace("Java", "Python"));
    }
}