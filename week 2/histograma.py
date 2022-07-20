#Programa que le uma sequencia de numeros (conjunto de inteiros) de uma linha. Assim, cada numero inteiro positivo e par - devolver asteristicos, se for impar - devolve pontos.

#Instrução
print ("Digite uma sequencia de valores inteiros entre 0 e 20")

#leitura dos valores
valor = [int (i) for i in input ("Digite a sequencia de numeros:\n") .split()]

#estrutura de repetição da sequencia
for i in valor:
  resultado = ''
  
  #condição caso o valor seja par
  if (i % 2 == 0):
    #estrutura de repetição - contagem dos aesteristicos
    for j in range (i):
      resultado += '*'
  else:
    #estrutura de repetição - contagem dos pontos
    for j in range (i):
      resultado += '.'
      
  print (resultado)
