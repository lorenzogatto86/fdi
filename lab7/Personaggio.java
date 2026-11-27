public class Personaggio {
    private String nome;
    private int puntiVita;
    private int puntiVitaMax;
    private int attacco;
    private int difesa;
    private int livello;
    private Pozione[] inventario;
    private int numOggetti;

    // Costruttore completo: inizializza statistiche e alloca l'array dello zaino vuoto
    public Personaggio(String nome, int puntiVitaMax, int attacco, int difesa, int capacitaZaino) {
        this.nome = nome;
        this.puntiVitaMax = puntiVitaMax;
        this.puntiVita = puntiVitaMax;
        this.attacco = attacco;
        this.difesa = difesa;
        this.livello = 1;
        this.inventario = new Pozione[capacitaZaino];
        this.numOggetti = 0;
    }

    public String getNome() {
        return nome;
    }

    public int getPuntiVita() {
        return puntiVita;
    }

    public int getLivello() {
        return livello;
    }

    public int getAttacco() {
        return attacco;
    }

    public int getDifesa() {
        return difesa;
    }

    public boolean isVivo() {
        return puntiVita > 0;
    }

    // Calcola il danno effettivo sottraendo la difesa (minimo 1) e aggiorna gli HP
    public void subisciDanno(int dannoInflitto) {
        int dannoEffettivo = dannoInflitto - this.difesa;
        if (dannoEffettivo < 1) {
            dannoEffettivo = 1;
        }

        this.puntiVita -= dannoEffettivo;
        if (this.puntiVita < 0) {
            this.puntiVita = 0;
        }

        System.out.println("  -> " + this.nome + " subisce " + dannoEffettivo
                + " danni! (HP: " + this.puntiVita + "/" + this.puntiVitaMax + ")");
    }

    // Cura il personaggio solo se è vivo, senza superare puntiVitaMax
    public void cura(int puntiCura) {
        if (isVivo() && puntiCura > 0) {
            this.puntiVita += puntiCura;
            if (this.puntiVita > this.puntiVitaMax) {
                this.puntiVita = this.puntiVitaMax;
            }
        }
    }

    // Infligge danno al bersaglio solo se entrambi sono vivi
    public void attacca(Personaggio bersaglio) {
        if (bersaglio != null && this.isVivo() && bersaglio.isVivo()) {
            bersaglio.subisciDanno(this.attacco);
        }
    }

    public void salitaDiLivello() {
        livello++;
        puntiVitaMax += 20;
        attacco += 5;
    }

    // Inserisce la pozione in coda nella prima posizione libera (numOggetti) se c'è spazio
    public boolean raccogliPozione(Pozione p) {
        if (p == null) {
            return false;
        }
        if (numOggetti < inventario.length) {
            inventario[numOggetti] = p;
            numOggetti++;
            System.out.println(this.nome + " mette [" + p.getNome() + "] nello zaino ("
                    + numOggetti + "/" + inventario.length + ")");
            return true;
        } else {
            System.out.println("Zaino pieno");
            return false;
        }
    }

    // Usa la pozione all'indice dato e compatta l'array facendo scorrere a sinistra gli elementi
    public void usaPozione(int indice) {
        if (indice < 0 || indice >= numOggetti) {
            System.out.println("Errore: nessuna pozione valida nello slot " + indice + ".");
            return;
        }

        Pozione p = inventario[indice];
        cura(p.getCura());
        System.out.println(this.nome + " usa [" + p.getNome() + "]! (HP: "
                + this.puntiVita + "/" + this.puntiVitaMax + ")");

        // Shift a sinistra: sovrascrive la posizione usata spostando indietro gli elementi successivi
        for (int i = indice; i < numOggetti - 1; i++) {
            inventario[i] = inventario[i + 1];
        }

        inventario[numOggetti - 1] = null;
        numOggetti--;
    }

    // Stampa l'occupazione dello zaino e i nomi delle pozioni presenti nella porzione valida
    public void stampaInventario() {
        System.out.print("Zaino (" + numOggetti + "/" + inventario.length + "): ");
        if (numOggetti == 0) {
            System.out.println("Zaino vuoto");
        } else {
            // Scorre solo fino a numOggetti per evitare di leggere celle null
            for (int i = 0; i < numOggetti; i++) {
                System.out.print("[" + inventario[i].getNome() + "] ");
            }
            System.out.println();
        }
    }

    @Override
    public String toString() {
        return nome + " [Liv. " + livello + "] - HP: " + puntiVita + "/" + puntiVitaMax
                + " - ATK: " + attacco + " - DEF: " + difesa;
    }
}
