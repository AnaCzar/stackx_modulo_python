# Algotritmo: Tres Valores em Ordem(IF)
# Dev:Ana Paula
# Data: 05.12.22


NumLado = int(input("Digite o Número de lados para o Poligono Regular(de 3 a 5)"))
MedLado = float(input("Digite as Medidas dos lados do Poligono Regular(em cm)"))

if NumLado == 3:
    Area = ((MedLado * MedLado) * 1.7) / 4
    print("O Poligono é um triângulo e sua área é :", Area, "cm²")
elif NumLado == 4:
    Area = MedLado * MedLado
    print("O Poligono é um quadrado e sua área é :", Area, "cm²")
elif NumLado == 5:
    print("O Poligono é um pentágono")
elif NumLado < 3:
    print("Você digitou Numero de lados inferior a 3, portanto: Não é um POLIGONO")
else:
    print("Você digitou Numero de lados superior a 5, portanto: POLÍGONO NÃO IDENTIFICADO")

print("Fim do programa !")
