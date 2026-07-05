public class Principal {
    public static void main(String[] args) {

        // Criamos o objeto universidade
        Universidade uni = new Universidade();
        uni.setNome("UTFPR");

        // Adicionamos os departamentos à universidade
        Departamento dainf = new Departamento();
        dainf.setNome("DAINF");      // Colocamos o nome do departamento
        dainf.setUniversidade(uni);  // Fornecemos a universidade afiliada
        uni.addDepartamento(dainf);  // Adicionamos o departamento à universidade

        Departamento damat = new Departamento();
        damat.setNome("DAMAT");      // Colocamos o nome do departamento
        damat.setUniversidade(uni);  // Fornecemos a universidade afiliada
        uni.addDepartamento(damat);  // Adicionamos o departamento à universidade

        Departamento daeln = new Departamento();
        daeln.setNome("DAELN");      // Colocamos o nome do departamento
        daeln.setUniversidade(uni);  // Fornecemos a universidade afiliada
        uni.addDepartamento(daeln);  // Adicionamos o departamento à universidade

        Departamento dafis = new Departamento();
        dafis.setNome("DAFIS");      // Colocamos o nome do departamento
        dafis.setUniversidade(uni);  // Fornecemos a universidade afiliada
        uni.addDepartamento(dafis);  // Adicionamos o departamento à universidade

        // Finalmente imprimimos os departamentos associados à universidade
        uni.imprimeDepartamentos();
    }
}
