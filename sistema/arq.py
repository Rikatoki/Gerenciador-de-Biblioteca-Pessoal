arquivo = 'biblioteca.txt' #Nome do arquivo (MUTÁVEL)
def verifArq():
    '''
    Verifica se o arquivo existe, se não, cria um.\n
    return: True se o arquivo existir. False se não existir. 
    '''
    try:
        with open(arquivo, 'r') as dados:
            return True
    except FileNotFoundError:
        with open(arquivo, 'wt'):
            print('Arquivo criado com sucesso!')
            return True
    except Exception as erro:
        print(f'Erro ao criar arquivo: {erro}')
        return False

def cadastLivro(titulo='Desconhecido', autor='Desconhecido',ano=0,genero='Desconhecido'):
    """
    param titulo: Título do livro\n
    param autor: Autor do livro\n
    param ano: Ano de lançamento\n
    param genero: Gênero do livro
    """
    try:
        with open(arquivo, 'at', encoding='utf-8') as dados:
            dados.write(f'{titulo};{autor};{ano};{genero}\n')
    except FileNotFoundError:
        verifArq()
        print('Tente novamente.')
    except Exception as erro:
        print(f'Erro: {erro}')

def listarLivros():
    """
    Faz uma lista de todos os livros contidos no arquivo.
    """
    try:
        with open(arquivo, 'rt', encoding='utf-8') as dados:
            livros = dados.readlines()
            for i,l in enumerate(livros):
                v = l.strip().split(';')
                print(f'Id:[{i+1}] Título: {v[0]} / Autor: {v[1]} / Ano: {v[2]} / Gênero: {v[3]}')
    except Exception as erro:
        print(f'Erro: {erro}')

def buscarLivro(busca):
    """
    busca: Título, Autor, Ano ou Gênero.
    return: Listagem de todos que contém busca.
    """
    try:
        with open(arquivo,'rt',encoding='utf-8') as dados:
            livros = dados.readlines()
            verificador = False
            for l in livros:
                v = l.strip().split(';')
                if busca in l:
                    print(f'Título: {v[0]} / Autor: {v[1]} / Ano: {v[2]} / Gênero: {v[3]}')
                    verificador = True
            if verificador:
                print('Não há livros')
    except Exception as  erro:
        print(f'Erro: {erro}')

def removerLivro(idx:int):
    """
    Verifica todo conteúdo até achar o conteúdo da index e logo em seguida o apaga.
    """
    try:
        with open(arquivo,'r') as ler:
            livros = ler.readlines()
            livros[idx-1]
            with open(arquivo,'wt+') as dados:
                for l in livros:
                    f = l.strip()
                    if l == livros[idx-1]:
                        continue
                    dados.write(f'{f}\n')
    except IndexError:
        print('Não há livro com este index.')
    except Exception as erro:
        print(f'Erro: {erro}')   

def atualizarLivro(idx=int):
    """
    A função pegará a index e passará por cada linha para verificar a index.\n
    Ao encontrar o conteúdo desejado, pergunta todas as informações novamente para rescreever o livro.
    """
    try:
        with open(arquivo,'r', encoding='utf-8') as ler:
            livros = ler.readlines()
            livros[idx-1]
            with open(arquivo,'wt+', encoding='utf-8') as dados:
                for l in livros:
                    if l == livros[idx-1]:
                        f = l.strip().split(';')
                        print(f'Título: {f[0]} / Autor: {f[1]} / Ano: {f[2]} / Gênero: {f[3]}')
                        t = input('Título: ').strip().title()
                        au = input('Autor: ').strip().title()
                        ano = int(input('Ano: '))
                        g = input('Genero: ').strip().capitalize()
                        dados.write(f'{t};{au};{ano};{g}\n')
                        continue
                    f = l.strip()    
                    dados.write(f'{f}\n')
    except IndexError:
        print('Não há livro com este index.')
    except Exception as erro:
        print(f'Erro: {erro}')