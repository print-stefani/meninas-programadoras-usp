#Programa que lê dois inteiros e calcula a soma, diferença do primeiro para o segundo, diferença do segundo para o primeiro e a multiplicação entre eles

#leitura das informações do usuario
num_1 = int (input("Digite o primeiro numero inteiro: "))
num_2 = int (input("Digite o segundo numero inteiro: "))

#calculos pedidos de soma, diferença dos inteiros e a multiplicação
soma =  num_1 + num_2
diferenca =  num_1 - num_2
diferenca_2 = num_2 - num_1
multiplica = num_1 * num_2

#valores de saida conforme o esperado do programa
print (soma)
print (diferenca)
print (diferenca_2)
print (multiplica)
