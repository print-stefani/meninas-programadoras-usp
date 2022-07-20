#Programa que faz a destinação de imposto de renda, verificando se é pessoa fisica ou juridica

#Introdução
print ("Digite F - pessoa fisica\nJ - pessoa juridica")

#variaveis
pessoa = input ()
imposto = float (input("igite o imposto:\t"))

#se for fisica o imposto é de 6% 
if pessoa == "F":
  valor_F = (imposto * 6) /100
  print ('{:.2f}'.format (valor_F))
  
#se for pessoa juridica o imposto é de 1% 
elif pessoa == "J":
  valor_J = (imposto * 1) /100
  print ('{:.2f}'.format (valor_J))
  
else:
  print ("Opções invalidas...")
