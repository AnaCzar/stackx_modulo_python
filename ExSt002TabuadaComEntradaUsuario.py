## Algoritmo: Tabuada com Entrada de Usuário(FOR)
# Dev:Ana Paula
# Data: 13.12.22


Tab = int(input("Digite a Tabuada desejada(de 1 a 10):"))
for i in range(0, 11, 1):
    Result = Tab * i
    print(Tab, "X", i, "=", Result)

