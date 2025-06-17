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
    try:
        with open(arquivo, 'at', encoding='utf-8') as dados:
            dados.write(f'{titulo};{autor};{ano};{genero}\n')
    except FileNotFoundError:
        verifArq()
        print('Tente novamente.')
    except Exception as erro:
        print(f'Erro: {erro}')

def listarLivros():
    try:
        with open(arquivo, 'rt', encoding='utf-8') as dados:
            livros = dados.readlines()
            for i,l in enumerate(livros):
                v = l.strip().split(';')
                print(f'Id:[{i+1}] Título: {v[0]} / Autor: {v[1]} / Ano: {v[2]} / Gênero: {v[3]}')
    except Exception as erro:
        print(f'Erro: {erro}')
