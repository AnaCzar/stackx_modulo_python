# Algotritmo: Altura e Sexo (IF)
# Dev:Ana Paula
# Data: 06.12.22


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
print("O maior número digitado é :", ListaNum[2])






