# Algoritmo: Receber Nomes e Salários(While)
# Dev:Ana Paula
# Data: 01.12.22

RendimCaderneta = 1.02
RendimRendaFixa = 1.05
Laco1 = True
Mes = 1

while Laco1 :
    Nome = str(input("Qual o nome do funcionário (João ou Carlos)?"))
    if Nome == "João" or Nome == "Carlos":
        Laco1 = False
    else:
        print("Você deve digitar/escolher entre João e Carlos")
        Laco1 = True


Salario = float(input("Qual o salário?"))

if Nome == "João":
    ValorAcJoao = Salario * RendimRendaFixa
    ValorAcCarlos = (Salario * 3) * RendimCaderneta

else:
    ValorAcJoao = (Salario/3) * RendimRendaFixa
    ValorAcCarlos = Salario * RendimCaderneta

while ValorAcJoao < ValorAcCarlos:
    Mes = Mes + 1
    ValorAcJoao = ValorAcJoao * RendimRendaFixa
    ValorAcCarlos = ValorAcCarlos * RendimCaderneta

print("O Valor pertencente a João R$", ValorAcJoao, " alcancou o valor de Carlos: R$ ", ValorAcCarlos,
      " em ", Mes, " Meses")








