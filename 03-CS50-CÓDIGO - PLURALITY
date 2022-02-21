#include <cs50.h>
#include <stdio.h>
#include <string.h>

// NUMERO MAXIMO DE CANDIDATOS
#define MAX 9

// NOME E CONTAGEM DEM VOTOS
typedef struct
{
    string name;
    int votes;
}
candidate;

// ARRAY DE CANDIDATOS
candidate candidates[MAX];

// NUMERO DE CANDIDATOS
int candidate_count;

// PROTOTIPOS DE FUNCAO
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // VERIFIQUE INVALIDADE
    if (argc < 2)
    {
        printf("MÍNIMO DOIS CANDIDATOS\n");
        return 1;
    }

    // MATRIZ DE CANDIDATOS
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("NUMERO MAXIMO DE CANDIDATOS É %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("NUMERO DE ELEITORES: ");

    // LOOP ELEITORES
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("VOTO: ");

        // CHECAR VOTO VÁLIDO
        if (!vote(name))
        {
            printf("VOTO INVÁLIDO.\n");
        }
    }

    // VENCEDOR DA ELEIÇÃO
    print_winner();
}

// NOVA VOTAÇÃO
bool vote(string name)
{

    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// IMPRIMI QUEM GANHOU
void print_winner(void)
{
    int max_value = candidates[0].votes;

    //PROCURA MAXIMO DE VOTOS
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > max_value)
        {
            max_value = candidates[i].votes;
        }
    }

    // IMPRIMI TODOS VENCEDORES COM MÁXIMO DE VOTOS
    for (int i = 0; i < candidate_count; i++)
    {

        if (candidates[i].votes == max_value)
        {
            printf("RESULTADO %s\n", candidates[i].name);
        }
    }

    return;
}
