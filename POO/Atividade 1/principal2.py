from Estudante import Estudante
def main():
    #Aluno 01 BEGIN
    aluno01 = Estudante("Carlos",2017,4)
    aluno01.setNome("Juricleison")
    print(aluno01.getNome())
    aluno01.addCreditos(20)
    print(aluno01.getCreditos())
    #Aluno 01 END
    
    #Aluno 02 BEGIN
    aluno02 = Estudante("Catapora",1234659,244)
    aluno02.addCreditos(48)
    print(aluno02.getCreditos())
    #Aluno 02 END
    
if __name__ == "__main__":
    main()
