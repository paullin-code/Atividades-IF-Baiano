# 5. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número: "))
if num == 2 or num == 3 or num == 5 or num == 7:
    print(f"O número ({num}) é primo!")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print(f"O número ({num}) não é primo!")
else:
    print(f"O número ({num}) é primo!")