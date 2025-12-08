#include "Calculadora.hpp"

//cria os componentes e os vínculos (via lista de inicialização)
Calculadora::Calculadora() : 
    dados(), 
    interface(), 
    controle(interface, dados) 
{
}

Calculadora::~Calculadora()
{
}

void Calculadora::funcionar()
{
  interface.mostraBoasVindas();
  dados.reset();
  controle.executar();
}