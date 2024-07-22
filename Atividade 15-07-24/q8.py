# 8. Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD. Escreva um programa que pergunta a situação do usuário (se é idoso, se é gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não.

situacoes = """I = Idoso
G = Gestante
P = PCD
N = Nenhum destes"""
situacao = input(f"{situacoes}\nQual a sua sitação: ").upper()
if situacao == "I" or situacao == "G" or situacao == "P":
    print("Você tem acesso a fila de prioridade!")
elif situacao == "N":
    print("Você não tem acesso a fila de prioridade!")
else:
    print("Erro!")