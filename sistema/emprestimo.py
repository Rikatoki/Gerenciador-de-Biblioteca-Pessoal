from livro import Livro
from usuario import Usuario
from datetime import date
from json import load,dump
class Emprestimo:
    def __init__(self):
        self.emprestimos: list[list[Livro]] = []

    def cadastrar(self, usuario:Usuario, livro:Livro,data = date.today()):
        if not livro.emprestado:
            self.emprestimos.append([usuario, livro, data, False])
            livro.emprestado = True
            return f'Cadastro: Livro: {livro.titulo} emprestado ao {usuario.nome}, email: {usuario.email}.'
        else:
            return f'O livro {livro.titulo} não está disponível.'

    def devolucao(self, id_usuario:int, id_livro:int):
        for l in self.emprestimos:
            if id_usuario == l[0].id and id_livro == l[1].id:
                if not l[3]:
                    data = date.today()
                    l[3] = data
                    l[1].emprestado = False
                    return f'Livro devolvido com sucesso!'
                return f'Livro já foi devolvido!'
            return f'Não foi encontrado este registro.'
        
