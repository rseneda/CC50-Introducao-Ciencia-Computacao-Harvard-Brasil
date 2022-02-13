#include <cs50.h>
#include <stdio.h>
#include <math.h>

    // AMERICAN 15 DIGITOS, INICIO 34 OU 37
    // VISA 13 OU 16 DIGITOS, INICIO 4
    // MASTER 16 DIGITOS, INICIO 51, 52, 53, 54 OU 55

bool checksum(long number, int len)
{
    int sum1 = 0, sum2 = 0;
    for (int i=0; i < len; i++)
    {
       
        int digit = number % 10; //checar numero
        number /= 10; //tira ultima casa
       
        if (i % 2 == 0) //pares
        {
            sum2 += digit;
        }
        else //impares
        {
            digit *= 2;
            if (digit > 9)
            {
               
                sum1 += (digit / 10) + (digit % 10);
            }
            else
            {
                sum1 += digit;
            }
        }
    }
   
    int sum = sum1 + sum2;
   
    if (sum % 10 == 0)
    { return true;  }
    else
    { return false; }
}

int main(void)
{
   long credit = get_long("numero sem ponto ou traço: ");
   int len = 0;
   long n = credit;
   do
   {
       n /= 10;
       len++;
   }
   while (n > 0);
   
   bool check = checksum(credit, len);
   
   //passou checksum
   if (check)
   {
       int two = (credit / (long)pow(10, len - 2));
       int one = (credit / (long)pow(10, len - 1));
       
       // american
       if (len == 15)
       {
           if (two == 34 || two == 37)
            {
           printf("amex\n");
            }
       else { printf("invalid\n"); }
        }
        else if (len == 16) // mastercard or visa
            {
            if (one == 4)
            {
                printf("visa\n");
            }
        else if (two > 50 && two < 56)
            {
                printf("mastercard\n");
            }
                else    { printf("invalid\n"); }
        }
        else if (len == 13) // visa
            {
                if (one == 4)
                {
                printf("visa\n");
                }
                else {printf("invalid\n");}
            }
        else
            {
            printf("invalid\n");
            }
   }
    else
    {
      printf("invalid\n");  
    }
}
