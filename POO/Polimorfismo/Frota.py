
from Veiculo import *
class Frota():
	def __init__(self):
		self._grau = 3
		self.__info = list()
		self.__frota = list()
	def insere(self,objeto):
		self.__frota.append(objeto)
	def procura(self,placaveiculo):
		for i in self.__frota:
			if(i.getPlacaVeiculo() == placaveiculo):
				print("Veiculo encontrado:")
				i.imprime()
				break
		else:
			print("Veiculo nao encontrado")
	def qntdVeiculo(self,tipoVeiculo):
		n = 0
		for i in self.__frota:
			if(i.getTipoVeiculo() == tipoVeiculo):
				n += 1
		return n
	def insereInfo(self,texto, tipoVeiculo):
		self.__info.append(texto)
	def removeInfo(self,texto):
		if texto in self.__info:
				self.__info.remove(texto)
				print(texto)
		else:
			print("Invalido")
	def imprimeInfo(self):
		print(*self.__info)
	def imprime(self):
		contador = 0
		for i in self.__frota:
			if(i.getTipoVeiculo() == "Carro" and self._grau == 3):
				i.imprime()
				contador += 1
				if(contador == self.qntdVeiculo("Carro")):
					self._grau -= 1
					self.imprime()			
			if(i.getTipoVeiculo() == "Moto" and self._grau == 2):
				i.imprime()
				contador += 1
				if(contador == self.qntdVeiculo("Moto")):
					self._grau -= 1
					self.imprime()
			if(i.getTipoVeiculo() == "Bicicleta" and self._grau == 1):
				i.imprime()
				contador += 1
				if(contador == self.qntdVeiculo("Bicicleta")):
					self._grau -= 1
					self.imprime() 
