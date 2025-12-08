#include "CalcDados.hpp"

CalcDados::CalcDados() : n1(0),
                         n2(0),
                         operacao('\0')
{
}

CalcDados::~CalcDados()
{
}

void CalcDados::setOperando(const int &i, const double &valor)
{
  switch (i)
  {
  case 1:
    this->n1 = valor;
    break;
  case 2:
    this->n2 = valor;
    break;
  default:
    break;
  }
}

const double &CalcDados::getOperando(const int &i) const
{
  switch (i)
  {
  case 1:
    return this->n1;
  case 2:
    return this->n2;
  default:
    cout << "Operando " << i << " inválido" << endl;
    exit(1);
  }
}

void CalcDados::setOperacao(const char &operacao)
{
  this->operacao = operacao;
}

const char &CalcDados::getOperacao() const
{
  return this->operacao;
}


void CalcDados::reset()
{
  this->n1 = 0;
  this->n2 = 0;
  this->operacao = '\0';
}