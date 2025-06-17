def linha(qnt=30, crtr='-=-'):
    '''
    CRIADOR DE LINHAS\n
    param qnt: Valor númerico de quantas linhas deseja. (Padrão: 20)\n
    param crtr: Caractere da linha. (Padrão: -=-)
    '''
    return print(f'{crtr}'*qnt)
def opçoes(*txt,cbç='MENU PRINCIPAL', form=90):
    '''
    CRIAÇÃO AUTOMÁTICA DO MENU\n
    param txt: Opções que queira inserir. (obrigatório) (Não há necessidade de numerar elas)\n
    param cbç: Cabeçário das opções. (Padrão: "MENU PRINCIPAL")\n
    param form: Formatação númerica do cabeçário (Padrão: 60)\n
    return: todas as opções muito bem formatadas
    '''
    linha()
    print(f'{cbç:^{form}}')
    linha()
    for i,o in enumerate(txt):
        print(f'[ {i} ] ---- {o}')
    linha()