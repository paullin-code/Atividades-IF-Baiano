# 10.Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo(F/M): ").upper()
    e_civil = input("Digite seu estado civil (S - Solteiro | C - Casado | V - Viúvo | D - Divorciado): ").upper()
    if len(nome) < 3:
        print("Erro! Nome menor que 3 caracteres!")
        continue
    elif 0 > idade > 150:
        print("Erro! Idade menos que 0 ou maior que 150!")
        continue 
    elif salario < 0:
        print("Erro! Salário menor que 0!")
        continue
    elif sexo != "F" and sexo != "M":
        print("Erro! Sexo inválido!")
        continue
    elif e_civil != "S" and e_civil != "C" and e_civil != "V" and e_civil != "D":
        print("Erro! Estado Civil inválido!")
    else:
        print("Tudo correto!")
        break