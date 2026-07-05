import java.util.Scanner;

public class Principal {
    private Poligono polig;
    private Scanner scanner;

    public Principal() {
        polig = new Poligono();
        scanner = new Scanner(System.in);
        exec();
    }

    private void exec() {
        int opcao = 1;
        while (opcao != 0) {
            System.out.println("\n=========================================");
            System.out.print("1 - Incluir ponto no poligono\n2 - Remover ponto do Poligono\n3 - Imprimir perimetro do poligono\n4 - Imprimir todos os prontos\n0 - Sair\n");
            System.out.print("=========================================\nSelecione uma opçao: ");
            opcao = Integer.parseInt(scanner.nextLine().trim());
            System.out.println("=========================================");
            switch (opcao) {
            case 1:
                lerPonto();
                break;
            case 2:
                removerPonto();
                break;
            case 3:
                imprimirPerimetro();
                break;
            case 4:
                polig.imprimirTodosPontos();
                break;
            default:
                break;
            }
        }
    }

    private void lerPonto() {
        float x = 0, y = 0;
        System.out.print("\nDigite a coordenada do vertice no formato(x.x, y.y) :");
        String entrada = scanner.nextLine().trim();
        entrada = entrada.replace("(", "").replace(")", "");
        String[] partes = entrada.split(",");
        x = Float.parseFloat(partes[0].trim());
        y = Float.parseFloat(partes[1].trim());

        Ponto tmp = new Ponto();
        tmp.setPonto(x, y);

        polig.setVertice(tmp);
    }

    private void imprimirPerimetro() {
        polig.imprimirPerimetro();
    }

    private void removerPonto() {
        int x = 0;

        polig.imprimirTodosPontos();
        System.out.print("\nQual ponto deseja remover? ");

        x = Integer.parseInt(scanner.nextLine().trim());

        polig.removerPonto(polig.get(x));
    }
}
