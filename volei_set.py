time_1 = int (input("Digite os pontos do time 1: "))
time_2 = int (input("Digite os pontos do time 2: "))

diferenca = time_1 - time_2
diferenca_2 = time_2 - time_1

if (time_1 == 25 or time_2 == 25) and (diferenca > 2 or diferenca_2 > 2):
  print('Sim, o set acabou')
else:
  print('Não, o set continua')
