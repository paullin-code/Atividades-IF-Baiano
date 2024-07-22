# 9. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


while True:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if senha != usuario:
        print("Login com sucesso!")
        break
    else:
        print("Usuário e senha não podem ser iguais!")
        continue