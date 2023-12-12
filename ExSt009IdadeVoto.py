# Algoritmo: Idade para Voto(IF)
# Dev:Ana Paula
# Data: 02.12.22

AnoAtual = 2022
AnoNasc = 9999

while AnoNasc > AnoAtual:
    AnoNasc = int(input("Digite o ano de nascimento :"))

Id = AnoAtual - AnoNasc
if 18 <= Id < 70:
    print("O voto com ", Id, " anos é obrigatório")
elif 16 <= Id < 18 and Id >= 70:
    print("O voto com ", Id, " anos é facultativo")
else:
    print("O voto com ", Id, " anos não é permitido")