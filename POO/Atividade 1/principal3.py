from Estudante import Estudante
def main():
    #Alunos
    k = 0
    alunos = [Estudante("Ronaldo",313,0),Estudante("Ricardo",932,3),Estudante("Felipe",333,1),Estudante("Raissa",321,1)]
    n = input("Digite o nome de um aluno")
    for i in alunos:
        if(n == i.getNome()):
            i.addCreditos(1)
        else:
            if(k >= len(alunos)-1):
                print("Aluno nao esta cadastrado")  
            k += 1
if __name__ == "__main__":
    main()
