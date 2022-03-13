#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Dois pais e dois alelos
typedef struct person
{
  struct person *parents[2];
  char alleles[2];
} person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
 srand(time(0));

  // Nova familia 3 gerações
  person *p = create_family(GENERATIONS);

  print_family(p, 0);

  free_family(p);
}

  // Familia individual
person *create_family(int generations)
{
  // Alocar meoria
  person *p = malloc(sizeof(person));

  // Parentes
  if (generations > 1)
  {
    // Historia com parentes
    p->parents[0] = create_family(generations - 1);
    p->parents[1] = create_family(generations - 1);

    p->alleles[0] = p->parents[0]->alleles[rand() % 2];
    p->alleles[1] = p->parents[1]->alleles[rand() % 2];
  }

  else
  {
    p->parents[0] = NULL;
    p->parents[1] = NULL;

    p->alleles[0] = random_allele();
    p->alleles[1] = random_allele();
  }

  // Nova pessoa
  return p;
}

void free_family(person *p)
{
  if (p == NULL)
    return;

  free_family(p->parents[0]);
  free_family(p->parents[1]);

  free(p);
}

void print_family(person *p, int generation)
{
  if (p == NULL)
    return;

  for (int i = 0; i < generation * INDENT_LENGTH; i++)
    printf(" ");

  printf("Geração %i, tipo sanguineo %c%c\n", generation, p->alleles[0], p->alleles[1]);
  print_family(p->parents[0], generation + 1);
  print_family(p->parents[1], generation + 1);
}
char random_allele()
{
  int r = rand() % 3;
  if (r == 0)
    return 'A';
  else if (r == 1)
    return 'B';
  else
    return 'O';
}
