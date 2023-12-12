## Algoritmo: Aumento Salarial(FOR)
# Dev:Ana Paula
# Data: 12.12.22

SalarioInicial = 1000
SalarioAtualizado = 0.00
AnoInicial = 2000
AnoFinal = 2018
ReajustePerc = 1.5

print("Programa para calcular Percentuais de reajuste e as atualizações salariais entre os anos 2001 e 2017")

for i in range(AnoInicial, AnoFinal, 1):
    if i == 2000:
        print("O salário no ano", i, "era de:", "R$", SalarioInicial)
    elif i == 2001:
        SalarioAtualizado = SalarioInicial * (1 + (ReajustePerc/100))
        print("No ano", i, "O Reajuste aplicado foi de:", ReajustePerc, "%", "e o salário era de R$", SalarioAtualizado)
    else:
        ReajustePerc = ReajustePerc * 2
        SalarioAtualizado = SalarioAtualizado * (1 + (ReajustePerc/100))
        print("No ano", i, "O Reajuste aplicado foi de:", ReajustePerc, "%", "e o salário foi de R$", SalarioAtualizado)


