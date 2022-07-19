#Programa usando o for para contagem de numeros

#instrução
print ("Valores aceitos são inteiros entre 0 e 1000")

#leitura do numero
valor = int (input("Digite até qual numero irá contar: "))

#estrutura de repetição em for e a função range
for i in range(valor + 1): # + 1 pois a contagem começa em 0 considerando um valor 
  print(i)
