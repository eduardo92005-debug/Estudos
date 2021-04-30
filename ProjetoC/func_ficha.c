#include <ncurses.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STR_TAM 10
#define MAT_TAM 10
#define NOME_TAM 14
#define COL_TAM_HORAS 1
#define LIN_TAM_DIAS 5
#define MAX_ITERACAO 10
#define ARQ_MAXTAM 32
#define QNTD_VAGAS 10
#define FUNC_NULO '1'
#define LINHAS_MAX 20
#define CHAR_MAX 34

//GLOBAIS
typedef struct ficha_funcionario
{
    char nome[NOME_TAM];
    int matricula;
    float banco_horas[COL_TAM_HORAS][LIN_TAM_DIAS];
    float frequencia;
    char status[10];
} FICHA;
FICHA funcionario[QNTD_VAGAS];
int globalnum_func;
// GLOBAIS

//Protótipos das funcoes
int qntdLinhas(FILE *arquivo);

void limpaTela();

void preencheVetor(FICHA func[]);

void zeraFicha(FICHA func);

int idle(void);

int buscaFuncPorMatricula(int matricula);

int tamanho_vetor(char vetor[]);

void liberaMem(FILE *arquivo);

bool verificaArq(FILE *arquivo, char nome_arquivo[]);

bool existeMatriculaArq(FILE *arquivo, int matricula);

char Menu(void);

void atualizaCadastro(int matricula, char nome[]);

int cadastroFuncionario(void);

int removeFuncionario(int matricula);

void cadastroHoras(int matricula);

void exibeFuncionario(int matricula);

void adimplentesEinadimplentes(void);

void relatorios(void);
//FIM PROTOTIPO

int qntdLinhas(FILE *arquivo)
{
    arquivo = fopen("Cadastro.txt", "r");
    int linhas = 0;
    char texto[10];
    char final_texto;

    linhas++;
    while ((final_texto = fgetc(arquivo)) != EOF)
    {
        if (final_texto == '\n')
            linhas++;
    }
    fclose(arquivo);
    return linhas;
}

void limpaTela()
{
    system("clear");
}

void preencheVetor(FICHA func[])
{
    for (int i = 0; i < 2; i++)
    {
        func[i].matricula = 000000000;
        func[i].frequencia = 0.0;
        func[i].nome[0] = FUNC_NULO;

        for (int x = 0; x < COL_TAM_HORAS; x++)
        {
            for (int y = 0; y < LIN_TAM_DIAS; y++)
            {
                func[i].banco_horas[x][y] = 0.0;
            }
        }
    }
}

void zeraFicha(FICHA func)
{

    func.matricula = 0;
    func.frequencia = 0.0;
    for (int j = 1; j < NOME_TAM; j++)
    {
        func.nome[0] = FUNC_NULO;
        func.nome[j] = '\0';
    }
    for (int x = 0; x < COL_TAM_HORAS; x++)
    {
        for (int y = 0; y < LIN_TAM_DIAS; y++)
        {
            func.banco_horas[x][y] = 0.0;
        }
    }
}

int idle(void)
{
    return 0;
}

int buscaFuncPorMatricula(int matricula)
{
    signed int busca_falha = -1;
    for (int i = 0; i < globalnum_func; i++)
    {
        bool checagem = (funcionario[i].matricula == matricula);
        if (checagem)
        {
            return i;
        }
    }
    return busca_falha;
}

int tamanho_vetor(char vetor[])
{
    int tam_vetor;
    tam_vetor = strlen(vetor);

    return tam_vetor;
}

void liberaMem(FILE *arquivo)
{

    fflush(arquivo);
    fflush(stdin);
    fclose(arquivo);
}

bool verificaArq(FILE *arquivo, char nome_arquivo[])
{
    arquivo = fopen("Cadastro.txt", "w+");
    if (arquivo != NULL)
    {
        liberaMem(arquivo);
        return true;
    }
    else
    {
        liberaMem(arquivo);
        return false;
    }
}

bool existeMatriculaArq(FILE *arquivo, int matricula)
{
    char str[STR_TAM];

    arquivo = fopen("Cadastro.txt", "r");
    while (!feof(arquivo))
    {
        char *saida_arq = fgets(str, MAT_TAM, arquivo);
        if (saida_arq)
        {
            int texto_para_matricula = atoi(str);
            if ((matricula == texto_para_matricula))
            {
                return TRUE;
            }
            else
            {
                idle();
            }
        }
    }
    liberaMem(arquivo);
}

