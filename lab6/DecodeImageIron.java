import java.awt.Color;
import java.io.IOException;

public class DecodeImageIron {
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.out.println("Usage: java DecodeImageIron inputFileName outputFileName");
            System.exit(0);
        }

        SimpleImage img = new SimpleImage(args[0]);

        // Scorre tutti i pixel dell'immagine (colonne x, righe y).
        // Tiene solo il rosso moltiplicato per 10 (massimo 255) e azzera
        // verde e blu, così l'immagine nascosta nel rosso diventa visibile.
        for (int x = 0; x < img.width(); x++) {
            for (int y = 0; y < img.height(); y++) {
                Color c = img.get(x, y);

                int r = c.getRed() * 10;
                // Sicurezza per restare nel range RGB [0, 255]
                if (r > 255) {
                    r = 255;
                }
                int g = 0;
                int b = 0;

                c = new Color(r, g, b);
                img.set(x, y, c);
            }
        }

        img.save(args[1]);
        System.out.println("Done...");
    }
}