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

