#Programa que lê um inteiro, se for maior ou igual a 60, a saida será "melhor idade" usando estrutura de condição


#leitura do dado
numero = int (input("Digite sua idade: "))

#estrutura de condição
if numero >= 60:
  #saida com a idade e com a mensagem
  print(numero, "Melhor idade!")
else:
  #caso seja uma condição falsa, a saida será "Fim"
  print("Fim")
