from CalcControle import CalcControle
from CalcDados import CalcDados
from CalcInterface import CalcInterface


def main():
    # Instanciamos a interface e memoria da calculadora
    interface = CalcInterface()
    dados = CalcDados()
    # Criamos o controle da calculadora utilizando a interface e memoria
    controle = CalcControle(interface, dados)
    # Executamos
    controle.executar()
    return 0


if __name__ == "__main__":
    main()
