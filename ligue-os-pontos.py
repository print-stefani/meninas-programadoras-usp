#Programa do jogo ligue os pontos, le as quatro faces do quadrado, só ganha se fechar o quadrado, caso não for fechado o valor deve ser E

print ("Jogo - Ligue os Pontos")
print ("Digite T (top), B (bottom), L (left), R (right) ou E (empty) se a linha correspondente estiver vazia")

#leitura dos lados do quadrados
qua_1 = input ()
qua_2 = input ()
qua_3 = input ()
qua_4 = input ()

#verificação das condições 
if qua_1 == "T" and qua_2 == "B" and qua_3 == "L" and qua_4 == "R":
  #quadrado fechado - jogador vence
  print ("yes!")
else:
  #quadrado não preenchido completamente - jogar novamente
  print ("next player...")
