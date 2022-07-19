#Programa que le dados do mesmo tipo na mesma linha usando o split(), retornando uma lista

#informar possiveis listas nesse programa
print(" f - valores inteiros \n s - sequencia de caracteres \n n - valores decimais\n") 

#leitura da entrada
entrada = input ("Digite a opção escolhida: ")

#verificação da entrada para formatação do split
if entrada == 'f':
  nota_final = [int (i) for i in input().split()]
  print (nota_final)
elif entrada == 'n':
  nota = [float(i) for i in input().split()]
  print (nota)
elif entrada == 's':
  sobrenome = [str(i) for i in input().split()]
  print (sobrenome)
