# Algoritmo: Empresa com 10 Funcionários(While)
# Dev:Ana Paula
# Data: 28.11.22

Contador = 1
Laco1 = True
Laco2 = True

while Contador <= 10:
    ValorHora = 0.00
    SalarMin = 450
    SalarInic = 0.00
    SalarFinal = 0.00
    AuxilioAlim = 0.00

    Cod = input("Digite o CODIGO do funcionário")
    NumHora = float(input("Digite a NUMERO DE HORAS TRABALHADAS do funcionário"))

    while Laco1:
        Turno = input("Digite o TURNO do funcionário")
        if Turno == "M" or Turno == "V" or Turno == "N":
            Laco1 = False
        else:
            print("Opção de TURNO digitado errado. Digite novamente!")
            continue
        break

    while Laco2:
        Categoria = input("Digite a CATEGORIA do funcionário")
        if Categoria =="O" or Categoria =="G":
            Laco2 = False
        else:
            print("Opção de CATEGORIA digitado errado. Digite novamente!")
            continue
        break

    if Categoria == "G" and Turno == "N":
        ValorHora = SalarMin * 0.18
    elif Categoria == "G" and Turno == "M" or Turno == "v":
        ValorHora = SalarMin * 0.15
    elif Categoria == "O" and Turno == "N":
        ValorHora = SalarMin * 0.13
    else:
        ValorHora = SalarMin * 0.10

    SalarInic = NumHora*ValorHora

    if SalarInic < 300.00:
        AuxilioAlim = SalarInic*0.20
    elif SalarInic >= 300.00 and SalarInic < 600.00:
        AuxilioAlim = SalarInic*0.15
    else:
        AuxilioAlim = SalarInic*0.05

    SalarFinal = SalarInic + AuxilioAlim

    print("O funcionário", "\n codigo =", Cod, "\n Turno = ", Turno,"\n Categoria =", Categoria,
          " \n Tem o valor de Hora R$=",ValorHora, "\n Realizou =", NumHora, "Horas de trabalho",
          "\n O Salario inicial ficou em = R$",SalarInic,"\n O auxilio alimentação = R$",AuxilioAlim,
          "\n Totalizando R$", SalarFinal, "de salário.")

    Laco1 = True
    Laco2 = True
    Contador = Contador + 1






