rom Veiculo import *
from Bicicleta import *
from Carro import *
from Moto import *
class MainTransporte():
	Bicicleta1 = Bicicleta("NNN-3232","Bike Mountain",2,"Bike",8)
	Veiculo1 = Veiculo("","","",0)
	Carro1 = Carro("QWJ-1334","Volkswagen",4,"Carro",4,4,720)
	Moto1 = Moto("JKB-3321","Yamaha",2,"Moto",1200)
	Bicicleta1.imprime()
	Carro1.imprime()
	Moto1.imprime()
	print(Moto1.getCilindradas())
	Moto1.setCilindradas(1000)
	print(Moto1.getCilindradas())
	lista = (Carro1.getPortas(),Carro1.getJanelas(),Carro1.getCavalos())
	print(*lista)
	Carro1.setPortas(3)
	Carro1.setJanelas(2)
	Carro1.setCavalos(200)
	lista = (Carro1.getPortas(),Carro1.getJanelas(),Carro1.getCavalos())
	print(*lista)
