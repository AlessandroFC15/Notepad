# -*- coding: utf-8 -*-
import datetime

class Anotacoes:
    def __init__(self, indice, conteudo):
        self.indice = indice
        self.conteudo = conteudo
        self.dataCriacao = datetime.date.today()
        
    def getDataCriacao(self):
        return self.dataCriacao
        
    def __str__(self):
        return "Índice: %d\nConteúdo: %s\nData de Criação: %s" % (self.indice, self.conteudo, self.dataCriacao)