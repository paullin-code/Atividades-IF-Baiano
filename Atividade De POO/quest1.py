class Livro():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    def exibir_detalhes(self):
        print(f"Nome do livro: {self.titulo}\nAutor do livro: {self.autor}\nAno de publicação: {self.ano_publicacao}")

titulo = input("Digite o titulo do livro: ")
autor = input("Digite o autor do livro: ")
ano_publicacao = int(input("Digite o ano de publicação do livro: "))

livro_1 = Livro(titulo, autor, ano_publicacao)
livro_1.exibir_detalhes()