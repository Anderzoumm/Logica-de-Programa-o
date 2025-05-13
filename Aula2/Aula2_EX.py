
#se a idade é maior que 60, escreva "voce tem direito aos benefiios
'''
ida = int(input("Digite sua idade"))
if ida >=60 :
    print ("Voce tem direito aos benefios")
else: 
    print ("Voce nao tem direito aos benefios")
'''

#se dano é maipr que 10 e escudo é igual a 0, vc morre

'''
dano = int(input("QUANTO DE DANO? "))
esc = int(input( "ESCUDO ATUAL: "))
if dano >= 10 and esc <= 0:
    print ("VOCE ESTA MORTO!!")
else:
    print (" VOCE VENCEU!!!")
'''


#se pelo menos uma das variaveis booleanas norte sul leste oeste resultem em True "VOCE ESCCAPOU"

'''
norte = True
sul = True
leste = False
oeste = True
if (norte == True or sul== True or leste==True or oeste==True) :
    print ("VOCE ESCAPOU")
'''

#Detecte ano bisexto
'''
ano = int(input("DIGITE O ANO"))
if (ano % 4 == 0):
    print (" È um ano bisexto")
else :
    print ("NAO É UM ANO BISEXTP")
'''

#IDENTIFICADOR DE TRIANGULO
'''
print ("bem vindo ao identificador de triangulo")
print ("#" * 39)
print("   *\n  ***\n *****\n*******")
x1 = float (input("DIGITE O VALOR DO PRIMEIRO LADO: "))
x2 = float (input("DIGITE O VALOR DO SEGUNDO LADO: "))
x3 = float (input("DIGITE O VALOR DO TERCEIRO LADO: "))
if ( x1 <= 0 or x2 <= 0 or x3 <= 0 ) or (x1 + x2 < x3 or x1 + x3 < x2 or x2 + x3 < x1):
    print ("TRIANGULO INVALIDO")    
    
elif x1 == x2 != x3 or x1 == x3 != x2 or x2 == x3 != x1:
    print (" ESTE È UM TRIANGULO ISOCELES")
elif x1 == x3 == x3:
    print ("ESTE É UM TRIANGULO ECLATERO")
elif x1 != x2 != x3:
    print ("ESTE É UM TRIANGULO ESCALETO")
'''

#CAUCULADORA BASICA USADNDO OQ APREDEMOS 
print ("CAUCULADORA")
x1 = float(input("Digite valor de x1: "))
x2 = float(input("Digite valor de x2: "))
oprs = "1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisão"
print (oprs)
opr = int(input("Digite uma operação: "))
if opr == 1 :
    r = x1 + x2
    res = f"Resultado é {r}"
elif opr == 2 :
    r = x1 - x2
    res = f"Resultado é {r}"
elif opr == 3 :
    r = x1 * x2
    res = f"Resultado é {r}"
elif opr == 4 :
    r = x1 / x2
    res = f"Resultado é {r}"
print (res)