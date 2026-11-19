public class Scomposizione {
    public static void main(String[] args) {
        // Definizione di una costante intera (tra 0 e 999)
        final int NUMERO = 23;

        // Metodo 1 (da sinistra a destra: dalla cifra più significativa)
        int centinaia = NUMERO / 100; // 23 / 100 = 0
        int resto = NUMERO % 100; // 23 % 100 = 23
        int decine = resto / 10; // 23 / 10 = 2
        int unita = resto % 10; // 23 % 10 = 3

        /*
         * // Metodo 2 alternativo (da destra a sinistra: dalla cifra meno
         * significativa)
         * int unita = NUMERO % 10; // 23 % 10 = 3
         * int temp = NUMERO / 10; // 23 / 10 = 2
         * int decine = temp % 10; // 2 % 10 = 2
         * int centinaia = temp / 10; // 2 / 10 = 0
         */

        System.out.println(centinaia + " " + decine + " " + unita);
    }
}