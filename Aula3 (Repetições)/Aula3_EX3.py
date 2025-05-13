""" Contador de ingressos"""
print ("Bilheteria")
total = 0
dinheiro = 0
idades = 0
while True:
    ida = int(input("Digite sua idade: "))
    idades += ida
    if ida ==0:
        break
    elif ida <=3 :
        continue
    elif ida <= 12:
        dinheiro += 15
    elif ida >= 12: 
        dinheiro += 30
    total +=1
    
    opc= (input("Deseja continuar?(s/n) "))
    if opc == "n":
        break
    else:
        continue
media = idades / ida
print (f'O total de pessoas que compraram ingressos foram de {total}, o dinheiro arrecado foi de {dinheiro} e a media de idade é de {media}')