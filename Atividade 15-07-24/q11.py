# 11. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 < num2:
    print(f"Intervalo entre {num1} e {num2}:") 
    for entre in range(num1 + 1, num2):
        print(entre) 
elif num1 > num2:
    print(f"Intervalo entre {num1} e {num2}:")
    for entre in range(num1 - 1, num2, -1):
        print(entre) 
