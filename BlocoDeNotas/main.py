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
    print('2 - Alterar conteúdo da anotação fornecendo índice')
    print('3 - Buscar Anotação ')
    print('X - Sair')
    
    opcao = input('>> Insira sua opcao: ').lower()
    
    if opcao == '1':
        novaAnotacao = criarNovaAnotacao()

        if novaAnotacao:
            notepad.inserirAnotacao(novaAnotacao)
    elif opcao == '2':
        indice = input('>> Insira o indice da anotacao: ')
        
        anotacao = notepad.getAnotacaoPorIndice(indice)
        
        if anotacao:
            novoConteudo = input('>> Insira o novo conteúdo: ')
            
            notepad.alterarConteudoAnotacao(anotacao, novoConteudo)
        else:
            print ('Não existe anotação com o índice %s no bloco de notas.' % indice)
        
    elif opcao == '3':
        indiceAnotacao = input('>> Insira o indice da anotacao: ')
        
        anotacao = notepad.getAnotacaoPorIndice(indiceAnotacao)
        
        if anotacao:
            print(anotacao)
        else:
            print ('Não existe anotação com o índice %s no bloco de notas.' % indiceAnotacao)
        
    if opcao == 'x':
        print('# Programa finalizado #')
        break