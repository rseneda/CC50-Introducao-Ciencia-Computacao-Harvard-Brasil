#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Coloque o nome do arquivo de imagem\n");
        return 1;
    }

    char *infile = argv[1];

    // Abrir arquivo
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Não pode abrir\n");
        return 2;
    }

    unsigned char buffer[512];
    char filename[8];
    int img_num = 0;

    // Criar arquivo
    FILE *outptr;
    bool jpeg = false;

    // Memória
    while (fread(buffer, sizeof(buffer), 1, inptr))
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpeg)
            {
                fclose(outptr);
                jpeg = false;
            }
            sprintf(filename, "%03i.jpg", img_num);
            outptr = fopen(filename, "w");
            fwrite(buffer, sizeof(buffer), 1, outptr);
            jpeg = true;
            img_num++;
        }
        else
        {
            if (jpeg)
            {
                fwrite(buffer, sizeof(buffer), 1, outptr);
            }
        }
    }

    fclose(inptr);
    fclose(outptr);

 return 0;
}
