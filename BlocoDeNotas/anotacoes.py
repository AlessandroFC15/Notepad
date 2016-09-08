# -*- coding: utf-8 -*-
import datetime

class Anotacoes:
    def __init__(self, id, indice, conteudo):
        self.id = id   
        self.indice = indice
        self.conteudo = conteudo
        self.dataCriacao = datetime.date.today()
        
    def getDataCriacao(self):
        return self.dataCriacao
        
    def contemPalavra(self, palavra):
        return self.conteudo.find(palavra) != -1
        
    def alterarConteudo(self, novoConteudo):
        self.conteudo = novoConteudo
        
    def alterarIndice(self, novoIndice):
        self.indice = novoIndice
        
    def __str__(self):
        return "Índice: %s\nConteúdo: %s\nData de Criação: %s" % (self.indice, self.conteudo, self.dataCriacao)