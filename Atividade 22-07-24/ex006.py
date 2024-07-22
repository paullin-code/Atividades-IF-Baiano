def notacao(horas):
    if 12 < horas < 24:
        hora_c = horas-12
        print(f"{hora_c}:{min}")
    elif 0 < horas < 13:
        hora_c = horas
        print(f"{hora_c}:{min}")
    else:
        print("erro!")

hora = input("Digite as horas: ")
horas = int(hora[:2])
min = int(hora[3:])
notacao(horas)