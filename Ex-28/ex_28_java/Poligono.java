import java.util.ArrayList;
import java.util.Iterator;

public class Poligono {
    private ArrayList<Ponto> pontos;

    public Poligono() {
        pontos = new ArrayList<Ponto>();
    }

    public void setVertice(Ponto pPonto) {
        if (pPonto == null) {
            System.out.println("Ponteiro NULL ao incluir novo vertice em Poligono");
            System.exit(1);
        }

        pontos.add(pPonto);
    }

    /* Calcula e imprime o perimetro do Poligono */
    public void imprimirPerimetro() {
        float perimetro = 0;

        /* Soma todas as distancias entre os pontos */
        for (int i = 0; i < getQuantidadePontos() - 1; i++) {
            perimetro += calcDist(pontos.get(i), pontos.get(i + 1));
        }
        /* Falta somar a distancia do ultimo ponto para o primeiro */
        if (getQuantidadePontos() - 1 > 1)
            perimetro += calcDist(pontos.get(getQuantidadePontos() - 1), pontos.get(0));

        System.out.println("O perimetro do Poligono é " + perimetro);
    }

    /* Acessa o vetor retornando o Ponto correspondente ao indice i do vetor */
    public Ponto get(int i) {
        if (i < 0 || i >= getQuantidadePontos()) {
            System.out.println("Vector out of range.");
            System.exit(8);
        }

        return pontos.get(i);
    }

    /* Pega a quantiade de pontos */
    public int getQuantidadePontos() {
        return pontos.size();
    }

    /* Calcula a distancia entre dois pontos */
    private float calcDist(Ponto p1, Ponto p2) {
        return (float) Math.sqrt((p1.getX() - p2.getX()) * (p1.getX() - p2.getX()) + (p1.getY() - p2.getY()) * (p1.getY() - p2.getY()));
    }

    /* Remover ponto do poligono */
    public void removerPonto(Ponto pPonto) {
        Iterator<Ponto> itr = pontos.iterator();

        Ponto tmp = null;
        while (itr.hasNext()) {
            tmp = itr.next();
            if (tmp == pPonto) {
                if (pPonto != null) {
                    itr.remove();
                }
                return;
            }
        }
    }

    /* Imprime todos os pontos e seu indice */
    public void imprimirTodosPontos() {
        Ponto tmp = null;
        System.out.println("Imprimindo pontos poligono: \nindice - (x,y)");

        if (getQuantidadePontos() < 1) {
            System.out.println("Nao ha pontos nesse poligono!");
            return;
        }

        for (int i = 0; i < getQuantidadePontos(); i++) {
            tmp = pontos.get(i);
            if (tmp != null)
                System.out.println(i + " - (" + tmp.getX() + "," + tmp.getY() + ")");
            else
                System.out.println(i + " - sem coordenadas");
        }
    }
}
