def inderteminado():
    resp = "Sim"
    numero = 0
    while resp == "Sim":
        n1 = int(input("Digite um numero: "))
        resp = input("Quer adicionar mais numeros? ").capitalize()
        numero += n1
    print(f"Essa é a soma de todos os números adicionados: {numero}")

inderteminado()
        

