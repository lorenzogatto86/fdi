import java.awt.Color;
import java.io.IOException;

public class DecodeImageWest {
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.out.println("Usage: java DecodeImageWest inputFileName outputFileName");
            System.exit(0);
        }

        SimpleImage img = new SimpleImage(args[0]);

        // Scorre tutti i pixel dell'immagine (colonne x, righe y).
        // Azzera rosso e verde; se il blu è minore di 16 lo moltiplica per 16,
        // altrimenti lo azzera: così emerge l'immagine nascosta nel blu.
        for (int x = 0; x < img.width(); x++) {
            for (int y = 0; y < img.height(); y++) {
                Color c = img.get(x, y);

                int r = 0;
                int g = 0;
                int b = c.getBlue();

                if (b < 16) {
                    b = b * 16;
                } else {
                    b = 0;
                }

                c = new Color(r, g, b);
                img.set(x, y, c);
            }
        }

        img.save(args[1]);
        System.out.println("Done...");
    }
}