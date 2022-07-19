#Programa que le dados indeterminados de linhas, e de saida imprime o numero de linhas lidas, menos os vazios.
#termina quando for digitado CDA 1942 - usando a estrutura de repetição while

#instrução
linha = input ("Digite o titulo e o poema de Carlos Drummond:\n")

#define variavel inicial
texto = 0

#estrutura de repetição
while linha != 'CDA 1942':
  
  #verificação da condição
  if linha != '':
    texto = texto + 1
  linha = input ()
print (texto)
