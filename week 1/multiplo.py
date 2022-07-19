#Programa que lê dois valores inteiros e verifica caso seja multiplo, caso não devolver "tente de novo"

#leitura dos dados
num_1 = int (input("Numero inteiro: "))
num_2 = int (input("Numero inteiro: "))

#estrutura de condições
if num_1 % num_2 == 0:
  #saida caso seja multiplo - verdadeiro
  print (num_1, "é múltiplo de", num_2)
else:
  #saida caso não seja multiplo - falso
  print ("tente de novo")
