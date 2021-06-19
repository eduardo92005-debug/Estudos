from Veiculo import *
class Bicicleta(Veiculo):
	def __init__(self,placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo, marcha):
		Veiculo.__init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
		self.__marcha = marcha
	def getMarcha(self):
		return self.__marcha
	def setMarcha(self,novo):
		self.__marcha = novo
