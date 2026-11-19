
public class Variabili {
    public static void main(String[] args) {
        // 1. Definizione e inizializzazione delle variabili
        int larghezza = 20;
        int lunghezza = 30;

        // 2. Modifica del valore di larghezza a 40
        larghezza = 40;

        // 3. Modifica del valore di lunghezza aggiungendo 15 al valore attuale
        lunghezza = lunghezza + 15; // in alternativa: lunghezza += 15;

        // 4. Stampa del messaggio e del prodotto
        System.out.print("L'area del tavolo e' ");
        System.out.println(larghezza * lunghezza);
    }
}
