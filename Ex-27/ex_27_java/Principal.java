import java.util.Scanner;

public class Principal {

    private Triangulo triang = new Triangulo(new Ponto(0,0),new Ponto(0,0),new Ponto(0,0));

    public void exec() {
        Scanner sc = new Scanner(System.in);
        float x = 0, y = 0;

        System.out.println("Criando um triângulo...");
        System.out.print("Digite a coordenada do primeiro vértice no formato (x.x,y.y): ");
        String entrada = sc.nextLine();
        float[] v1 = parseCoordenada(entrada);
        triang.setVertice1(v1[0], v1[1]);

        System.out.print("Digite a coordenada do segundo vértice no formato (x.x,y.y): ");
        entrada = sc.nextLine();
        float[] v2 = parseCoordenada(entrada);
        triang.setVertice2(v2[0], v2[1]);

        System.out.print("Digite a coordenada do terceiro vértice no formato (x.x,y.y): ");
        entrada = sc.nextLine();
        float[] v3 = parseCoordenada(entrada);
        triang.setVertice3(v3[0], v3[1]);

        triang.imprimirPerimetro();
    }

    // Função auxiliar para converter "(x,y)" em float[]
    private float[] parseCoordenada(String s) {
        s = s.replace("(", "").replace(")", "");
        String[] partes = s.split(",");
        float x = Float.parseFloat(partes[0].trim());
        float y = Float.parseFloat(partes[1].trim());
        return new float[]{x, y};
    }

    public static void main(String[] args) {
        new Principal().exec();
    }
}