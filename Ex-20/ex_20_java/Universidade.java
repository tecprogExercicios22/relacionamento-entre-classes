import java.util.LinkedList;
import java.util.List;

public class Universidade {
    private String nome;
    private List<Departamento> lDepartamentos;
    private int nDepartamentos;
    private static final int MAX_DEPARTAMENTOS = 50;

    // Construtora & Destrutora
    public Universidade() {
        this.nome = "";
        this.lDepartamentos = new LinkedList<Departamento>();
        this.nDepartamentos = 0;
    }

    // Métodos
    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void addDepartamento(Departamento departamento) {
        if (this.nDepartamentos < MAX_DEPARTAMENTOS) {
            this.lDepartamentos.add(0, departamento);
            this.nDepartamentos++;
        } else {
            System.err.println("Máximo 50 departamentos");
            System.exit(1);
        }
    }

    public void imprimeDepartamentos() {
        System.out.println("Departamentos: ");
        for (Departamento departamento : this.lDepartamentos) {
            System.out.println("\t -> " + departamento.getNome());
        }
    }
}
