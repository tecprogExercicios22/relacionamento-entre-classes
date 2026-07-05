public class Principal {
    public static void main(String[] args) {
        // Instanciamos a interface e memoria da calculadora
        CalcInterface interface_ = new CalcInterface();
        CalcDados dados = new CalcDados();
        // Criamos o controle da calculadora utilizando a interface e memoria
        CalcControle controle = new CalcControle(interface_, dados);
        // Executamos
        controle.executar();
    }
}
