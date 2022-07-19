#Programa que conta os pares ate o valor informado 

#Instrução
print ("Valores aceitos são de 1 a 1000")

#coleta do numero
valor = int (input("Digite o numero: "))

#estrutura de repetição e função range 
for valor in range (valor):
  #verificação da condição para saida dos pares
  if valor % 2 == 0:
    print (valor)
