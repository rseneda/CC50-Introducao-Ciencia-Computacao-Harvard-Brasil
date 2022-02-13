#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
int letras = 0;
int palavras = 1;
int frases = 0;

        // USUÁRIO ENTRAR COM TEXTO
        string s = get_string("Insira seu texto: ");

        // VERIFICA CARACTERES
        for (int i = 0, n = strlen(s); i < n; i++)
       
        // VERIFICA LETRAS MAIUSCULAS E MINUSCULAS
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
        { letras++; }
       
        // VERIFICA ESPAÇO
        else if (s[i] == ' ')
        { palavras++; }
       
        // VERIFICA PONTUAÇÃO
        else if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        { frases++; }
       
// CALCULLO COLEMAN LIAU

float resultado = (0.0588 * letras / palavras * 100) - (0.296 * frases / palavras * 100) -15.8;
int a = (int) round(resultado);

        // IMPRIMIR RESULTADOS
        if (a > 1)
        { printf("Before Grade 1\n"); }
        else if (a < 20)
        { printf("Grade 16+\n"); }    
        else
        { printf("Grade %i\n", a); }
}