char Menu(void)
{
    char str[STR_TAM];

    printf("MENU PRINCIPAL\n");
    printf("1 - Cadastro de funcionario\n");
    printf("2 - Remover funcionario\n");
    printf("3 - Atualizar dados\n");
    printf("4 - Relatorios\n");
    printf("5 - Consultar funcionario\n");
    printf("6 - Sair\n");
    printf("DIGITE A OPÇÃO DESEJADA\n");
    fgets(str, STR_TAM, stdin);
    printf("Pressione <ENTER> para contiuar!");
    getchar();
    limpaTela();
    return str[0];
}

void atualizaCadastro(int matricula, char nome[])
{
    FILE *arquivo;
    FILE *novo_arq;
    char matricula_para_texto[10];
    char matrix_str[15][10];
    int tam_nome, tam_matricula, linhas;

    sprintf(matricula_para_texto, "%i", matricula);
    arquivo = fopen("Cadastro.txt", "r");
    novo_arq = fopen("Cadastro1.txt", "w+");
    tam_nome = tamanho_vetor(nome);
    tam_matricula = tamanho_vetor(matricula_para_texto);
    linhas = qntdLinhas(arquivo);
    if (arquivo != NULL)
    {
        for (int i = 0; i < linhas; i++)
        {

            fgets(matrix_str[i], sizeof matrix_str[i], arquivo);
            for (int j = 0; j < 1; j++)
            {
                char string_comparacao[10];
                strncpy(string_comparacao, matrix_str[i], 10);
                if (strncmp(string_comparacao, nome, tam_nome) == 0)
                {
                    break;
                }
                if (strncmp(string_comparacao, matricula_para_texto, tam_matricula) == 0)
                {
                    break;
                }
                fputs(matrix_str[i], novo_arq);
            }
        }
    }
    setbuf(arquivo, 0);
    remove("Cadastro.txt");
    rename("Cadastro1.txt", "Cadastro.txt");
    fflush_unlocked(arquivo);
    liberaMem(arquivo);
    liberaMem(novo_arq);
}

int cadastroFuncionario(void)

{
    FILE *arquivo;
    char str[STR_TAM], opcao, matricula_para_texto[MAT_TAM + 1];
    FICHA *func;

    fflush(stdin);
    if (verificaArq(arquivo, "Cadastro.txt"))
    {
        arquivo = fopen("Cadastro.txt", "a+");
    }
    else
    {
        arquivo = fopen("Cadastro.txt", "w");
    }
    func = funcionario;
    while (opcao != 'N' && opcao != 'n')
    {
        globalnum_func++;

        printf("\n Digite seu nome: ");
        scanf("%14s", func->nome);
        fflush(stdin);
        printf("\n*(Ate 8 números) Digite sua matricula: ");
        scanf("%10d", &func->matricula);
        if (!existeMatriculaArq(arquivo, func->matricula))
        {
            fputs("Nome: \n", arquivo);
            fputs(func->nome, arquivo);
            fputc('\n', arquivo);
            fputs("Matricula: ", arquivo);
            fprintf(arquivo, "\n%i", func->matricula);
            fputs("\nFrequencia: ", arquivo);
            fprintf(arquivo, "\n%f", func->frequencia);
            fputs("\nStatus: ", arquivo);
            fputs(strcpy(func->status, "\nCadastrado!\n"), arquivo);
            fputc('\n', arquivo);
            (*&func)++;
            printf("Deseja cadastrar mais algum funcionario? (Qualquer tecla para Sim/N para nao): ");
            scanf("%s", str);
            opcao = str[0];
        }
        else
        {
            printf("Erro: Matrícula já cadastrada!\n");
            break;
        }
    }
    liberaMem(arquivo);
}

int removeFuncionario(int matricula)
{
    FICHA *func;
    FILE *arquivo;
    int busca_sucesso;

    if (verificaArq(arquivo, "Demitidos.txt"))
    {
        arquivo = fopen("Demitidos.txt", "a+");
    }
    else
    {
        arquivo = fopen("Demitidos.txt", "w");
    }
    printf(" Digite a matricula do funcionario que deseja remover: ");
    scanf("%d", &matricula);
    busca_sucesso = buscaFuncPorMatricula(matricula);
    if (busca_sucesso != -1)
    {
        func = &funcionario[buscaFuncPorMatricula(matricula)];
        if (func->matricula != 0)
        {
            fputs("*****DEMITIDO*****\n", arquivo);
            fprintf(arquivo, "Nome: %s", func->nome);
            fprintf(arquivo, "Matricula: %d", func->matricula);
            fprintf(arquivo, "Frequencia: %f", func->frequencia);
            for (int i = 0; i < COL_TAM_HORAS; i++)
            {
                for (int j = 0; j < LIN_TAM_DIAS; j++)
                {
                    fprintf(arquivo, "Banco de horas: %.2f", func->banco_horas[i][j]);
                }
            }
            preencheVetor(func);
            atualizaCadastro(matricula, func->nome);
            printf("Removido com sucesso!\n");
            liberaMem(arquivo);
            return 0;
        }
    }
    printf("Não foi possivel remover, consulte o administrador!\n");
    liberaMem(arquivo);
    return -1;
}

