# -*- coding: utf-8 -*-

from bloco_de_notas import BlocoDeNotas
from anotacoes import Anotacoes

def criarNovaAnotacao():
    indice = input('>> Insira o indice da nova anotacao: ')
    conteudo = input('>> Insira o conteudo da nova anotacao: ')
    id = input('>> Insira o ID da nova anotacao: ')
    
    return Anotacoes(id, indice, conteudo)

a = Anotacoes(1, '1ª anotação', 'Eh isso mesmo')
b = Anotacoes(2, '2ª anotação', 'Body mesmo')
c = Anotacoes(3, 'McGregor Notes', 'I never got into training to be an All-Ireland boxing champ or to win a belt. At the start, I just got into it to learn how to defend myself when I got into situations.')

notepad = BlocoDeNotas(a, b, c)

print('.: BLOCO DE NOTAS :.')

while True:
    print('\n1 - Inserir Anotação') 
    print('2 - Alterar conteúdo da anotação')
    print('3 - Buscar Anotação ')
    print('4 - Buscar Anotação por palavra')
    print('X - Sair')
    
    opcao = input('>> Insira sua opcao: ')
    
    if opcao == '1':
        novaAnotacao = criarNovaAnotacao()

        if novaAnotacao:
            notepad.inserirAnotacao(novaAnotacao)
    elif opcao == '2':
        anotacao = None

        while True:
            alterar_conteudo_opcao = input('>> Buscar anotação pro índice (I) ou ID (ID) | X para voltar: ').lower()

            if alterar_conteudo_opcao == 'i':
                anotacao_indice = input('>> Insira o índice: ')

                anotacao = notepad.getAnotacaoPorIndice(anotacao_indice)
                break
            elif alterar_conteudo_opcao == 'id':
                anotacao_id = input('>> Insira o ID: ')

                anotacao = notepad.getAnotacaoPorID(int(anotacao_id))
                break
            else:
                print('# Insira uma opção válida #')

        if anotacao:
            novoConteudo = input('>> Insira o novo conteúdo: ')

            notepad.alterarConteudoAnotacao(anotacao, novoConteudo)
        else:
            print('Não existe nenhuma anotação no bloco de notas com o dado informado. Tente novamente')
        
    elif opcao == '3':
        indiceAnotacao = input('>> Insira o indice da anotacao: ')
        
        anotacao = notepad.getAnotacaoPorIndice(indiceAnotacao)
        
        if anotacao:
            print(anotacao)
        else:
            print ('Não existe anotação com o índice %s no bloco de notas.' % indiceAnotacao)

    elif opcao == '4':
        print()
        palavra = input('>> Insira uma palavra: ')

        anotacoes = notepad.getAnotacoesComPalavra(palavra)

        if anotacoes:
            print("\n.: Anotacoes Encontradas com a palavra '%s'\n" % palavra)
            for anotacao in anotacoes:
                print(anotacao, '\n')
        else:
            print('# Nenhuma anotacao no bloco de notas contem a palavra %s' % palavra)

    elif opcao.lower() == 'x':
        print('# Programa finalizado #')
        break