import datetime

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

class Anotacoes:
	def __init__(self, indice, conteudo):
		self.indice = indice
		self.conteudo = conteudo
		self.dataCriacao = datetime.date.today()
		
	def getDataCriacao(self):
		return self.dataCriacao
		
	def __str__(self):
		return "Índice: %d\nConteúdo: %s\nData de Criação: %s" % (self.indice, self.conteudo, self.dataCriacao)
		
a = Anotacoes(1, '1ª anotação mesmo')
b = Anotacoes(2, '2ª anotação mesmo')

notepad = BlocoDeNotas(a, b)

print(notepad.getAnotacao(3))