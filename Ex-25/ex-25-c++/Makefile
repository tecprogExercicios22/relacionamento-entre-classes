# Definição do compilador e das flags
CC = g++
CFLAGS = -Wall -std=c++11

# Nome do executável final
TARGET = calculadora

# Objetos necessários para a compilação
OBJS = main.o Calculadora.o CalcControle.o CalcDados.o CalcInterface.o

# Regra padrão (executada ao digitar apenas 'make')
all: $(TARGET)

# Regra para ligar os objetos e gerar o executável
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Regras de compilação para cada arquivo objeto
main.o: main.cpp Calculadora.hpp stdinc.hpp
	$(CC) $(CFLAGS) -c main.cpp

Calculadora.o: Calculadora.cpp Calculadora.hpp CalcControle.hpp CalcDados.hpp CalcInterface.hpp stdinc.hpp
	$(CC) $(CFLAGS) -c Calculadora.cpp

CalcControle.o: CalcControle.cpp CalcControle.hpp CalcDados.hpp CalcInterface.hpp stdinc.hpp
	$(CC) $(CFLAGS) -c CalcControle.cpp

CalcDados.o: CalcDados.cpp CalcDados.hpp stdinc.hpp
	$(CC) $(CFLAGS) -c CalcDados.cpp

CalcInterface.o: CalcInterface.cpp CalcInterface.hpp stdinc.hpp
	$(CC) $(CFLAGS) -c CalcInterface.cpp

# Regra para limpar os arquivos gerados (objetos e executável)
# Use 'make clean' para executar
clean:
	rm -f $(OBJS) $(TARGET)