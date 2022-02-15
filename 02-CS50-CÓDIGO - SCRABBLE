#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

    // DOIS JOGADORES DIGITAM SUAS PALAVRAS, GANHA PALAVRA COM MAIOR PONTUAÇÃO
    // PONTOS CONFORME AS LETRAS DO ALFABETO

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int compute_score(string word);
int main(void)

{
        // CADA JOGADOR DIGITA UMA PALAVRA
        string word1 = get_string("Jogador 1 digite a sua palavra: ");
        string word2 = get_string("Jogador 2 digite a sua palavra: ");

    // PONTOS DAS PALAVRAS
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // IMPRIMI PALAVRA GANHADORA
    // GANHA MAIOR PONTUAÇÃO

    if (score1 == score2)
    {
        printf("Empatou!\n");
    }
    else if (score1 > score2)
    {
        printf("Jogador 1 você venceu!\n");
    }
    else
    {
        printf("Jogador 2 você venceu!\n");
    }
}
int compute_score(string word)
{
    // PONTUAÇÃO
    int score = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (islower(word[i]))
        {
            // VALORES ASCII LETRAS 
            score += POINTS[word[i] - 'a'];
        }
        else if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
    }
return score;
}
