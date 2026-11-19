public class LimitiTipiNumerici {
    public static void main(String[] args) {
        System.out.println("=== TIPI INTERI ===");
        System.out.println("byte    -> Min: " + Byte.MIN_VALUE + " | Max: " + Byte.MAX_VALUE);
        System.out.println("short   -> Min: " + Short.MIN_VALUE + " | Max: " + Short.MAX_VALUE);
        System.out.println("int     -> Min: " + Integer.MIN_VALUE + " | Max: " + Integer.MAX_VALUE);
        System.out.println("long    -> Min: " + Long.MIN_VALUE + " | Max: " + Long.MAX_VALUE);

        System.out.println("\n=== TIPI IN VIRGOLA MOBILE (REALI) ===");
        System.out.println("float   -> Min: " + Float.MIN_VALUE + " | Max: " + Float.MAX_VALUE);
        System.out.println("double  -> Min: " + Double.MIN_VALUE + " | Max: " + Double.MAX_VALUE);

        System.out.println("\n=== TIPO CARATTERE (codifica numerica Unicode a 16 bit) ===");
        System.out.println("char    -> Min: " + (int) Character.MIN_VALUE + " | Max: " + (int) Character.MAX_VALUE);
    }
}