public class Personaggio {
    private String nome;
    private int puntiVita;
    private int puntiVitaMax;
    private int attacco;
    private int livello;

    // Costruttore completo: inizializza i parametri e imposta il livello iniziale a
    // 1
    public Personaggio(String nome, int puntiVitaMax, int attacco) {
        this.nome = nome;
        this.puntiVitaMax = puntiVitaMax;
        this.puntiVita = puntiVitaMax;
        this.attacco = attacco;
        this.livello = 1;
    }

    // Costruttore semplificato: delega al costruttore completo con valori di
    // default
    public Personaggio(String nome) {
        this(nome, 100, 15);
    }

    // Metodi getter per leggere lo stato interno del personaggio
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

    // Restituisce true se il personaggio ha almeno 1 punto vita
    public boolean isVivo() {
        return puntiVita > 0;
    }

    // Riduce i punti vita impedendo che scendano sotto lo zero
    public void subisciDanno(int danno) {
        if (danno > 0) {
            puntiVita -= danno;
            if (puntiVita < 0) {
                puntiVita = 0;
            }
        }
    }

    // Incrementa i punti vita senza superare puntiVitaMax (solo se il personaggio è
    // vivo)
    public void cura(int puntiCura) {
        if (isVivo() && puntiCura > 0) {
            puntiVita += puntiCura;
            if (puntiVita > puntiVitaMax) {
                puntiVita = puntiVitaMax;
            }
        }
    }

    // Infligge il danno dell'attaccante al bersaglio solo se entrambi sono vivi
    public void attacca(Personaggio bersaglio) {
        if (bersaglio != null && this.isVivo() && bersaglio.isVivo()) {
            bersaglio.subisciDanno(this.attacco);
        }
    }

    // Incrementa livello (+1), punti vita massimi (+20) e attacco (+5)
    public void salitaDiLivello() {
        livello++;
        puntiVitaMax += 20;
        attacco += 5;
    }

    // Restituisce una descrizione testuale completa dello stato del personaggio
    @Override
    public String toString() {
        return nome + " [Liv. " + livello + "] - HP: " + puntiVita + "/" + puntiVitaMax
                + " - Attacco: " + attacco;
    }
}