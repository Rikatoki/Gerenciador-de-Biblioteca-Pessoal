from sistema import emprestimo,livro,usuario
from datetime import date
from time import sleep
class Menu_Cadastro:
    def __init__(self):
        self.options = {
            "1": self.livro,
            "2": self.usuario,
            "3": self.sair
        }
    def sub_menu(self):
        print(f'''{'Cadastros':^60}
1 - Cadastrar Livro
2 - Cadastrar Usuario
3 - Voltar
''')
    def executar(self):
        while True:
            self.sub_menu()
            escolha = input('Escolha uma opção: ')
            acao = self.options.get(escolha)
            if acao:
                sleep(0.5)
                if escolha == "3":
                    break
                acao()
            else:
                print(f'Opção inválida.')
                sleep(0.5)

    def livro(self):
        try:
            titulo = input('Titulo: ').title().strip()
            autor = input('Autor: ').title().strip()
            ano = int(input('Ano de lançamento: '))
            genero = input('Gênero: ').capitalize().strip() 
        except ValueError:
            print(f'Digite apenas valores númericos.')
        except Exception as erro:
            print(f'Erro: {erro}')
        else:
            cadastro_livro = livro.Livro(titulo,autor,ano,genero)

    def usuario(self):
        try:
            nome = input('Nome: ').title().strip()
            email = input('Email: ').strip()
        except Exception as erro:
            print(f'Erro: {erro}')
        else:
            cadastro_usuario = usuario.Usuario(nome,email)
    def sair(self):
        print('')

class Menu_Listar:
    def __init__(self):
        self.options = {
            "1": self.livros,
            "2": self.pessoas,
            "3": self.sair
        }
    def sub_menu(self):
        print(f'''{'Listagem':^60}
1 - Listar Livro
2 - Listar Usuario
3 - Voltar
''')
    def executar(self):
        while True:
            self.sub_menu()
            escolha = input('Escolha uma opção: ')
            acao = self.options.get(escolha)
            if acao:
                sleep(0.5)
                if escolha == "3":
                    break
                acao()
            else:
                print(f'Opção inválida.')
                sleep(0.5)

    def livros():
        for l in livro.Livro.livros:
            print(l)
    def pessoas():
        for u in usuario.Usuario.usuarios:
            print(u)
    def sair(self):
        print('')
        
class Menu_Emprestimo:
    def __init__(self):
        self.options = {
            "1": self.emprestar,
            "2": self.devolver,
            "3": self.sair
        }
    def sub_menu(self):
        print(f'''{'Empréstimos':^60}
1 - Emprestar Livro
2 - Devolução do Livro
3 - Voltar
''')
    def executar(self):
        while True:
            emprestimos = emprestimo.Emprestimo()
            emprestimos.carregar()
            self.sub_menu()
            escolha = input('Escolha uma opção: ')
            acao = self.options.get(escolha)
            if acao:
                sleep(0.5)
                if escolha == "3":
                    emprestimos.salvar()
                    break
                acao()
            else:
                print(f'Opção inválida.')
                sleep(0.5)
    def emprestar():
        try:
            listar = Menu_Listar()
            listar.livros()
            id_livro = int(input('Selecione o ID do livro: '))
            listar.pessoas()
            id_pessoa = int(input('Selecione o ID do usuário: '))
            print('')
        except Exception as erro:
            print(f'Erro: {erro}')
        else:
            for l in livro.Livro.livros:
                if l.id == id_livro:
                    livro = l
            for u in usuario.Usuario.usuarios:
                if u.id == id_pessoa:
                    pessoa = u
            if not livro or not pessoa:
                print(f'Ocorreu um erro na verificação de ID.')
            else:
                emprestimos = emprestimo.Emprestimo()
                if not emprestimos.registrar(pessoa,livro):
                    print(f'Não foi possível emprestar o livro. Verifique se o livro está disponível.')
                else:
                    emprestimos.registrar(pessoa,livro)
                    print(f'Emprestimo realizado com sucesso!!\n')

    def devolver():
        emprestimos = emprestimo.Emprestimo()
        if not emprestimos.listar_ativos():
            print('Não há empréstimos em ativos.')
        else:
            try:
                emprestimos.listar_ativos()
                id_user = int(input('ID do usuário: '))
                id_livro = int(input('ID do livro: '))
                emprestimos.devoluçao()
            except Exception as erro:
                print(f'Erro: {erro}')
    def sair(self):
        print('')
        
class Menu_Relatorio:
    def __init__(self):
        self.options = {
            "1": self.ativos,
            "2": self.historico,
            "3": self.sair
        }
    def sub_menu(self):
        print(f'''{'Relatórios':^60}
1 - Relatório de empréstimos ativos
2 - Relatório de histórico de um usuário
3 - Voltar
''')
    def executar(self):
        while True:
            self.sub_menu()
            escolha = input('Escolha uma opção: ')
            acao = self.options.get(escolha)
            if acao:
                sleep(0.5)
                if escolha == "3":
                    break
                acao()
            else:
                print(f'Opção inválida.')
                sleep(0.5)

    def ativos(self):
        emprestimos = emprestimo.Emprestimo()
        if not emprestimos.listar_ativos():
            print('Não há empréstimos ativos.')
        else:
            emprestimos.listar_ativos()

    def historico(self):
        try:
            listar = Menu_Listar()
            emprestimos = emprestimo.Emprestimo()
            listar.pessoas()
            id_usuario = int(input('Verificar histórico do ID: '))
            if not emprestimos.historico(id_usuario):
                print(f'Não há registro desse usuário.')
            else:
                emprestimos.historico(id_usuario)
        except Exception as erro:
            print(f'Erro: {erro}')
    def sair(self):
        print('')

class MenuPrincipal:
    def __init__(self):
        self.options = {
            "1": self.cadastro,
            "2": self.emprestimos,
            "3": self.listar,
            "4": self.relatorios,
            "5": self.busca,
            "6": self.sair
        }
    
    def mostrar_menu(self):
        data = date.today()
        print(f'''{'-=-'*20}
{f'{f'GERENCIAR DE BIBLIOTECA PESSOAL':>45}{f'[{data}]':>15}'}
{'-=-'*20}

1 - Cadastrar [Livro / Pessoa]
2 - Gerenciar Empréstimos
3 - Listar [Livro / Pessoa]
4 - Relatórios
5 - Buscar [Livro]
6 - Sair
{'---'*20}''')
    def executar(self):
        while True:
            self.mostrar_menu()
            escolha = input('Escolha uma opção: ')
            acao = self.options.get(escolha)
            if acao:
                sleep(0.5)
                acao()
            else:
                print('Opção inválida, tente novamente.')
                sleep(1)
    
    def cadastro(self):
        print('')
        cadastro = Menu_Cadastro()
        cadastro.executar()

    def listar(self):
        print('')
        listar = Menu_Listar()
        listar.executar()

    def emprestimos(self):
        print('')
        emprestimos = Menu_Emprestimo()
        emprestimos.executar()

    def relatorios(self):
        print('')
        relatorios = Menu_Relatorio()
        relatorios.executar()

    def busca(self):
        print('')
        bsc = input('Titulo ou Autor: ')
        livro.Livro.buscar(bsc)

    def sair(self):
        print('Fechando o programa...')
        sleep(0.5)
        exit()