# Algotritmo: Tres Valores em Ordem(IF)
# Dev:Ana Paula
# Data: 04.12.22

PrimeiroNum = int(input("Digite o primeiro Número:"))
SegundoNum = int(input("Digite o segundo Número:"))
while SegundoNum == PrimeiroNum:
    print("Os valores não podem ser iguais!")
    SegundoNum = int(input("Digite o segundo Número:"))

TerceiroNum = int(input("Digite o terceiro Número:"))
while TerceiroNum == PrimeiroNum or TerceiroNum == SegundoNum:
    print("Os valores não podem ser iguais!")
    TerceiroNum = int(input("Digite o terceiro Número:"))

ListaNum = [PrimeiroNum, SegundoNum, TerceiroNum]
ListaNum.sort()
print(ListaNum)
print("Fim do Programa!!")












