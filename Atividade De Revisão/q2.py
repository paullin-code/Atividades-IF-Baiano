# 2. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ["a","e","i","o","u"]
conso = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'k', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'y']
letra = input("Digite uma letra: ")
if letra.lower() in vogal:
    print(f"A letra ({letra}) é uma vogal!")
elif letra.lower() in conso:
    print(f"A letra ({letra}) é uma consoante!")
else:
    print(f"A letra ({letra}) não é uma vogal ou consoante!")