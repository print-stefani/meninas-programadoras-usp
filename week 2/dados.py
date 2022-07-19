#Programa que conta os pontos de dado de 6 faces, distribuido em 9 posições (3 linhas e 3 colunas)

#instrução
print ("Digite 0 - sem ponto ou 1 - ponto, em cada linha")

#leitura das posições
linha_1 = [int (i) for i in input().split()]
linha_2 = [int (i) for i in input().split()]
linha_3 = [int (i) for i in input().split()]

#comprimento total da face 
total = len (linha_1 or linha_2 or linha_3)

#estrutura de repetição, i = inicio, analise do total
for i in range (total):
  
  #contar todos 1 em cada face
  total_1 = linha_1 .count (1)
  total_2 = linha_2 .count (1)
  total_3 = linha_3 .count (1)
  
  #soma o total em toda a face
  soma = total_1 + total_2 + total_3
  
print (soma)
