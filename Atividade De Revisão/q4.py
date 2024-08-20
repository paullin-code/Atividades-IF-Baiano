# 4. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


data = input("Formato: dd/mm/aaaa\nDigite uma data: ")
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])
if ano > 0 and dia > 0 and 0 < mes < 13:
    if mes == 2 and ano%4 == 0:
        if 0 < dia < 30:
            print("É uma data válida!")
        else:
            print("É uma data inválida!")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 0 < dia < 31:
            print("É uma data válida!")
        else:
            print("É uma data inválida!")
    elif (0 < mes < 13) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if 0 < dia < 32:
            print("É uma data válida!")
        else:
            print("É uma data inválida!")
else:
    print("É uma data inválida!")