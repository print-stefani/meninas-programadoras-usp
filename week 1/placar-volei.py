#Programa que le o nome de dois times e a pontuação dos mesmos, caso seja inicio de time, a saida é "inicio de jogo"

#leitura do nome dos times 
time_1 = input ("Nome do time 1: ")
time_2 = input ("Nome do time 2: ")

#leitura da pontuação
pontos_1 = int (input ("Pontos do time 1: "))
pontos_2 = int (input ("Pontos do time 2: "))

#verificação de condição
if pontos_1 or pontos_2 != 0:
  #saida do nome do time com sua pontuação
  print (time_1, pontos_1)
  print (time_2, pontos_2)
else:
  #caso a primeira condição seja falsa - inicio de jogo
  print (time_1, pontos_1)
  print (time_2, pontos_2)
  print ("início de jogo")
