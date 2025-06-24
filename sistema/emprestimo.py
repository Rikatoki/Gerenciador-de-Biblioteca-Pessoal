from livro import Livro
from usuario import Usuario
from datetime import date
from json import load,dump
class Emprestimo:
    def __init__(self):
        self.emprestimos: list[tuple[Usuario,Livro,date,date]] = []

    def cadastrar(self, usuario:Usuario, livro:Livro,data = date.today(), devolucao = None):
        if not livro.emprestado:
            if devolucao == None:
                devolucao = False
            self.emprestimos.append([usuario, livro, data, devolucao])
            livro.emprestado = True
            return f'Cadastro: [Livro: {livro.titulo} emprestado ao {usuario.nome}, email: {usuario.email}.]'
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
        return f'Não foi encontrado este registro, ou o livro já foi devolvido.'
        
    def emprestimos_ativos(self):
        ativos = False
        for e in self.emprestimos:
            if e[3] == False:
                print(f'Usuario: {e[0].nome} | Livro: {e[1].titulo} | Data de entrega: {e[2]}')
                ativos = True
        return ativos

    def historico_usuario(self,user:int):
        historico = False
        for e in self.emprestimos:
            if e[0].id == user:
                print(f'Cadastro: [Livro: {e[1].titulo} emprestado ao {e[0].nome}, email: {e[0].email}.]')
                historico = True
        return historico
    
    def salvar(self):
        lista = []
        for e in self.emprestimos:
            dicionario = {
                "usuario": e[0],
                "livro": e[1],
                "data": e[2],
                "devolucao": e[3]
            }
            lista.append(dicionario)
        with open('dados/emprestimos.json', 'w',encoding='utf-8') as arq:
            dump(lista,arq, indent=4)

    def carregar(self):
        with open('dados/emprestimos.json','r',encoding='utf-8') as arq:
            dados = load(arq)
            for d  in dados:
                self.emprestimos.append([d["usuario"], d["livro"], d["data"], d["devolucao"]])