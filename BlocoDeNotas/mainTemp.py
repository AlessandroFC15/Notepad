# -*- coding: utf-8 -*-

from bloco_de_notas import BlocoDeNotas
from anotacoes import Anotacoes

import sys

class Menu:
    def __init__(self):
        self.bloco_de_notas = BlocoDeNotas()
        self.escolhas = {
            "1": self.bloco_de_notas.imprimir_notas,
            "2": self.buscar_notas_titulo,
            "3": self.buscar_notas_ID,
            "4": self.adicionar_notas,
            "5": self.modificar_notas,
            "7": self.buscar_notas_com_palavra,
            "8": self.bloco_de_notas.getPalavrasMaisFrequentes,
            "X": self.sair
            
        }
    
    def apresentar_menu(self):
        print("""\n\t.: Menu :.
        1. Imprimir notas
        2. Buscar nota por título
        3. Buscar nota por ID
        4. Adicionar notas
        5. Alterar nota
        7. Buscar notas com palavra
        8. Buscar palavras mais frequentes
        X. Sair
        """)
        
    def executar(self):
        while True:
            self.apresentar_menu()
            option = input('>> Escolha uma opção: ')
            
            action = None
            
            if option in self.escolhas:
                action = self.escolhas[option]
            
            if action:
                print()
                action()
            else:
                print ("# %s não é uma escolha válida #" % option)
                
    def buscar_notas_titulo(self):
        indiceAnotacao = input('>> Insira o título da anotacao: ')
        
        anotacao = self.bloco_de_notas.getAnotacaoPorTitulo(indiceAnotacao)
        
        if anotacao:
            print(anotacao)
        else:
            print ('# Não existe anotação com o título %s no bloco de notas #' % indiceAnotacao)
            
    def buscar_notas_ID(self):
        id = input('>> Insira o ID da anotacao: ')
        
        anotacao = self.bloco_de_notas.getAnotacaoPorID(id)
        
        if anotacao:
            print(anotacao)
        else:
            print ('# Não existe anotação com o ID %s no bloco de notas #' % id)
            
    def adicionar_notas(self):
        novaAnotacao = self.criarNovaAnotacao()

        if novaAnotacao:
            self.bloco_de_notas.inserirAnotacao(novaAnotacao)
            
    def criarNovaAnotacao(self):
        titulo = input('>> Insira o título da nova anotacao: ')
        conteudo = input('>> Insira o conteudo da nova anotacao: ')
       
        return Anotacoes(titulo, conteudo)
        
    def modificar_notas(self):
        anotacao = None

        while True:
            alterar_conteudo_opcao = input('>> Buscar anotação por título (T) ou ID (ID): ')

            if alterar_conteudo_opcao.lower() == 't':
                anotacao_titulo = input('>> Insira o título: ')

                anotacao = self.bloco_de_notas.getAnotacaoPorTitulo(anotacao_titulo)
                break
            elif alterar_conteudo_opcao.lower() == 'id':
                anotacao_id = input('>> Insira o ID: ')

                anotacao = self.bloco_de_notas.getAnotacaoPorID(int(anotacao_id))
                break
            else:
                print('# Insira uma opção válida #')

        if anotacao:
            novoConteudo = input('>> Insira o novo conteúdo: ')
            novoTitulo = input('>> Insira o novo título: ')
            
            if novoConteudo:
                self.bloco_de_notas.alterarConteudoAnotacao(anotacao, novoConteudo)
                
            if novoTitulo:
                self.bloco_de_notas.alterarTituloAnotacao(anotacao.titulo, novoTitulo)
        else:
            print('# Não existe nenhuma anotação no bloco de notas com o dado informado. Tente novamente #')
            
            
    def buscar_notas_com_palavra(self):
        palavra = input('>> Insira uma palavra: ')

        anotacoes = self.bloco_de_notas.getAnotacoesComPalavra(palavra)

        if anotacoes:
            print("\n.: Anotacoes Encontradas com a palavra '%s'\n" % palavra)
            for anotacao in anotacoes:
                print(anotacao, '\n')
        else:
            print('# Nenhuma anotacao no bloco de notas contem a palavra %s' % palavra)
        
    def sair(self):
        print("Saindo...")
        sys.exit(0)
       
if __name__ == "__main__":
    menu = Menu()

    menu.executar()
