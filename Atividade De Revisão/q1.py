# 1. Crie um programa em Python que peça dois números ao usuário. Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão, exponenciação e resto da divisão do primeiro número pelo segundo.


n1 = float(input("Digite o primerio número: "))
n2 = float(input("Digite o segundo número: "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
exp = n1 ** n2
rest = n1 % n2
print(f"Números: {n1} / {n2} \nSoma: {soma} \nSubtração: {sub} \nMultiplicação: {mult} \nExponenciação: {exp} \nResto: {rest}")