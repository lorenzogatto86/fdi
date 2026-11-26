public class SommaRicorsiva {

    // Metodo ricorsivo che calcola la somma dei primi n interi positivi: 1 + 2 + ... + n
    public static int somma(int n) {
        // Controllo della precondizione: se n non e' strettamente positivo lanciamo un'eccezione
        if (n <= 0) {
            throw new IllegalArgumentException("Il numero deve essere un intero positivo (> 0), ricevuto: " + n);
        }
        // Caso base: la somma del primo intero positivo e' 1
        if (n == 1) {
            return 1;
        }
        // Passo ricorsivo: somma(n) = n + somma(n - 1)
        return n + somma(n - 1);
    }

    public static void main(String[] args) {
        // Verifica del numero di argomenti passati da riga di comando
        if (args.length != 1) {
            System.out.println("Errore: fornire esattamente un parametro da riga di comando.");
            System.out.println("Uso: java SommaRicorsiva <intero_positivo>");
            return;
        }

        try {
            // Converte la stringa args[0] in intero (lancia NumberFormatException se non e' un intero)
            int n = Integer.parseInt(args[0]);

            // Chiama il metodo ricorsivo (lancia IllegalArgumentException se n <= 0)
            int risultato = somma(n);
            System.out.println("La somma dei primi " + n + " interi positivi e': " + risultato);

        } catch (NumberFormatException e) {
            System.out.println("Errore: il parametro '" + args[0] + "' non e' un numero intero valido.");
        } catch (IllegalArgumentException e) {
            System.out.println("Errore: " + e.getMessage());
        }
    }
}
