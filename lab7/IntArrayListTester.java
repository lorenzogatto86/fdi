// Classe di test per verificare i metodi di IntArrayList
public class IntArrayListTester {
    public static void main(String[] args) {
        IntArrayList list = new IntArrayList();
        System.out.println("Lista iniziale: " + list + " | size = " + list.size());

        // Test add(element) e resize automatico (1 -> 2 -> 4 -> 8)
        list.add(1);
        list.add(2);
        list.add(5);
        list.add(4);
        System.out.println("Dopo add: " + list + " | size = " + list.size());

        // Test get e contains
        System.out.println("Elemento in posizione 2: " + list.get(2));
        System.out.println("Contiene 5? " + list.contains(5));
        System.out.println("Contiene 0? " + list.contains(0)); // Verifica che non controlli le celle libere

        // Test add(position, element)
        list.add(0, 99);           // Inserimento in testa
        list.add(2, 77);           // Inserimento in mezzo
        list.add(list.size(), 88); // Inserimento in coda
        System.out.println("Dopo add posizionali: " + list + " | size = " + list.size());

        // Test remove(position)
        int rimosso = list.remove(2);
        System.out.println("Rimosso elemento " + rimosso + " -> " + list + " | size = " + list.size());

        // Test gestione IllegalArgumentException
        try {
            list.get(100);
        } catch (IllegalArgumentException e) {
            System.out.println("Eccezione catturata correttamente: " + e.getMessage());
        }
    }
}
