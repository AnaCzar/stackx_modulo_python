# Algotritmo: Triangulo (IF)
# Dev:Ana Paula
# Data: 06.12.22

MedLado1 = float(input("Digite a medida do 1º lado do triângulo: "))
MedLado2 = float(input("Digite a medida do 2º lado do triângulo: "))
MedLado3 = float(input("Digite a medida do 3º lado do triângulo: "))

if MedLado1 == MedLado2 == MedLado3:
    Triangulo = "Equilátero"
elif MedLado1 != MedLado2 != MedLado3 != MedLado1:
    Triangulo = "Escaleno"
else:
    Triangulo = "Isóceles"

print("O Triangulo é ", Triangulo)
