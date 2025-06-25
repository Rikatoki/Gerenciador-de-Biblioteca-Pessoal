from livro import Livro
from usuario import Usuario
from datetime import date
from json import load,dump
class Emprestimo:
    def __init__(self):
        self.emprestimos: list[tuple[int, int ,str, bool]] = []
        
    def registrar(self, user:Usuario, livro:Livro, data = date.today(), devolucao = False):
        if livro.emprestado == False:
            livro.emprestado = True
            self.emprestimos.append(user.id,livro.id,data.isoformat(),devolucao)
            return True
        return False

    def devoluçao(self, id_user:int, id_livro:int):
        sucesso = False
        for e in self.emprestimos:
            if e[0] == id_user and e[1] == id_livro:
                e[3] = date.today().isoformat()
                sucesso = True
        return sucesso

    def listar_ativos(self):
        ativos = False
        for n in self.emprestimos:
            if n[3] == False:
                print(f'Usuário [{n[0]}] Livro [{n[1]}] - Data do empréstimo: {n[2]}')
                ativos = True
        return ativos
    
    def historico(self, id_user:int):
        ativo = False
        for n in self.emprestimos:
            if n[0] == id_user:
                print(f'Usuário [{n[0]}] Livro [{n[1]}] - Data do empréstimo: {n[2]} - Devolução: {n[3]}')
                ativo = True
        return ativo

    def salvar(self):
        lista = []
        for e in self.emprestimos:
            lista.append({
                "id_user": e[0],
                "id_livro": e[1],
                "data_entrega": e[2],
                "devolucao": e[3]
            })
        with open("dados/emprestimos.json", 'w', encoding='utf-8') as arq:
            dump(sorted(lista, key= lambda d: d["data_entrega"]), arq, indent=4)

    def carregar(self):
        with open("dados/emprestimos.json", 'r', encoding='utf-8') as arq:
            dados = load(arq)
        for e in dados:
            self.emprestimos.append([e["id_user"], e["id_livro"], e["data_entrega"], e["devolucao"]])
