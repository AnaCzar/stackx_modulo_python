# Algoritmo: Salario Bruto(IF)
# Dev:Ana Paula
# Data: 25.11.22   // considerei as faixas salariais exatamente como o enuanciado - como se fosse prova

Imposto = 0.07
SalarioBruto = float(input("Qual o salário Bruto do Colaborador?"))

if SalarioBruto <= 350:
    Gratificacao = 100
elif SalarioBruto >= 351 and SalarioBruto <= 600:
    Gratificacao = 75
elif SalarioBruto >= 601 and SalarioBruto <= 900:
    Gratificacao = 50
else:
    Gratificacao = 35

ValorReceber = SalarioBruto + Gratificacao - (SalarioBruto*Imposto)
print("O salário Bruto digitado foi R$ ", SalarioBruto, "A gratificação é de R$ ", Gratificacao,
      " E o valor total a receber é R$ ", ValorReceber, "Deduzido de imposto ( R$", SalarioBruto*Imposto, " )")