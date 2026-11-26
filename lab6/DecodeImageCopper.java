import java.awt.Color;
import java.io.IOException;

public class DecodeImageCopper {
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.out.println("Usage: java DecodeImageCopper inputFileName outputFileName");
            System.exit(0);
        }

        SimpleImage img = new SimpleImage(args[0]);

        // Scorre tutti i pixel dell'immagine (colonne x, righe y).
        // Azzera il rosso e moltiplica verde e blu per 19 (massimo 255)
        // per far emergere l'immagine nascosta in quei canali.
        for (int x = 0; x < img.width(); x++) {
            for (int y = 0; y < img.height(); y++) {
                Color c = img.get(x, y);

                int r = 0;
                int g = Math.min(255, c.getGreen() * 19);
                int b = Math.min(255, c.getBlue() * 19);

                c = new Color(r, g, b);
                img.set(x, y, c);
            }
        }

        img.save(args[1]);
        System.out.println("Done...");
    }
}