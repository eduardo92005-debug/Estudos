from Veiculo import *
class Carro(Veiculo):
	def __init__(self, placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo,portas,janelas, cavalos):
		Veiculo.__init__(self,placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo)
		self._portas = portas
		self._janelas = janelas
		self._cavalos = cavalos
	#Getters
	def getPortas(self):
		return self._portas
	def getJanelas(self):
		return self._janelas
	def getCavalos(self):
		return self._cavalos
	#Setters
	def setPortas(self,novo):
		self._portas = novo
	def setJanelas(self,novo):
		self._janelas = novo
	def setCavalos(self,novo):
		self._cavalos = novo
