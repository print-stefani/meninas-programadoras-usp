#Programa que le uma linha com um número indeterminado de valores entre 0 e 9, usando o metodo count().

#Instruções
print ("Digite valores entre 0 e 9\n")

#leitura dos valores
lista = [int(i) for i in input().split()]

#estrutura de repetição contado a ocorrencia mais de uma vez de um numero
for i in range (10):
  print (i, lista.count(i))
