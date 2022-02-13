#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int x, y;
    int anos = 0;
   
    //QUANTIDADE INICIAL DE POPULAÇÃO - x
    //SOLICITA VALOR INICIAL MAIOR QUE 9
        do
        {
        x = get_int("populacao inicial: ");
        }
        while (x < 9);
       
    //QUANTIDADE FINAL DE POPULAÇÃO - y
    //SOLICITA VALOR IGUAL OU MAIOR QUE INICAL
        do
        {
        y = get_int("populacao fim: ");
        }
        while (y < x);
       
     //CALCULO 1 ANO
            {
            if (x >= y)
            printf("%d\n", x + (x/3 - x/4));
            }

                //QUANTOS ANOS PARA ATINGIR POPULAÇÃO
                {printf("%d\n", (y-x) / (x + (x/3 - x/4)));}
}
