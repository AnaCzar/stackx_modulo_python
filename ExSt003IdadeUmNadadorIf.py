# Algoritmo: Idade de um Nadador(IF)
# Dev:Ana Paula
# Data: 25.11.22

Idade = int(input("Qual a idade (completa) do nadador?"))

if Idade < 5:
    Categoria = "Não há Categoria cadastrada!!"
elif Idade >= 5 and Idade <= 7:
    Categoria = "Infantil"
elif Idade >= 8 and Idade <= 10:
    Categoria = "Juvenil"
elif Idade >= 11 and Idade <= 15:
    Categoria = "Adolescente"
elif Idade >= 16 and Idade <= 30:
    Categoria = "Adulto"
else:
    Categoria = "Senior"

print("A idade digitada foi: ", Idade, " anos. A categoria para esta idade é :", Categoria )
