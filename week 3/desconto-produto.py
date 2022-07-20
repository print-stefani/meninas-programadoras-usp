#Programa que le o valor de um produto, porcetagem de desconto dado e valor economizado

print ("Digite valores com casas decimais")

#variaveis
produto = float (input("Valor do produto:\t"))
desconto = float (input ("Desconto:\t"))

#calculo de desconto
economia = (produto * desconto)/100 
desconto_total = produto - economia

#saida do valor inicial, desconto e economia
print("")
print("Valor inteiro do produto: ",'{:.2f}'.format (produto))
print("Desconto dado: ",'{:.2f}'.format (desconto_total))
print("Economia de: ",'{:.2f}'.format (economia))
