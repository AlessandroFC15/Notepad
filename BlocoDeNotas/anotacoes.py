# -*- coding: utf-8 -*-
import datetime

class Anotacoes:
    def __init__(self, titulo, conteudo):
        self.id = id(self)   
        self.titulo = titulo
        self.conteudo = conteudo
        self.dataCriacao = datetime.date.today()
        
    def getDataCriacao(self):
        return self.dataCriacao
        
    def contemPalavra(self, palavra):
        return self.conteudo.find(palavra) != -1
        
    def alterarConteudo(self, novoConteudo):
        self.conteudo = novoConteudo
        
    def alterarTitulo(self, novoTitulo):
        self.titulo = novoTitulo
        
    def __str__(self):
        return "ID: %s \nTítulo: %s\nConteúdo: %s\nData de Criação: %s" % (self.id, self.titulo, self.conteudo, self.dataCriacao)