public class Departamento {
    private String nome;
    private Universidade universidade;

    public Departamento() {
        this.nome = "";
        this.universidade = null;
    }

    public Departamento(String nome, Universidade universidade) {
        this.nome = nome;
        this.universidade = universidade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return this.nome;
    }

    public void setUniversidade(Universidade universidade) {
        this.universidade = universidade;
    }

    public Universidade getUniversidade() {
        return this.universidade;
    }
}
