public class Pozione {
    private String nome;
    private int puntiCura;

    // Costruttore: garantisce un valore minimo di 10 punti cura se il parametro è <= 0
    public Pozione(String nome, int puntiCura) {
        this.nome = nome;
        if (puntiCura <= 0) {
            this.puntiCura = 10;
        } else {
            this.puntiCura = puntiCura;
        }
    }

    public String getNome() {
        return nome;
    }

    public int getCura() {
        return puntiCura;
    }

    @Override
    public String toString() {
        return nome + " (+" + puntiCura + " HP)";
    }
}
