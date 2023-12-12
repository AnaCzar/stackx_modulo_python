# Algoritmo: Gratificação de nata(IF)
# Dev:Ana Paula
# Data: 23.11.22

HorasExtas = float(input("Quantas Horas Extras realizou o colaborador ?"))
HorasFaltas = float(input("Quantas Horas Faltas teve o colaborador?"))

MinutosTotais = (HorasExtas * 60) -(2/3*(HorasFaltas * 60))

if MinutosTotais>=2401:
    Premio=500.00
    print("O total é de : ", MinutosTotais, " minutos e o valor do Premio é de R$", Premio)
elif MinutosTotais>=1801 and MinutosTotais<2401:
    Premio = 400.00
    print("O total é de : ", MinutosTotais, " minutos e o valor do Premio é de R$", Premio)
elif MinutosTotais>1201 and MinutosTotais<1801:
    Premio = 300.00
    print("O total é de : ", MinutosTotais, " minutos e o valor do Premio é de R$", Premio)
elif MinutosTotais>600 and MinutosTotais<=1201:
    Premio = 200.00
    print("O total é de : ", MinutosTotais, " minutos e o valor do Premio é de R$", Premio)
elif MinutosTotais <= 600:
    Premio=100.00
    print("O total é de : ", MinutosTotais, " minutos e o valor do Premio é de R$", Premio)
