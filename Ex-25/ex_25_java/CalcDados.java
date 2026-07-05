public class CalcDados {
    private double n1, n2;
    private char operacao;

    public CalcDados() {
        this.n1 = 0;
        this.n2 = 0;
        this.operacao = '\0';
    }

    public void setOperando(int i, double valor) {
        switch (i) {
        case 1:
            this.n1 = valor;
            break;
        case 2:
            this.n2 = valor;
            break;
        default:
            break;
        }
    }

    public double getOperando(int i) {
        switch (i) {
        case 1:
            return this.n1;
        case 2:
            return this.n2;
        default:
            System.out.println("Operando " + i + " inválido");
            System.exit(1);
            return 0;
        }
    }

    public void setOperacao(char operacao) {
        this.operacao = operacao;
    }

    public char getOperacao() {
        return this.operacao;
    }

    public void reset() {
        this.n1 = 0;
        this.n2 = 0;
        this.operacao = '\0';
    }
}
