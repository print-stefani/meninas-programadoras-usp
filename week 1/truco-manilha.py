#Programa que le a face de um dado, caso todas as faces sejam preenchidas, voce ganhou o jogo.

#leitura das faces
face_1 = input ("Face 1: ")
face_2 = input ("Face 2: ")
face_3 = input ("Face 3: ")
face_4 = input ("Face 4: ")
face_5 = input ("Face 5: ")
face_6 = input ("Face 6: ")


#verificação das faces (condições)
if face_1 == 'P' and face_2 == 'P' and face_3 == 'P' and face_4 == 'P' and face_5 == 'P' and face_6 == 'P':
  print ('Sena!')
else:
  print ('Jogue de novo...')
