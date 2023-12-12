# Algoritmo: Validar Senha(IF)
# Dev:Ana Paula
# Data: 03.12.22

Senha = 9999

while Senha != 1234:
    Senha = int(input("Digite sua senha de 4 digitos"))

    if Senha == 1234:
        print("Acesso Permitido")

    else:
        print("Acesso Negado")

print("Fim do programa !")
