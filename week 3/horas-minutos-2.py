#Programa que le os minutos (numeros) e converte em horas, com formatação usando '{:02d}'

#leitura de quantos valores serão convertidos
numero = int (input ("Minutos: "))

#estrutura de repetição para converção e contagem
for contador in range (numero):
  
  #os minutos a serem convertidos
  total = int (input())
  
  #calculo de conversão
  hora = total // 60
  minuto = total % 60
  
  #formatação 0 - indica o espaço a ser preenchido com zeros e d - indica que é inteiro
  print ("{:02d}h{:02d}min".format(hora,minuto))
