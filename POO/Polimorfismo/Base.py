from Bicicleta import *
from Moto import *
from Carro import *
from Veiculo import *

Veiculo = Veiculo("","",0,"",0)
Veiculo.insere(Bicicleta("NNN-0332","Bike Mountain",2,"Bicicleta",20))
Veiculo.insere(Carro("QWJ-1334","Volkswagen",4,"Carro",6,4,4,720))
Veiculo.insere(Moto("JKB-3321","Yamaha",2,"Moto",8,1200))
Veiculo.insere(Carro("KKK-0032","Ferrari",4,"Carro",8,2,2,1800))
Veiculo.imprimeFrota()
