class Aquecedor34():
    """attributes: __temperatura, __min(parameter),__max(patameter), __incremento"""
    def __init__(self,minimo,maximo):
        self.__temperatura = 15
        self.__min = minimo
        self.__max = maximo
        self.__incremento = 5
    #Getters
    def getTemperatura(self):
        return self.__temperatura
    def getMin(self):
        return self.__min
    def getMax(self):
        return self.__max
    def getIncremento(self):
        return self.__incremento
    #Setters
    def setTemperatura(self,new_temp):
        self.__temperatura = new_temp
    def setMin(self,new_min):
        self.__min = new_min
    def setMax(self,new_max):
        self.__max = new_max
    def setIncremento(self,new_incremento):
        self.__incremento = new_incremento
    #Methods
    def MaisMorno(self):
        self.__temperatura += self.__incremento
    def MenosMorno(self):
        self.__temperatura -= self.__incremento
