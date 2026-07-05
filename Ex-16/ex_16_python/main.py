from Cliente import Cliente
from Conta import Conta


def main():
    # Criamos os clientes
    clienteA = Cliente("Ned Stark", "000.000.000-00")
    clienteB = Cliente("John Snow", "111.000.000-00")
    # Criamos as contas
    contaA = Conta(0)
    contaB = Conta(1)
    contaC = Conta(2)
    # Adicionamos um valor inicial as contas
    contaA.depositar(10.0)
    contaB.depositar(20.0)
    contaC.depositar(50.0)
    # Associamos a contaA com o clienteA
    contaA.setTitular(clienteA)
    clienteA.adicionarConta(contaA)
    # Adicionamos a contaC para o clienteA
    clienteA.adicionarConta(contaC)
    # Associamos a contaB com o clienteB
    contaB.setTitular(clienteB)
    clienteB.adicionarConta(contaB)
    # Adicionamos a contaC para o clienteB
    clienteB.adicionarConta(contaC)
    # Depositamos nas contas por meio dos clientes
    clienteA.aplicarRecursos(100.0)
    clienteB.aplicarRecursos(100.0)
    # Geramos os relatorios dos clientes
    print(clienteA.gerarRelatorio())
    print(clienteB.gerarRelatorio())
    return 0


if __name__ == "__main__":
    main()
