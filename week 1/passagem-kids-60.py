#Programa que le a idade dos passageiros e verifica caso seja menor que 6 (no colo) e pessoas com mais de 60 anos não paga a passagem

#leitura da idade
idade = int (input("Digite sua idade: "))

#verificação das condições
if idade >= 60:
  #caso a condição seja verdadeira, gratis
  print('Gratis')
elif idade <= 6:
  #conjunto de comandos caso a primeira condição seja falsa, gratis no colo 
  print('Gratis no colo')
else:
  #caso as condições anteriores seja falso - pagar
  print("Pago")
