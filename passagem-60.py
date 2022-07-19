#Programa que lê a idade do usuario e verifica se irá pagar a passagem ou não, usando a estrutura de condição

print ("Verificação da passagem do ônibus")

#leitura da idade
idade  = int (input(" Digite sua idade: "))

#estrutura de verificação das condições
if idade >= 60:
  #saida verdadeira
  print ("Gratis")
else:
  #saida caso a condição anterior for falsa
  print ("Pago")
