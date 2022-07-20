# Programa que le os pontos de uma partida de volei. Cada ponto será contado por linha, sendo 1 - time 1 e 2 - time 2

#Instruções
print ("Para contar os pontos marcados na partida:\nDigite 1 - ponto para time 1\nDigite 2 - ponto para time 2\n")

#variaveis de contagem
soma_1 = 0
soma_2 = 0

#variavel da diferença dos pontos
diferenca = 0

#estrutura de repetição - while, enquanto a soma for menor que 25 ou a diferença for menor que 2
while ((soma_1 < 25 and soma_2 < 25) or diferenca < 2):
  #o programa pedira os pontos
  entrada = int(input())
  
  #se digitar 1 - pontos para time 1
  if(entrada == 1):
    soma_1 += 1
  #se digitar 2 - pontos para time 2 
  elif(entrada == 2):
    soma_2 += 1
  else:
    print ("Opção invalida!... tente de novo")
    
  #se os pontos do time 1 for maior que o do time 2, calcular a diferença 
  if(soma_1 > soma_2):
    diferenca = soma_1 - soma_2
  else:
    #se não, calcular a diferença dos pontos do time 2 e do time 1
    diferenca = soma_2 - soma_1
    
#resultado final do set/partida
print (soma_1,'x',soma_2)
