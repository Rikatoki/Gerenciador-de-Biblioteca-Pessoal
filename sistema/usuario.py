from os import path

class Usuario:
    @classmethod
    def carregar_id(cls):
        if path.exists('dados/usuario_id.txt'):
            with open('dados/usuario_id.txt', 'r') as f:
                return int(f.read())
        return 0
    @classmethod
    def salvar_id(cls,id):
        with open('dados/usuario_id.txt', 'w') as f:
            f.write(str(id))
    def __init__(self, nome:str, email:str, id:int = None):
        if id is not None:
            self.id = id    
        else:
            id = Usuario.carregar_id() + 1
            Usuario.salvar_id(id)
            self.id =id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "email":self.email
        }
    
    @classmethod
    def from_dict(cls, data:list[dict]):
        return [cls(**u) for u in data]
    
    def __str__(self):
        return f'ID:{self.id} - [{self.nome}] email: {self.email}'