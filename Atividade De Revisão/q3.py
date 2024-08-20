# 3. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turnos = "M = Matutino \nV = Vespertino \nN = Noturno"
turno = input(f"Turnos:\n{turnos}\nDigite o seu turno: ")
if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa Tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")