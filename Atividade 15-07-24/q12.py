#12.Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

lista = []
while True:
    lista.append(float(input("Digite um número: ")))
    continuar = input("Deseja continuar (S/N): ").upper()
    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        print("Reposta inválida!")
        continue
print(f"""Menor Valor: {min(lista)}
Maior Valor: {max(lista)}
Soma dos valores: {sum(lista)}""")