#Programa de caça-palavras, precisamos saber quais palavras queremos caçar e em que matriz de letras vamos busca-las.

#variavel a procurar
palavra = input ("Digite a palavra que deseje procura: ")

#lista de palavras
caca_palavra = [str (i) for i in input().split()]

#Estrutura de condição 
if palavra in caca_palavra:
  achou = caca_palavra.index(palavra)
  print (palavra, achou)
else:
  print ("falta", palavra)
