from os import path
class Livro:
    @classmethod
    def carregar_id(cls):
        if path.exists('dados/livro_id.txt'):
            with open('dados/livro_id.txt','r') as f:
                return int(f.read())
        return 0
    
    @classmethod
    def salvar_id(cls,id):
        with open('dados/livro_id.txt','w') as f:
            f.write(str(id))

    def __init__(self, titulo:str, autor:str, ano:int, genero:str, id:int = None,emprestado:bool = False):
        if id is None:
            id = Livro.carregar_id() + 1
            Livro.salvar_id(id)
        self.id = id
        self.titulo = titulo.title().split()
        self.autor = autor.title().split()
        self.ano = ano
        self.genero = genero.title().split()
        self.emprestado = emprestado

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
    def from_dict(cls, data:list[dict]):
        return [cls(**l) for l in data]
    
    def __str__(self):
        disponivel = 'Não' if self.emprestado else 'Sim'
        return f'ID:{self.id} - [{self.titulo}] Por: {self.autor} | Ano: {self.ano}, Gênero: {self.genero} | Disponível: {disponivel}'