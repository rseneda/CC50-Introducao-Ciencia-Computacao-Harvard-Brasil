#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

// NUMERO MAXIMO DE CANDIDATOS E VOTOS
#define MAX_CANDIDATES 9
#define MAX_VOTERS 100

// PREFERENCIAS DE VOTOS E CANDIDATOS
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// NOME E CONTAGEM DEM VOTOS
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// ARRAY DE CANDIDATOS
candidate candidates[MAX_CANDIDATES];

// NUMERO DE CANDIDATOS E VOTOS
int voter_count;
int candidate_count;

// PROTOTIPOS DE FUNCAO
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // VERIFIQUE INVALIDADE
    if (argc < 2)
        {
        printf("COLOQUE NOMES DOS CANDIDATOS DO SEGUNDO TURNO.\n");
        return 1;
        }

    // MATRIZ DE CANDIDATOS
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
        {
        printf("NUMERO MAXIMO DE CANDIDATOS É %i\n", MAX_CANDIDATES);
        return 2;
        }
        for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }
        
        voter_count = get_int("NUMERO DE ELEITORES: ");
        if (voter_count > MAX_VOTERS)
        {
        printf("NUMERO MAXIMO DE ELEITORES É %i\n", MAX_VOTERS);
        return 3;
        }
    
    // LOOP ELEITORES
    for (int i = 0; i < voter_count; i++)
    {
        //CONSULTA CLASSIFICAÇÃO
        for (int j = 0; j < candidate_count; j++)
        {
        string name = get_string("CLASSIFICAÇÃO %i: ", j + 1);
        if (!vote(i, j, name))
            {
                printf("VOTO INVALIDO.\n");
                return 4;
            }
        }
    printf("\n");
        
    }
    
    while (true)
    {
    //VOTOS CANDIDATOS RESTANTES
    tabulate();
    
    bool won = print_winner();
    if (won)
        {
        break;
        }
   
    //ELIMINAR CANDIDATOS EM ULTIMO LUGAR
        int min = find_min();
        bool tie = is_tie(min);
    
    // EMPATE, TODOS GANHAM
        if (tie)
    
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }
        
        //ELIMINE NUMERO MINIMO DE VOTOS
        eliminate(min);
        
         for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
   }
     return 0;
}

// PREFERENCIA DE REGISTRO DE VOTO VÁLIDO
    bool vote(int voter, int rank, string name)

  {
    bool exist = false;
    for (int i = 0; i < candidate_count; i++)
        {
        if (strcmp(name, candidates[i].name) == 0)
            {
            preferences[voter][rank] = i;
            exist = true;
            break;
            }
         }
    return exist;
    }
     
// CANDIDATOS NÃO ELIMINADOS
void tabulate(void)
        
     {
    for (int i = 0; i < voter_count; i++)
        {
        for (int j = 0; j < candidate_count; j++)
            {
            if (candidates[preferences[i][j]].eliminated == false)
                {
                candidates[preferences[i][j]].votes += 1;
                break;
                }
            }
        }
    return;
    }

// IMPRIMIR VENCEDOR
bool print_winner(void)
    {
    for (int i = 0; i < candidate_count; i++)
        {
        string most = candidates[i].name;
        if (candidates[i].votes > voter_count / 2)
            {
            printf("%s\n", most);
            return true;
            }
        }
    return false;
    }
        
// DEVOLVE VOTOS RESTANTES
int find_min(void)
    {
    int minvotes = voter_count;
    for (int i = 0; i < candidate_count; i++)
        {   
        if (candidates[i].eliminated == false && candidates[i].votes < minvotes)
            {
            minvotes = candidates[i].votes;
            }
        }
    return minvotes;
    }
bool is_tie(int minvotes)
    {
    for (int i = 0; i < candidate_count; i++)
        {
        if (candidates[i].eliminated == false && candidates[i].votes != minvotes)
            {
            return false;
            }
        }
    return true;
    }
    
// ELIMINAR CANDIDATOS
void eliminate(int minvotes)
    {
    for (int i = 0; i < candidate_count; i++)
        if (candidates[i].votes == minvotes)
        {
            candidates[i].eliminated = true;
        }
    return;
    }
