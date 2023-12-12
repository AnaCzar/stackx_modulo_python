# Algotritmo: Compra de Maçãs(IF)
# Dev:Ana Paula
# Data: 03.12.22

ValorAtacado = 0.25
ValorVarejo = 0.30

NumeroMaca = int(input("Qual a quantidade de maçãs desejada?"))

if NumeroMaca >= 12:
    ValorTotal = NumeroMaca * ValorAtacado
else:
    ValorTotal = NumeroMaca * ValorVarejo

print("O Valor Total da(s) ", NumeroMaca, "Maçã(s) é de R$ ", ValorTotal)
print("Fim do programa !")

