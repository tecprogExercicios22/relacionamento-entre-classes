class Triangulo {
    private Ponto vertice1;
    private Ponto vertice2;
    private Ponto vertice3;
    
    // Construtor
    public Triangulo(Ponto v1, Ponto v2, Ponto v3) {
        this.vertice1 = v1;
        this.vertice2 = v2;
        this.vertice3 = v3;
    }

    public void setVertice1(double x, double y){
        vertice1.setPonto(x,y);
    }
    public void setVertice2(double x, double y){
        vertice2.setPonto(x,y);
    }
    public void setVertice3(double x, double y){
        vertice3.setPonto(x,y);
    }

    public Ponto getPVertice1() {
        return vertice1;
    }

    public Ponto getPVertice2() {
        return vertice2;
    }

    public Ponto getPVertice3() {
        return vertice3;
    }

    public boolean testeTriangulo() {
        if (vertice1.getX() == vertice2.getX() && vertice1.getX() == vertice3.getX())
            return false;
        if (vertice1.getY() == vertice2.getY() && vertice1.getY() == vertice3.getY())
            return false;
        return true;
    }

    public double calcDist(Ponto p1, Ponto p2) {
        return Math.sqrt( (p1.getX() - p2.getX()) * (p1.getX() - p2.getX()) + (p1.getY() - p2.getY()) * (p1.getY() - p2.getY()));
    }


    public void imprimirPerimetro() {
        float perimetro = 0;

        if (!testeTriangulo()) {
            System.out.println("Os vértices não formam um triangulo, pois são colineares.\n");
            return;
        }

        perimetro += calcDist(vertice1, vertice2);
        perimetro += calcDist(vertice2, vertice3);
        perimetro += calcDist(vertice1, vertice3);

        System.out.println("O perimetro do triangulo é " + perimetro);
    }
}
