#Programa que le nomes dos times e , saida do time vitorioso e os sets jogados

#leitura dos dados - times
T1 = input ("Nome do time 1: ")
T2 = input ("Nome do time 2: ")

#leitura dos pontos de cada time
pontos_T1 = [int (i) for i in input("Pontos do set - time 1:\n") .split ()]
pontos_T2 = [int (i) for i in input("Pontos do set - time 2:\n") .split ()]

#total de numero de sets/jogos
numero_de_jogos = len (pontos_T1 or pontos_T2)

#variaveis contadoras iniciais de vitorias dos sets
vitoria_T1 = 0
vitoria_T2 = 0

#estrutura de repetição - contagem do numero de jogos
for i in range (numero_de_jogos):
  
  #estrutura de condição para contagem de vitorias de cada time
  if (pontos_T1 [i] > pontos_T2 [i]):
    vitoria_T1 += 1
  else:
    vitoria_T2 += 1
    
#estrutura condicional para verificar o time vencedor
if vitoria_T1 > vitoria_T2:
  print (T1, '(total', numero_de_jogos, 'sets)')
else:
    print (T2, '(total', numero_de_jogos, 'sets)')
