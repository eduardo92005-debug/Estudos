class Aquecedor34():
    """attributes: __temperatura, __min(parameter),__max(parameter), __incremento"""
    def __init__(self,minimo,maximo):
        self.__temperatura = 5
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
        if self.__temperatura < self.__max:
            self.__temperatura += self.__incremento
    def MenosMorno(self):
        if(self.__temperatura > self.__min):
            self.__temperatura -= self.__incremento
           #ka
