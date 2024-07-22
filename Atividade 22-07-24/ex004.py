def real_dolar(real):
    dolar = 0.18
    resul = real * dolar
    print(f"R$ {real} são equivalentes a $ {resul:.2f}")

def real_euro(real):
    euro = 0.16
    resul = real * euro
    print(f"R$ {real} são equivalentes a $ {resul:.2f}")

def real_peso_arg(real):
    peso_arg = 0.0061
    resul = real * peso_arg
    print(f"R$ {real} são equivalentes a $ {resul:.2f}")

real = float(input("Digite o valor em R$: "))
real_dolar(real)
real_euro(real)
real_peso_arg(real)