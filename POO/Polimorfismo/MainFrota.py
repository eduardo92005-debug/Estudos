  
from Frota import *
from Veiculo import *
from Bicicleta import *
from Carro import *
from Moto import *

Frota1 = Frota()
Frota1.insere(Bicicleta("NNN-0332","Bike Mountain",2,"Bicicleta",20))
Frota1.insere(Carro("QWJ-1334","Volkswagen",4,"Carro",4,4,720))
Frota1.insere(Moto("JKB-3321","Yamaha",2,"Moto",1200))
Frota1.insere(Carro("KKK-0032","Ferrari",4,"Carro",2,2,1800))
Frota1.imprime()
print("......")
Frota1.procura("QWJ-1334")
Frota1.procura("DSA-1234")
print("......")
Frota1.insereInfo("O carro(QWJ-1334) esta quebrado","Carro")
Frota1.insereInfo("A bicicleta esta faltando um pneu","Bicicleta")
Frota1.removeInfo("O carro(QWJ-1334) esta quebrado")
print("......")
Frota1.imprimeInfo()
