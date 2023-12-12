# Algoritmo: Idade e Peso(IF)
# Dev:Ana Paula
# Data: 23.11.22

Idade = int(input("Qual a idade? (idade completa)"))
Peso = float(input("Qual o peso? (em Kg)"))

if Idade < 20:
    if Peso <= 60:
        Risco = 9
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
    elif Peso > 60 and Peso <= 90:
        Risco = 8
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
    else:
        Risco = 7
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
elif Idade >= 20 and Idade <= 50:
    if Peso <= 60:
        Risco = 6
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
    elif Peso > 60 and Peso <= 90:
        Risco = 5
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
    else:
        Risco = 4
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
elif Idade >= 50:
     if Peso <= 60:
        Risco = 3
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
     elif Peso > 60 and Peso <= 90:
        Risco = 2
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)
     else:
        Risco = 1
        print("A classe de risco para", Peso, " Kg e idade: ", Idade, " anos é :", Risco)

