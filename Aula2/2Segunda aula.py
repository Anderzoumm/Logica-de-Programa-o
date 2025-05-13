#ler dois valores e comparar ambos
'''
x1 = int(input("Digite o primeiro valor: "))
x2 = int(input("Digite o segundo valor: "))
if x1 > x2 :
    print (" X1 é maior que X2")
else :
    print (" X2 é maior que X1")
'''
'''
#Par ou impar
x3 = int(input("DIGITE UM VALOR INTEIRO: "))
if x3 % 2 == 0 :
    print ("Par")
else:
    print  (" impar")
'''
#APROVADO OU NAO
'''
print ("ESCOLA DE ENSINO MEDIO")
x1 = float(input("Digite a primeira nota: "))
x2 = float(input("Digite a segunda nota: "))
x3 = float(input("Digite a terceira nota: "))
res = x1 >= 7 and x2 >= 7 and x3 >= 7
if res == True:
    print (" Aprovado")
else:
    print (" Reprovado")
'''
#Criar um algoritmo de lista de compras
print ("LISTA DE COMPRAS")
print ("################")
opcs = "1-Laranjas(R$2,30) \n2-Maças(R$3,60) \n3-Banana(R$1,85)"
print(opcs)
opc = float(input ("Digite o que deseja adicionar a sua lista: "))
quant = float(input("Quantas? "))
if opc == 1:
    valor = 2.30 * quant
elif opc == 2:
    valor = 3.60 * quant
elif opc == 3 :
    valor = 1.85 * quant
else :
    print("Produto invalido")
result = f"Sua compra deu R${valor}"
print (result)