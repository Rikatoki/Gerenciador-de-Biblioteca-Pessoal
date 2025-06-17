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
            for l in livros:
                v = l.strip().split(';')
                if busca in l:
                    print(f'Título: {v[0]} / Autor: {v[1]} / Ano: {v[2]} / Gênero: {v[3]}')
    except Exception as  erro:
        print(f'Erro: {erro}')
