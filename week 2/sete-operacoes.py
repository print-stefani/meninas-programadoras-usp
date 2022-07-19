#Programa que le dois numeros inteiros e efetua sete operações matematicas: soma, subtração, multiplicação, divisão, módulo, divisão inteira e potência

#leitura dos numeros
valor_1 = int (input("Numero inteiro: "))
valor_2 = int (input("Numero inteiro: "))

#calculos ds sete operações e saida dos resultados direto 
print (valor_1 + valor_2)
print (valor_1 - valor_2)
print (valor_1 * valor_2)
print('{:.2f}'.format(valor_1 / valor_2)) #formatação dos decimais
print (valor_1 % valor_2)
print (valor_1 // valor_2)
print (valor_1 ** valor_2)
