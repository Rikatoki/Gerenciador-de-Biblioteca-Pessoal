import os
from json import load,dump
class Livro:
    livros: list['Livro'] = []
    
    def __init__(self, titulo:str, autor:str, ano:int, genero:str, id:int = None,emprestado:bool = False):
        Livro.carregar()
        if id is None:
            id = Livro.carregar_id() + 1
            Livro.salvar_id(id)
        self.id = id
        self.titulo = titulo.title().split()
        self.autor = autor.title().split()
        self.ano = ano
        self.genero = genero.title().split()
        self.emprestado = emprestado
        Livro.livros.append(self)
        Livro.salvar()
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "id": self.id,
            "emprestado": self.emprestado
        }
    
    @classmethod
    def from_dict(cls, data):
        livros = []
        for d in data:
            livro = cls.__new__(cls)
            livro.id = d["id"]
            livro.titulo = d["titulo"]
            livro.autor = d["autor"]
            livro.ano = d["ano"]
            livro.genero = d["genero"]
            livro.emprestado = d["emprestado"]
            livros.append(livro)
        return livros
    
    @classmethod
    def salvar(cls):
        livros = []
        for l in cls.livros:
            livros.append(l.to_dict())
        os.makedirs('dados', exist_ok=True)
        with open('dados/livros.json', 'w', encoding='utf-8') as arq:
            dump(livros, arq, indent=2)

    @classmethod
    def carregar(cls):
        if os.path.exists('dados/livros.json'):
            with open('dados/livros.json', 'r', encoding='utf-8') as arq:
                dados = load(arq)
            Livro.livros = Livro.from_dict(dados)

    @classmethod
    def carregar_id(cls):
        if os.path.exists('dados/livro_id.txt'):
            with open('dados/livro_id.txt','r') as f:
                return int(f.read())
        return 0
    
    @classmethod
    def salvar_id(cls,id):
        os.makedirs('dados', exist_ok=True)
        with open('dados/livro_id.txt','w') as f:
            f.write(str(id))

    
    def __str__(self):
        disponivel = 'Não' if self.emprestado else 'Sim'
        return f'ID:{self.id} - [{self.titulo}] Por: {self.autor} | Ano: {self.ano}, Gênero: {self.genero} | Disponível: {disponivel}'
    

livro1 = Livro("1984", "George Orwell", 1949, "Distopia")