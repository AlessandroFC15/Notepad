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
            print(anotacao, '\n')
            
    def getAnotacaoPorIndice(self, indice):
        return self.anotacoes[indice] if indice in self.anotacoes else None 
    
    def getAnotacaoPorID(self, id):
        listaAnotacoesComID = [anotacao for anotacao in self.anotacoes.values() if anotacao.id == id]     
        
        return listaAnotacoesComID[0] if listaAnotacoesComID else None
        
    def getAnotacoesComPalavra(self, palavra):
        return [anotacao for anotacao in self.anotacoes.values() if anotacao.contemPalavra(palavra)]        
            
    def inserirAnotacao(self, anotacao=None):
        if not anotacao:
            anotacao = Anotacoes(404, 'To be implemented')
        
        # Caso não existe uma anotação com o mesmo índice
        if not anotacao.indice in self.anotacoes:
            # Caso não exista uma anotação com o mesmo ID
            if not self.existeAnotacaoComID(anotacao.id):
                self.anotacoes[anotacao.indice] = anotacao
                print('Adição de anotação realizada com sucesso!')
            else:
                print('Já existe uma anotação cadastrada com este ID.')
        else:
            print('Já existe uma anotação cadastrada com este índice.')
            
    def excluirAnotacao(self, anotacaoAExcluir):
        if self.excluirAnotacao(anotacaoAExcluir):
            del self.anotacoes[anotacaoAExcluir.indice]
        else:
            print ('Não existe anotação com o índice %s, id %s no bloco de notas.' % anotacaoAExcluir.indice, anotacaoAExcluir.id)
            
    def alterarConteudoAnotacao(self, anotacao, novoConteudo):
        if self.existeAnotacao(anotacao):
            anotacao.alterarConteudo(novoConteudo) 
            print('Alteração realizada com sucesso!')
        else:
            print ('A anotação fornecida não existe no bloco de notas.')
            
    def alterarIndiceAnotacao(self, indiceAntigo, novoIndice):
        if indiceAntigo in self.anotacoes:
            if not novoIndice in self.anotacoes:
                anotacao = self.anotacoes[indiceAntigo]    
                anotacao.alterarIndice(novoIndice)
            
                del self.anotacoes[indiceAntigo]        
                self.anotacoes[anotacao.indice] = anotacao
            else:
                print('Já existe uma anotação com o novo índice fornecido')
        else:
            print('A anotação fornecida não existe no bloco de notas.')
            
    def existeAnotacaoComID(self, id):
        return id in [anotacao.id for anotacao in self.anotacoes.values()]
        
    def existeAnotacao(self, anotacao):
        return anotacao.indice in self.anotacoes
            
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

