import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        int WIDTH = 800;
        int HEIGHT = 600;

        JFrame frame = new JFrame("Fractal Plant");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.setPreferredSize(new Dimension(WIDTH, HEIGHT));

        FractalPlant fractalPlant = new FractalPlant();
        frame.add(fractalPlant);

        frame.pack();
        frame.setVisible(true);
    }
}