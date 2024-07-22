# 7. Para votar, você deve ter entre 18 anos e menos de 65 anos. Escreva um programa que pergunte sua idade e diga se você é obrigado a votar ou não.

idade = int(input("Digite sua idade: "))
if 17 < idade < 66:
    print("Você é obrigado a votar!")
elif idade < 0:
    print("Idade inválida!")
else:
    print("Você não é obrigado a votar!")