# Algoritmo: Numero Maior(IF)
# Dev:Ana Paula
# Data: 02.12.22
Num1 = 0
Num2 = 0

while Num1 == Num2:
    Num1 = float(input("Digite o PRIMEIRO Número : "))
    Num2 = float(input("Digite o SEGUNDO Número : "))

if Num1 > Num2 :
    print("O maior número é O PRIMEIRO digitado:", Num1)
else:
    print("O maior número é O SEGUNDO digitado:", Num2)