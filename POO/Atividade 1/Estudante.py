class Estudante():
    """attributes:nome,matricula,creditos"""
    def __init__(self,nome,matricula,creditos): #Construtor
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = creditos
    #Adicionar Creditos
    def addCreditos(self,quantidade):
        self.__creditos += quantidade
    #Métodos acessores
    def setNome(self,novo_nome):
        self.__nome = novo_nome
    def getNome(self):
        return self.__nome
    def getCreditos(self):
        return self.__creditos
