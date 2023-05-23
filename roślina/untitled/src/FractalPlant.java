import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Stack;
import javax.swing.JPanel;
import javax.swing.Timer;

public class FractalPlant extends JPanel implements ActionListener {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private static final double ANGLE = 25.0;
    private static final int ITERATIONS = 50;
    private static final double INITIAL_LENGTH = 2;
    private static final int RECTANGLE_SIZE = 2;

    private String word;
    private int iteration;
    private final Timer timer;
    private final int[][] map = new int[HEIGHT][WIDTH];

    public FractalPlant() {
        this.word = "X";
        this.iteration = 0;
        this.timer = new Timer(300, this);
        this.timer.start();
    }

    private void generateWord() {
        StringBuilder newWord = new StringBuilder();

        for (char symbol : word.toCharArray()) {
            if (symbol == 'X') {
                newWord.append("F+[[X]-X]-F[-FX]+X");
            } else if (symbol == 'F') {
                newWord.append("FF");
            } else {
                newWord.append(symbol);
            }
        }

        word = newWord.toString();
    }

    public void paint(Graphics g) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == 1) {
                    g.fillRect(j, i, RECTANGLE_SIZE, RECTANGLE_SIZE);
                }
            }
        }
    }

    private void algorithm() {
        double length = INITIAL_LENGTH;
        double x = 50; // start x
        double y = HEIGHT - 150; // start y
        double angle = 25.0;

        Stack<Position> positionStack = new Stack<>();

        for (char symbol : word.toCharArray()) {
            switch (symbol) {
                case 'F':
                    double x2 = x + length * Math.cos(Math.toRadians(angle));
                    double y2 = y - length * Math.sin(Math.toRadians(angle));
                    map[(int) y][(int) x] = 1;
                    x = x2;
                    y = y2;
                    break;
                case '+':
                    angle += ANGLE;
                    break;
                case '-':
                    angle -= ANGLE;
                    break;
                case '[':
                    positionStack.push(new Position(x, y, angle));
                    break;
                case ']':
                    if (!positionStack.isEmpty()) {
                        Position position = positionStack.pop();
                        x = position.getX();
                        y = position.getY();
                        angle = position.getAngle();
                    }
                    break;
            }
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        iteration++;
        try {
            generateWord();
            algorithm();
            repaint();
            if (iteration == ITERATIONS) {
                timer.stop();
            }
        }catch (ArrayIndexOutOfBoundsException exception){
            timer.stop();
        }
    }
}