class Aquecedor12():
    """attributes: __temperatura"""
    def __init__(self):
        self.__temperatura = 15
    def getTemperatura(self):
        return self.__temperatura
    def setTemperatura(self,new_temp):
        self.__temperatura = new_temp
    def MaisMorno(self):
        self.__temperatura += 5
    def MenosMorno(self):
        self.__temperatura -= 5
