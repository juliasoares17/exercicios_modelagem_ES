class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True  

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
