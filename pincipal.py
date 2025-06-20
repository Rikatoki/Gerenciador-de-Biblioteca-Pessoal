from sistema import (menu,arq)
from time import sleep
while True:
    arq.verifArq()
    menu.opçoes('SAIR','ADICIONAR LIVROS', 'LISTAR LIVROS', 'BUSCAR LIVRO ESPECÍFICO', 'REMOVER LIVROS', 'ATUALIZAR LIVROS', cbç='GERENCIADOR DE BIBLIOTECA PESSOAL')
    try:
        opç = int(input('OPÇÂO: '))
        menu.linha()
    except (TypeError, ValueError):
        print('ERRO: Tipo de valor inválido.')
    except Exception as erro:
        print(f'ERRO: {erro}')
    else:
        if opç == 1:
            try:
                titulo = input('Título: ').title().strip()
                autor = input('Autor: ').title().strip()
                try:
                    ano = int(input('Ano: '))
                except:
                    print('Erro: Digite um valor válido')
                genero = input('Genero: ').capitalize().strip()
            except Exception as erro:
                print(f'Erro: {erro}')
            else:
                arq.cadastLivro(titulo,autor,ano,genero)
        elif opç == 2:
            arq.listarLivros()
            menu.linha()
        elif opç == 3:
            n = input('Título ou Autor: ').title().strip()
            arq.buscarLivro(n)
            menu.linha()
        elif opç == 4:
            arq.listarLivros()
            try:
                index = int(input('Digite o index do livro: '))
            except:
                print('Digite um valor aceitável.')
            arq.removerLivro(index)
            menu.linha()
        elif opç == 5:
            try:
                arq.listarLivros()
                index = int(input('Index do livro: '))
                arq.atualizarLivro(index)
                menu.linha()
            except Exception as erro:
                print(f'Erro: {erro}')
        elif opç == 0:
            print('SAINDO DO PROGRAMA...')
            menu.linha()
            break
        else:
            print('Opção inválida')
    finally:
        print('')
        sleep(0.5)