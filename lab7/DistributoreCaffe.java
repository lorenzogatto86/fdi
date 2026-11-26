public class DistributoreCaffe {
    // Costanti private di classe
    private static final double COSTO_CAFFE = 0.50;
    private static final int ACQUA_PER_CAFFE = 40; // in ml
    // Piccola tolleranza per evitare errori di arrotondamento dei numeri in virgola mobile (double)
    private static final double EPSILON = 1e-9;

    // Variabili d'istanza private
    private int numeroCialde;
    private int livelloAcqua;       // in ml
    private double creditoInserito; // double (non int!) per gestire i centesimi (0.10, 0.20, 0.50...)
    private double incassoTotale;

    // Costruttore: normalizza eventuali valori iniziali negativi a 0
    public DistributoreCaffe(int cialdeIniziali, int acquaIniziale) {
        this.numeroCialde = (cialdeIniziali < 0) ? 0 : cialdeIniziali;
        this.livelloAcqua = (acquaIniziale < 0) ? 0 : acquaIniziale;
        this.creditoInserito = 0.0;
        this.incassoTotale = 0.0;
    }

    // Accetta solo i tagli di moneta consentiti (0.10, 0.20, 0.50, 1.00, 2.00 euro)
    public void inserisciMoneta(double importo) {
        if (importo == 0.10 || importo == 0.20 || importo == 0.50
                || importo == 1.00 || importo == 2.00) {
            creditoInserito += importo;
            System.out.printf("Moneta accettata (%.2f euro). Credito attuale: %.2f euro%n",
                    importo, creditoInserito);
        } else {
            System.out.printf("Moneta non valida (%.2f euro). Tagli accettati: 0.10, 0.20, 0.50, 1.00, 2.00%n",
                    importo);
        }
    }

    // Verifica risorse e credito; se tutto e' sufficiente eroga il caffe' e restituisce true
    public boolean erogaCaffe() {
        boolean pronto = true;

        if (numeroCialde < 1) {
            System.out.println("Impossibile erogare: cialde esaurite.");
            pronto = false;
        }
        if (livelloAcqua < ACQUA_PER_CAFFE) {
            System.out.println("Impossibile erogare: acqua insufficiente ("
                    + livelloAcqua + " ml disponibili, servono " + ACQUA_PER_CAFFE + " ml).");
            pronto = false;
        }
        // Usiamo + EPSILON per gestire casi come 0.10 + 0.10 + 0.10 + 0.20 in virgola mobile
        if (creditoInserito + EPSILON < COSTO_CAFFE) {
            System.out.printf("Impossibile erogare: credito insufficiente (%.2f euro inseriti, servono %.2f euro).%n",
                    creditoInserito, COSTO_CAFFE);
            pronto = false;
        }

        if (!pronto) {
            return false;
        }

        // Aggiorna stato del distributore
        numeroCialde--;
        livelloAcqua -= ACQUA_PER_CAFFE;
        incassoTotale += COSTO_CAFFE;

        double resto = creditoInserito - COSTO_CAFFE;
        if (resto > EPSILON) {
            System.out.printf("Caffe' erogato! Resto restituito: %.2f euro%n", resto);
        } else {
            System.out.println("Caffe' erogato! Nessun resto.");
        }

        creditoInserito = 0.0;
        return true;
    }

    // Ricarica cialde e/o acqua solo se i rispettivi valori sono strettamente positivi
    public void ricarica(int nuoveCialde, int nuovaAcqua) {
        if (nuoveCialde > 0) {
            numeroCialde += nuoveCialde;
        }
        if (nuovaAcqua > 0) {
            livelloAcqua += nuovaAcqua;
        }
    }

    // Azzera l'incasso accumulato e restituisce l'importo prelevato
    public double ritiraIncasso() {
        double prelevato = incassoTotale;
        incassoTotale = 0.0;
        return prelevato;
    }
}
