#Programa que recebe a pontuação de dois times ao final de um set verificando se acabou a partida

#leitura das informações do usuario
time_1  =  int ( input ( "Digite os pontos do tempo 1: " ))
time_2  =  int ( input ( "Digite os pontos do tempo 2: " ))

#calculo da diferença de pontos entre os times
diferenca  =  time_1  -  time_2
diferenca_2  =  hora_2  -  hora_1

#condição de verificação se o set acaba ou não
if ( time_1  ==  25  ou  time_2  ==  25 ) e ( diferenca  >  2  ou  diferenca_2  >  2 ):
  print ( 'Sim, o set acabou' )
mais :
  print ( 'Não, o set continua' )
