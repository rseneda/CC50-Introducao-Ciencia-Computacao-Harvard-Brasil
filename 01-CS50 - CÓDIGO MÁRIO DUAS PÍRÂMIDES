#include <cs50.h>

#include <stdio.h>

void print(char c, int n);

 

int main(void)

{

    int n;

    do

    {

        n = get_int("height: ");

    } while (n < 1 || n > 8);

   

    for (int i = 0;  i < n; i++)

   

    {

        print(' ', n - 1 - i);

        print('#', i + 1);

        print(' ', 2);

        print('#', i + 1);

        

        printf("\n");

    }

}

 

void print(char c, int n)

{

    for (int i = 0; i < n; i++)

    {

        printf("%c", c);

    }

}
