#Programa que le um caractere e verifica se será movimento de um jopo ou não.

#leitura do caractere
tecla = input ()

#verificação do caractere e suas condições
if tecla == "a" or tecla == "A":
  print ("LEFT")
elif tecla == "w" or tecla == "W":
  print ("UP")
elif tecla == "s" or tecla == "S":
  print ("DOWN")
elif tecla == "d" or tecla == "D":
  print ("RIGHT")
else:
  #caso não seja A-W-S-D, não será movimento do jogo, logo será falso
  print ("?")
