# -*- coding: utf-8 -*-
import string
from anotacoes import Anotacoes

class BlocoDeNotas:
    def __init__(self, *anotacoes):
        self.anotacoes = {}
        
        for anotacao in anotacoes:
            self.anotacoes[anotacao.titulo] = anotacao
            
    def getNumeroAnotacoes(self):
        return len(self.anotacoes)
        
    def imprimir_notas(self):
        if len(self.anotacoes) > 0:
            for anotacao in self.anotacoes.values():
                print(anotacao, '\n')
        else:
            print ("Não existem notas cadastradas!")
        
        
    def getAnotacaoPorTitulo(self, titulo):
        return self.anotacoes[titulo] if titulo in self.anotacoes else None 
    
    def getAnotacaoPorID(self, id):
        listaAnotacoesComID = [anotacao for anotacao in self.anotacoes.values() if anotacao.id == id]     
        
        return listaAnotacoesComID[0] if listaAnotacoesComID else None
        
    def getAnotacoesComPalavra(self, palavra):
        return [anotacao for anotacao in self.anotacoes.values() if anotacao.contemPalavra(palavra)]        
            
    def inserirAnotacao(self, anotacao=None):
        if not anotacao:
            anotacao = Anotacoes(404, 'To be implemented')
        
        # Caso não existe uma anotação com o mesmo título
        if not anotacao.titulo in self.anotacoes:
            # Caso não exista uma anotação com o mesmo ID
            if not self.existeAnotacaoComID(anotacao.id):
                self.anotacoes[anotacao.titulo] = anotacao
                print('|| Adição de anotação realizada com sucesso! || ')
            else:
                print('# Já existe uma anotação cadastrada com este ID. #')
        else:
            print('# Já existe uma anotação cadastrada com este título. #')
            
    def excluirAnotacao(self, anotacaoAExcluir):
        if self.excluirAnotacao(anotacaoAExcluir):
            del self.anotacoes[anotacaoAExcluir.titulo]
        else:
            print ('# Não existe anotação com o título %s, id %s no bloco de notas #' % anotacaoAExcluir.titulo, anotacaoAExcluir.id)
            
    def alterarConteudoAnotacao(self, anotacao, novoConteudo):
        if self.existeAnotacao(anotacao):
            anotacao.alterarConteudo(novoConteudo) 
            print('|| Alteração realizada com sucesso! ||')
        else:
            print ('# A anotação fornecida não existe no bloco de notas. #')
            
    def alterarTituloAnotacao(self, tituloAntigo, novoTitulo):
        if tituloAntigo in self.anotacoes:
            if not novoTitulo in self.anotacoes:
                anotacao = self.anotacoes[tituloAntigo]    
                anotacao.alterarTitulo(novoTitulo)
            
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
        

