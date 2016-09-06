# -*- coding: utf-8 -*-
import string
from anotacoes import Anotacoes

class BlocoDeNotas:
    def __init__(self, *anotacoes):
        self.anotacoes = {}
        
        for anotacao in anotacoes:
            self.anotacoes[anotacao.indice] = anotacao
            
    def getNumeroAnotacoes(self):
        return len(self.anotacoes)
        
    def printAnotacoes(self):
        for anotacao in self.anotacoes.values():
            print(anotacao)
            print('')
            
    def getAnotacao(self, indice):
        if indice in self.anotacoes:
            return self.anotacoes[indice]
        else:
            print ('Não existe anotação com o índice %s no bloco de notas.' % indice)
            return None
            
    def inserirAnotacao(self, anotacao=None):
        if not anotacao:
            anotacao = Anotacoes(404, 'To be implemented')
        
        if not (anotacao.indice in self.anotacoes):
            self.anotacoes[anotacao.indice] = anotacao
        else:
            print('Já existe uma anotação cadastrada com este índice')
            
    def excluirAnotacao(self, indice):
        if indice in self.anotacoes:
            del self.anotacoes[indice]
        else:
            print ('Não existe anotação com o índice %s no bloco de notas.' % indice)
    
    def getPalavrasMaisFrequentes(self):
        words = {}        
        
        for anotacao in self.anotacoes.values():
            palavras = [word.strip(string.punctuation) for word in anotacao.conteudo.split(' ')]
            
            for palavra in palavras:
                words[palavra] = words[palavra] + 1 if palavra in words else 1
                
        
        ordenado = sorted(words, key=words.get, reverse=True)
        
        return { ordenado[0] : words[ordenado[0]], 
                ordenado[1] : words[ordenado[1]], 
                ordenado[2] : words[ordenado[2]] }