void cadastroHoras(int matricula)
{
    float frequencia_local = 0.0;
    float frequencia_func;
    char dias[5][8] = {"Segunda", "Terca", "Quarta", "Quinta", "Sexta"};

    fflush(stdin);
    printf(" Digite a matricula do funcionario que deseja cadastrar horas: ");
    scanf("%d", &matricula);
    for (int i = 0; i < COL_TAM_HORAS; i++)
    {
        for (int j = 0; j < LIN_TAM_DIAS; j++)
        {
            float banco_horas_func = funcionario[buscaFuncPorMatricula(matricula)].banco_horas[i][j];
            printf(" Digite as horas trabalhadas no seguinte dia (%s): ", dias[j]);
            scanf("%f", &banco_horas_func);
            frequencia_local += ((banco_horas_func) / LIN_TAM_DIAS);
            frequencia_func = frequencia_local;
        }
    }
    funcionario[buscaFuncPorMatricula(matricula)].frequencia = frequencia_func;
}

void exibeFuncionario(int matricula)
{

    FICHA func;
    printf(" Digite a matricula do funcionario para a consulta: ");
    scanf("%d", &matricula);
    func = funcionario[buscaFuncPorMatricula(matricula)];
    if (func.matricula != 0)
    {
        printf("Nome: %s \n", func.nome);
        printf("Matricula: %d \n", func.matricula);
        printf("Media: %.2f \n", func.frequencia);
    }
}

void adimplentesEinadimplentes()
{
    FILE *adimplentes;
    FILE *inadimplentes;
    FICHA *func;

    adimplentes = fopen("Adimplentes.txt", "w+");
    inadimplentes = fopen("Inadimplentes.txt", "w+");
    if (verificaArq(adimplentes, "Adimplentes.txt") && verificaArq(inadimplentes, "Inadimplentes.txt"))
    {
        func = funcionario;
        for (int i = 0; i < globalnum_func; i++)
        {
            if (func->frequencia >= 5.0)
            {
                fputs(func->nome, adimplentes);
                fputc('\n', adimplentes);
                fprintf(adimplentes, "%d", func->matricula);
                fprintf(adimplentes, "%f", func->frequencia);
            }
            else if (func->frequencia == 0.0)
            {
                idle();
            }
            else
            {
                fputs(func->nome, inadimplentes);
                fputc('\n', inadimplentes);
                fprintf(inadimplentes, "%d", func->matricula);
                fprintf(inadimplentes, "%f", func->frequencia);
            }
            (*&func)++;
        }
    }
    liberaMem(adimplentes);
    liberaMem(inadimplentes);
}

void relatorios()
{
    char tipo_relatorio[15];
    FILE *arquivo;
    adimplentesEinadimplentes();
    printf(" Digite um tipo de relatorio ('C'adastro), ('D'emitidos), ('A'dimplentes), ('I'nadimplentes): ");
    scanf("%s", tipo_relatorio);
    switch (tipo_relatorio[0])
    {
    case 'C':
    {
        char texto[30];
        arquivo = fopen("Cadastro.txt", "r");
        for (int i = 0; i < qntdLinhas(arquivo); i++)
        {
            fgets(texto, 30, arquivo);
            printf("%s", texto);
        }
        liberaMem(arquivo);
        break;
    }
    case 'D':
    {
        char texto[30];
        arquivo = fopen("Demitidos.txt", "r");
        for (int i = 0; i < qntdLinhas(arquivo); i++)
        {
            fgets(texto, 30, arquivo);
            printf("%s", texto);
        }
        liberaMem(arquivo);
        break;
    }
    case 'A':
    {
        char texto[30];
        arquivo = fopen("Adimplentes.txt", "r");
        for (int i = 0; i < qntdLinhas(arquivo); i++)
        {
            fgets(texto, 10, arquivo);
            printf("%s", texto);
        }
        liberaMem(arquivo);
        break;
    }
    }
}

int main()
{

    int exit = 1;
    preencheVetor(funcionario);
    int opcao;
    do
    {
        switch (opcao = Menu())
        {
        case '1':
            cadastroFuncionario();
            break;
        case '2':
            removeFuncionario(0);
            break;
        case '3':
            cadastroHoras(0);
            break;
        case '4':
            relatorios();
            break;
        case '5':
            exibeFuncionario(0);
            break;
        case '6':
            exit = 0;
            break;
        default:
            idle();
            break;
        }
    } while (exit == 1);
    return 0;
}
