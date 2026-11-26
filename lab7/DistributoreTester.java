public class DistributoreTester {
    public static void main(String[] args) {
        // Partiamo con risorse ridotte (1 cialda e 60 ml di acqua) per testare facilmente gli "ostacoli"
        DistributoreCaffe macchina = new DistributoreCaffe(1, 60);

        System.out.println("--- 1. Test moneta non valida e credito insufficiente ---");
        macchina.inserisciMoneta(0.05); // rifiutata
        macchina.inserisciMoneta(0.20); // accettata (credito: 0.20)
        System.out.println("Esito erogazione: " + macchina.erogaCaffe()); // fallisce: credito < 0.50

        System.out.println("\n--- 2. Completamento pagamento ed erogazione con resto ---");
        macchina.inserisciMoneta(0.50); // credito: 0.70
        System.out.println("Esito erogazione: " + macchina.erogaCaffe()); // riesce, resto 0.20
        // Ora restano: 0 cialde e 20 ml di acqua

        System.out.println("\n--- 3. Ostacolo: cialde e acqua esaurite ---");
        macchina.inserisciMoneta(0.50); // credito: 0.50
        System.out.println("Esito erogazione: " + macchina.erogaCaffe()); // fallisce: mancano cialde e acqua

        System.out.println("\n--- 4. Ricarica parziale (solo cialde) -> manca ancora acqua ---");
        macchina.ricarica(2, 0);
        System.out.println("Esito erogazione: " + macchina.erogaCaffe()); // fallisce: acqua 20 ml < 40 ml

        System.out.println("\n--- 5. Ricarica acqua (e test valori negativi ignorati) -> erogazione riuscita ---");
        macchina.ricarica(-5, -100); // deve essere ignorata
        macchina.ricarica(0, 100);   // acqua diventa 120 ml
        // Il credito di 0.50 inserito al punto 3 e' ancora presente!
        System.out.println("Esito erogazione: " + macchina.erogaCaffe()); // riesce, nessun resto

        System.out.println("\n--- 6. Chiusura giornata: ritiro incasso ---");
        double incasso = macchina.ritiraIncasso();
        System.out.printf("Incasso totale di giornata ritirato: %.2f euro%n", incasso);
        System.out.printf("Verifica azzeramento incasso: %.2f euro%n", macchina.ritiraIncasso());
    }
}
