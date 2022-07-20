#Programa que le um numero em minutos e transforma em horas e minutos

#variavel
numero = int (input ("Digite os minutos: "))

#calculo de horas e minutos
hora = numero // 60
minuto = numero % 60

#saida do programa 
print (numero, "minutos =", hora, "horas e", minuto, "minutos")
