#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Bytes
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Usar input.wav e output.wav\n");
        return 1;
    }

    // Abrir arquivo e determinar fator
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Não foi possível abrir arquivo.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Não foi possível abrir arquivo.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // Copiar cabeçalho do arquivo de entrada para o arquivo de saída
    uint8_t byte_buffer[HEADER_SIZE];
  if (fread(byte_buffer, sizeof(uint8_t), HEADER_SIZE, input))
  {
    fwrite(byte_buffer, sizeof(uint8_t), HEADER_SIZE, output);
  }

    //Dados Atualizados
    uint16_t two_byte_buffer;
  while (fread(&two_byte_buffer, sizeof(uint16_t), 1, input))
  {
    two_byte_buffer *= (uint16_t)factor;
    fwrite(&two_byte_buffer, sizeof(uint16_t), 1, output);
  }

    // Fechar Arquvios
    fclose(input);
    fclose(output);
}
