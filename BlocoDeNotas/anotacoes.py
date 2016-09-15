# -*- coding: utf-8 -*-
import datetime

class Anotacoes:
    def __init__(self, titulo, conteudo):
        self.id = id(self)   
        self.titulo = titulo
        self.conteudo = conteudo
        self.dataCriacao = datetime.date.today()
        
    def get_data_criacao(self):
        return self.dataCriacao
        
    def contem_palavra(self, palavra):
        return self.conteudo.find(palavra) != -1
        
    def altera_conteudo(self, novoConteudo):
        self.conteudo = novoConteudo
        
    def alterar_titulo(self, novoTitulo):
        self.titulo = novoTitulo
        
    def __str__(self):
        return "ID: %s \nTítulo: %s\nConteúdo: %s\nData de Criação: %s" % (self.id, self.titulo, self.conteudo, self.dataCriacao)