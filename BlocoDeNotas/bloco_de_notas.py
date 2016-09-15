# -*- coding: utf-8 -*-
import string
from anotacoes import Anotacoes

class BlocoDeNotas:
    def __init__(self, *anotacoes):
        self.anotacoes = {}
        
        for anotacao in anotacoes:
            self.anotacoes[anotacao.titulo] = anotacao
            
    def get_numero_anotacoes(self):
        return len(self.anotacoes)
        
    def imprimir_notas(self):
        if len(self.anotacoes) > 0:
            for anotacao in self.anotacoes.values():
                print(anotacao, '\n')
        else:
            print ("Não existem notas cadastradas!")
        
        
    def get_anotacao_por_titulo(self, titulo):
        return self.anotacoes[titulo] if titulo in self.anotacoes else None 
    
    def get_anotacao_por_ID(self, id):
        listaAnotacoesComID = [anotacao for anotacao in self.anotacoes.values() if anotacao.id == id]     
        
        return listaAnotacoesComID[0] if listaAnotacoesComID else None
        
    def get_anotacoes_com_palavra(self, palavra):
        return [anotacao for anotacao in self.anotacoes.values() if anotacao.contem_palavra(palavra)]        
            
    def inserir_anotacao(self, anotacao=None):
        if not anotacao:
            anotacao = Anotacoes(404, 'To be implemented')
        
        # Caso não existe uma anotação com o mesmo título
        if not anotacao.titulo in self.anotacoes:
            # Caso não exista uma anotação com o mesmo ID
            if not self.existeAnotacaoComID(anotacao.id):
                self.anotacoes[anotacao.titulo] = anotacao
                print('\n|| Adição de anotação realizada com sucesso! || ')
            else:
                print('\n# Já existe uma anotação cadastrada com este ID. #')
        else:
            print('\n# Já existe uma anotação cadastrada com este título. #')
            
    def excluir_anotacao(self, anotacaoAExcluir):
        if self.existeAnotacao(anotacaoAExcluir):
            del self.anotacoes[anotacaoAExcluir.titulo]
            print ('\n|| Exclusão realizada com sucesso ||')
        else:
            print ('# Não existe anotação com o título %s, id %s no bloco de notas #' % anotacaoAExcluir.titulo, anotacaoAExcluir.id)
            
    def alterar_conteudo_anotacao(self, anotacao, novoConteudo):
        if self.existeAnotacao(anotacao):
            anotacao.alterar_conteudo(novoConteudo) 
            print('|| Alteração realizada com sucesso! ||')
        else:
            print ('# A anotação fornecida não existe no bloco de notas. #')
            
    def alterar_titulo_anotacao(self, tituloAntigo, novoTitulo):
        if tituloAntigo in self.anotacoes:
            if not novoTitulo in self.anotacoes:
                anotacao = self.anotacoes[tituloAntigo]    
                anotacao.alterar_titulo(novoTitulo)
            
                del self.anotacoes[tituloAntigo]        
                self.anotacoes[anotacao.titulo] = anotacao
                print('|| Alteração realizada com sucesso! || ')
            else:
                print('# Já existe uma anotação com o novo título fornecido #')
        else:
            print('# A anotação fornecida não existe no bloco de notas #')
            
    def existeAnotacaoComID(self, id):
        return id in [anotacao.id for anotacao in self.anotacoes.values()]
        
    def existeAnotacao(self, anotacao):
        return anotacao.titulo in self.anotacoes
            
    def getPalavrasMaisFrequentes(self):
        words = {}        
        
        for anotacao in self.anotacoes.values():
            palavras = [word.strip(string.punctuation) for word in anotacao.conteudo.split(' ')]
            
            for palavra in palavras:
                words[palavra] = words[palavra] + 1 if palavra in words else 1
                
        
        ordenado = sorted(words, key=words.get, reverse=True)
        
        palavras = {}

        if len(ordenado) >= 1:
            palavras[ordenado[0]] = words[ordenado[0]]
            
        if len(ordenado) >= 2:
            palavras[ordenado[1]] = words[ordenado[1]]
            
        if len(ordenado) >= 3:
            palavras[ordenado[2]] = words[ordenado[2]]
        
        if palavras:
            print(palavras)
        else:
            print('# Não existem palavras no bloco de notas #')
        

