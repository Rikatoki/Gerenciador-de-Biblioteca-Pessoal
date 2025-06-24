from livro import Livro
from usuario import Usuario
class Dados:
    def __init__(self):
        self.livros: list[Livro] = []
        self.usuarios: list[Usuario] = []