public class Calculadora {
    // Composição: A Calculadora possui (é dona de) Dados, Interface e Controle
    private CalcDados dados;
    private CalcInterface interface_;
    private CalcControle controle;

    // cria os componentes e os vínculos (via lista de inicialização)
    public Calculadora() {
        this.dados = new CalcDados();
        this.interface_ = new CalcInterface();
        this.controle = new CalcControle(this.interface_, this.dados);
    }

    public void funcionar() {
        this.interface_.mostraBoasVindas();
        this.dados.reset();
        this.controle.executar();
    }
}
