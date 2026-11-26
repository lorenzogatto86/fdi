public class ProvaPersonaggio {

    // Simula un combattimento a turni tra un eroe e un mostro usando la classe
    // Personaggio
    public static void main(String[] args) {
        Personaggio eroe = new Personaggio("Cavaliere");
        Personaggio mostro = new Personaggio("Drago", 120, 18);

        System.out.println("=== STATO INIZIALE ===");
        System.out.println(eroe);
        System.out.println(mostro);
        System.out.println();

        boolean pozione = false;
        int turno = 1;

        // Ciclo di combattimento: prosegue finché entrambi i personaggi sono vivi
        while (eroe.isVivo() && mostro.isVivo()) {
            System.out.println("--- Turno " + turno + " ---");

            eroe.attacca(mostro);

            if (mostro.isVivo()) {
                mostro.attacca(eroe);
            }

            if (eroe.isVivo() && eroe.getPuntiVita() < 40) {
                if (!pozione) {
                    System.out.println(eroe.getNome() + " beve una pozione!");
                    eroe.cura(40);
                    pozione = true;
                }
            }

            System.out.println(eroe);
            System.out.println(mostro);
            System.out.println();

            turno++;
        }

        if (eroe.isVivo()) {
            System.out.println(eroe.getNome() + " ha vinto!");
            eroe.salitaDiLivello();
            System.out.println("Nuovo stato: " + eroe);
        } else {
            System.out.println("RIP cavaliere!");
        }
    }
}