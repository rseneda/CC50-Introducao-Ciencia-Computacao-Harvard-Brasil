#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float quarters = 0.25;
    float dimes = 0.10;
    float nickles = 0.05;
    float pennies = 0.01;
    float change = 0.00;
    int count = 0;
    do
    {
        change = get_float("Change owed: ");

    }
    while (change < 0);

   do
   {
       change -= quarters;
       count++;
   }
    while (change >= 0.25);

    printf("%f\n", change);
   do
   {
       change -= dimes;
       count++;
   }
    while (change >= 0.10);


    do
   {
       change -= nickles;
       count++;
   }
    while (change >= 0.05);


    do
   {
       change -= pennies;
       count++;
   }
    while (change >= 0.01);


printf("%i\n", count);
printf("%f\n", change);

}
