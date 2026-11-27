public class ArenaMain {

    // Testa la gestione dell'inventario compatto (inserimento, shift a sinistra e casi limite)
    public static void main(String[] args) {
        // Setup iniziale
        Personaggio arthur = new Personaggio("Arthur", 100, 25, 5, 4);
        Personaggio drago = new Personaggio("Drago Giovane", 150, 35, 5, 1);

        System.out.println("=== SETUP INIZIALE ===");
        System.out.println(arthur);
        System.out.println(drago);
        System.out.println();

        // 1. Riempimento parziale
        System.out.println("=== 1. RIEMPIMENTO PARZIALE ===");
        Pozione p1 = new Pozione("Pozione Minore", 15);
        Pozione p2 = new Pozione("Pozione Media", 30);
        Pozione p3 = new Pozione("Elisir Supremo", 60);

        arthur.raccogliPozione(p1);
        arthur.raccogliPozione(p2);
        arthur.raccogliPozione(p3);
        arthur.stampaInventario();
        System.out.println();

        // 2. Test del limite logico (slot 3 è fisicamente valido, ma logicamente vuoto)
        System.out.println("=== 2. TEST DEL LIMITE LOGICO ===");
        arthur.usaPozione(3);
        System.out.println();

        // 3. Combattimento (2 turni del Drago) e verifica dello shift a sinistra
        System.out.println("=== 3. COMBATTIMENTO E SHIFT ===");
        drago.attacca(arthur);
        drago.attacca(arthur);
        arthur.usaPozione(0);
        arthur.stampaInventario();
        System.out.println();

        // 4. Inserimento in coda dopo lo shift
        System.out.println("=== 4. INSERIMENTO IN CODA ===");
        Pozione p4 = new Pozione("Antidoto Curativo", 20);
        arthur.raccogliPozione(p4);
        arthur.stampaInventario();
        System.out.println();

        // 5. Svuotamento completo e tentativo su zaino vuoto
        System.out.println("=== 5. SVUOTAMENTO E CASI LIMITE ===");
        for (int i = 0; i < 3; i++) {
            arthur.usaPozione(0);
            arthur.stampaInventario();
        }
        arthur.usaPozione(0);
    }
}
