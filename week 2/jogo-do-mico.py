#Programa do jogo do mico, le o nome do jogador e lista de cartas

#leitura dos dados
nome_jogador = input ()
cartas = [i for i in input () .split ()]



#verificação da posse da carta coringa (mico)
for string in cartas:
  
  #verificação da posse da carta coringa
  if string == 'mico':
    resposta = 'mico!'
  else:
    #caso não tenha coringa (mico)
    resposta = 'ok'
    
print(nome_jogador, resposta)
