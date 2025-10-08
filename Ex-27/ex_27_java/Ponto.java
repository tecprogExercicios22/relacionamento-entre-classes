class Ponto {
    private double x;
    private double y;
    
    // Construtor
    public Ponto(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    // Getters
    public double getX() {
        return x;
    }
    
    public double getY() {
        return y;
    }

    public void setPonto(double x, double y){
        this.x = x;
        this.y = y;
    }
    
    // Calcula a distância entre este ponto e outro ponto
    public double calcularDistancia(Ponto outro) {
        double dx = this.x - outro.x;
        double dy = this.y - outro.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
}
