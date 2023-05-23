class Position {
    private final double x;
    private final double y;
    private final double angle;

    public Position(double x, double y, double angle) {
        this.x = x;
        this.y = y;
        this.angle = angle;
    }

    public double getX() {
        return x;
    }

    public double getAngle(){return angle;}
    public double getY() {return y;}
}