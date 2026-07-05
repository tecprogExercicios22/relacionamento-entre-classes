import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class CalcInterface {
    // Inicializamos o vetor com as operacoes válidas
    private static final List<Character> OPERACOES_VALIDAS = Arrays.asList('+', '-', '*', '/', 's');
    private static Scanner scanner = new Scanner(System.in);

    public CalcInterface() {
    }

    public double recebeOperando(int i) {
        System.out.println("Insira o operando " + i);
        double operando = scanner.nextDouble();
        return operando;
    }

    public char recebeOperacao() {
        char operacao;
        do {
            System.out.println("Insira uma operacao:");
            operacao = scanner.next().charAt(0);
        } while (!CalcInterface.isOperacaoValida(operacao));
        return operacao;
    }

    public void mostraResultado(double resultado) {
        System.out.println("Resultado: " + resultado);
    }

    private static boolean isOperacaoValida(char operacao) {
        int size = CalcInterface.OPERACOES_VALIDAS.size();
        for (int i = 0; i < size; i++)
            if (CalcInterface.OPERACOES_VALIDAS.get(i) == operacao)
                return true;
        return false;
    }

    public void mostraBoasVindas() {
        System.out.println("--------------------------------");
        System.out.println("   Bem-vindo à Calculadora OO   ");
        System.out.println("--------------------------------");
    }
}
