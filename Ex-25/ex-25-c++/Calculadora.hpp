#ifndef C_CALCULADORA
#define C_CALCULADORA

#include "stdinc.hpp"
#include "CalcDados.hpp"
#include "CalcInterface.hpp"
#include "CalcControle.hpp"

class Calculadora
{
private:
  // Composição: A Calculadora possui (é dona de) Dados, Interface e Controle
  CalcDados dados;
  CalcInterface interface;
  CalcControle controle;

public:
  Calculadora();
  ~Calculadora();
  void funcionar();
};

#endif