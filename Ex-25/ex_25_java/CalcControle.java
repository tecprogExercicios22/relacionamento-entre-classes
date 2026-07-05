public class CalcControle {
    private CalcDados dados;
    private CalcInterface inteface;

    public CalcControle() {
        this.inteface = new CalcInterface();
        this.dados = new CalcDados();
    }

    public CalcControle(CalcInterface calcInterface, CalcDados calcDados) {
        this.inteface = calcInterface;
        this.dados = calcDados;
    }

    public void executar() {
        // Carregamos os dados
        this.dados.setOperando(1, this.inteface.recebeOperando(1));
        // Loop da calculadora
        while (this.dados.getOperacao() != 's') {
            this.dados.setOperando(2, this.inteface.recebeOperando(2));
            this.dados.setOperacao(this.inteface.recebeOperacao());

            // valida operacao
            if (this.dados.getOperacao() != 's') {
                // Executamos a operacao
                double resultado = this.operar(this.dados.getOperando(1), this.dados.getOperando(2), this.dados.getOperacao());
                // Mostramos o resultado
                this.inteface.mostraResultado(resultado);
                // Armazena resultado como primeiro operando e volta para o segundo passo
                this.dados.setOperando(1, resultado);
            } else {
                // Caso operação == s, finaliza a calculadora
                System.out.print("Calculadora Finalizada!");
                System.exit(0);
            }
        }
    }

    private double operar(double n1, double n2, char operacao) {
        switch (operacao) {
        case '*':
            return n1 * n2;
        case '/':
            return n1 / n2;
        case '-':
            return n1 - n2;
        case '+':
            return n1 + n2;
        case 's':
            return 0;
        default:
            System.out.println("Operação " + operacao + " inválida");
            System.exit(1);
            return 0;
        }
    }
}
