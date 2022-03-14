from cs50 import get_string

text = get_string("Insira seu texto: ")

letters = 0
words = 1
sentences = 0

for char in text:
  if char.isalpha():
    letters += 1
  if char.isspace():
    words += 1
  if char == '.' or char == '!' or char == '?':
    sentences += 1

l = letters * 100 / words
s = sentences * 100 / words
index = 0.0588 * l - 0.296 * s - 15.8

if index < 1:
  print("Antes da Grade 1")
elif index > 16:
  print("Grade 16+")
else:
  print(f"Grade {int(index)}")
