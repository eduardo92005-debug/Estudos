  
from Veiculo import *
class Moto(Veiculo):
	def __init__(self, placaveiculo,fabricanteveiculo,numerorodas,tipoveiculo,cilindradas):
		Veiculo.__init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
		self._cilindradas = cilindradas
	def getCilindradas(self):
		return self._cilindradas
	def setCilindradas(self,novo):
		self._cilindradas = novo
