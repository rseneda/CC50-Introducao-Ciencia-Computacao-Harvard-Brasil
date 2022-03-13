#include <math.h>
#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      RGBTRIPLE rgb = image[i][j];
      int avg = (rgb.rgbtRed + rgb.rgbtGreen + rgb.rgbtBlue) / 3;

      RGBTRIPLE newrgb;
      newrgb.rgbtRed = avg;
      newrgb.rgbtGreen = avg;
      newrgb.rgbtBlue = avg;

      image[i][j] = newrgb;
    }
  }
  return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width; j++)
    {
      RGBTRIPLE rgb = image[i][j];
      BYTE originalRed = rgb.rgbtRed;
      BYTE originalGreen = rgb.rgbtGreen;
      BYTE originalBlue = rgb.rgbtBlue;

      float sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
      float sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
      float sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;

      RGBTRIPLE newrgb;
      newrgb.rgbtRed = sepiaRed > 255 ? 255 : sepiaRed;
      newrgb.rgbtGreen = sepiaGreen > 255 ? 255 : sepiaGreen;
      newrgb.rgbtBlue = sepiaBlue > 255 ? 255 : sepiaBlue;

      image[i][j] = newrgb;
    }
  }
  return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < width / 2; j++)
    {
      RGBTRIPLE temp = image[i][j];
      image[i][j] = image[i][width - j];
      image[i][width - j] = temp;
    }
  }
  return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  RGBTRIPLE aux[height + 2][width + 2];

  for (int i = 0; i < height + 2; i++)
  {
    for (int j = 0; j < width + 2; j++)
    {
      if (i == 0 || i == height + 1 || j == 0 || j == width + 1)
      {
        RGBTRIPLE newrgb;
        newrgb.rgbtRed = 0;
        newrgb.rgbtGreen = 0;
        newrgb.rgbtBlue = 0;

        aux[i][j] = newrgb;
      }
      else
        aux[i][j] = image[i - 1][j - 1];
    }
  }

  for (int i = 1; i < height + 1; i++)
  {
    for (int j = 1; j < width + 1; j++)
    {
      RGBTRIPLE newrgb;
      RGBTRIPLE tl = aux[i - 1][j - 1];
      RGBTRIPLE tc = aux[i - 1][j + 0];
      RGBTRIPLE tr = aux[i - 1][j + 1];
      RGBTRIPLE ml = aux[i + 0][j - 1];
      RGBTRIPLE mr = aux[i + 0][j + 1];
      RGBTRIPLE bl = aux[i + 1][j - 1];
      RGBTRIPLE bc = aux[i + 1][j + 0];
      RGBTRIPLE br = aux[i + 1][j + 1];

      int div = 8;

      if (i == 1 || i == height || j == 1 || j == width)
        div = 5;
      if ((i == 1 && (j == 1 || j == width)) || (i == height && (j == 1 || j == width)))
        div = 3;

      BYTE blurRed = (tl.rgbtRed + tc.rgbtRed + tr.rgbtRed + ml.rgbtRed + mr.rgbtRed + bl.rgbtRed + bc.rgbtRed + br.rgbtRed) / div;
      BYTE blurGreen = (tl.rgbtGreen + tc.rgbtGreen + tr.rgbtGreen + ml.rgbtGreen + mr.rgbtGreen + bl.rgbtGreen + bc.rgbtGreen + br.rgbtGreen) / div;
      BYTE blurBlue = (tl.rgbtBlue + tc.rgbtBlue + tr.rgbtBlue + ml.rgbtBlue + mr.rgbtBlue + bl.rgbtBlue + bc.rgbtBlue + br.rgbtBlue) / div;

      newrgb.rgbtRed = blurRed;
      newrgb.rgbtGreen = blurGreen;
      newrgb.rgbtBlue = blurBlue;

      image[i][j] = newrgb;
    }
  }
  return;
}

// Edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
  RGBTRIPLE aux[height + 2][width + 2];

  for (int i = 0; i < height + 2; i++)
  {
    for (int j = 0; j < width + 2; j++)
    {
      if (i == 0 || i == height + 1 || j == 0 || j == width + 1)
      {
        RGBTRIPLE newrgb;
        newrgb.rgbtRed = 0;
        newrgb.rgbtGreen = 0;
        newrgb.rgbtBlue = 0;

        aux[i][j] = newrgb;
      }
      else
        aux[i][j] = image[i - 1][j - 1];
    }
  }

  for (int i = 1; i < height + 1; i++)
  {
    for (int j = 1; j < width + 1; j++)
    {
      RGBTRIPLE newrgb;
      RGBTRIPLE tl = aux[i - 1][j - 1];
      RGBTRIPLE tc = aux[i - 1][j + 0];
      RGBTRIPLE tr = aux[i - 1][j + 1];
      RGBTRIPLE ml = aux[i + 0][j - 1];
      RGBTRIPLE mr = aux[i + 0][j + 1];
      RGBTRIPLE bl = aux[i + 1][j - 1];
      RGBTRIPLE bc = aux[i + 1][j + 0];
      RGBTRIPLE br = aux[i + 1][j + 1];

      float GxRed = (tl.rgbtRed * -1 + tc.rgbtRed * 0 + tr.rgbtRed * 1 +
                     ml.rgbtRed * -2 + mr.rgbtRed * 2 +
                     bl.rgbtRed * -1 + bc.rgbtRed * 0 + br.rgbtRed * 1);
      float GxGreen = (tl.rgbtGreen * -1 + tc.rgbtGreen * 0 + tr.rgbtGreen * 1 +
                       ml.rgbtGreen * -2 + mr.rgbtGreen * 2 +
                       bl.rgbtGreen * -1 + bc.rgbtGreen * 0 + br.rgbtGreen * 1);
      float GxBlue = (tl.rgbtBlue * -1 + tc.rgbtBlue * 0 + tr.rgbtBlue * 1 +
                      ml.rgbtBlue * -2 + mr.rgbtBlue * 2 +
                      bl.rgbtBlue * -1 + bc.rgbtBlue * 0 + br.rgbtBlue * 1);

      float GyRed = (tl.rgbtRed * -1 + tc.rgbtRed * -2 + tr.rgbtRed * -1 +
                     ml.rgbtRed * -0 + mr.rgbtRed * 0 +
                     bl.rgbtRed * 1 + bc.rgbtRed * 2 + br.rgbtRed * 1);
      float GyGreen = (tl.rgbtGreen * -1 + tc.rgbtGreen * -2 + tr.rgbtGreen * -1 +
                       ml.rgbtGreen * -0 + mr.rgbtGreen * 0 +
                       bl.rgbtGreen * 1 + bc.rgbtGreen * 2 + br.rgbtGreen * 1);
      float GyBlue = (tl.rgbtBlue * -1 + tc.rgbtBlue * -2 + tr.rgbtBlue * -1 +
                      ml.rgbtBlue * 0 + mr.rgbtBlue * 0 +
                      bl.rgbtBlue * 1 + bc.rgbtBlue * 2 + br.rgbtBlue * 1);

      float red = sqrtf(powf(GxRed, 2) + powf(GyRed, 2));
      float green = sqrtf(powf(GxGreen, 2) + powf(GyGreen, 2));
      float blue = sqrtf(powf(GxBlue, 2) + powf(GyBlue, 2));

      newrgb.rgbtRed = red > 255 ? 255 : red;
      newrgb.rgbtGreen = green > 255 ? 255 : green;
      newrgb.rgbtBlue = blue > 255 ? 255 : blue;

      image[i][j] = newrgb;
    }
  }
  return;
}
