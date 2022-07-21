#Programa que lê um conjunto de valores e verifica quantas vezes cada valor aparece

#Instrução
print ("Digite uma lista de valores inteiros entre -100 e 100")

#leitura dos dados
lista = [int (i) for i in input().split()]


menor = min(lista)
maior = max(lista)
lista.sort ()

soma = 0
anterior = 101

for i in lista:
  soma += i
  lista_total = sum(lista)
  if i != anterior:
    print(i, lista.count(i))
    anterior = i
print(lista_total)
