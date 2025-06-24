import os
from json import load, dump
class Usuario:
    usuarios: list['Usuario'] = []
    
    def __init__(self, nome:str, email:str, id:int = None):
        Usuario.carregar()
        if id is not None:
            self.id = id    
        else:
            id = Usuario.carregar_id() + 1
            Usuario.salvar_id(id)
            self.id =id
        self.nome = nome
        self.email = email
        Usuario.usuarios.append(self)
        Usuario.salvar()

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "email":self.email
        }
    
    @classmethod
    def from_dict(cls, data:list[dict]):
        usuarios = []
        for d in data:
            user = cls.__new__(cls)
            user.id = d["id"]
            user.nome = d["nome"]
            user.email = d["email"]
            usuarios.append(user)
        return usuarios
    
    @classmethod
    def salvar(cls):
        usuarios = []
        for u in cls.usuarios:
            usuarios.append(u.to_dict())
        os.makedirs('dados', exist_ok=True)
        with open('dados/usuarios.json', 'w', encoding='utf-8') as arq:
            dump(usuarios, arq, indent=2)

    @classmethod
    def carregar(cls):
        if os.path.exists('dados/usuarios.json'):
            with open('dados/usuarios.json', 'r', encoding='utf-8') as arq:
                dados = load(arq)
            Usuario.usuarios = Usuario.from_dict(dados)
    
    @classmethod
    def carregar_id(cls):
        if os.path.exists('dados/usuario_id.txt'):
            with open('dados/usuario_id.txt', 'r') as f:
                return int(f.read())
        return 0
    
    @classmethod
    def salvar_id(cls,id):
        with open('dados/usuario_id.txt', 'w') as f:
            f.write(str(id))
    
    def __str__(self):
        return f'ID:{self.id} - [{self.nome}] email: {self.email}'
    