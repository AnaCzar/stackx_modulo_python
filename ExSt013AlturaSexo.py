# Algotritmo: Altura e Sexo (IF)
# Dev:Ana Paula
# Data: 05.12.22


Sexo = int(input('Digite o sexo : 1- Feminino ou 2-Masculino'))
Altura = float(input('Digite sua Altura (em metros)'))
if Sexo == 1:
    PesoIdeal = (62.1*Altura) - 44.7
else:
    PesoIdeal = (72.7 * Altura) - 58

print("O seu peso ideal é :", PesoIdeal, "Kg")


