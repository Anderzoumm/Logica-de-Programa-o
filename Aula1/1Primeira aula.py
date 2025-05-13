print ("Hello world!")       #Classico ne, nao vamos perder a tradição
#operações do python
#As basicas que todos conhecemos.
1+2
1-2
1*2
1/2
1//2 #Divisao co a parte intera
1%2 # Modulo/ resto da divisão
1**2 #exponesial potencia
#Concatenação de Strings
a1 = "ola "
print (a1 + "mundo!")
# Repetição de strings
print ("Painel de controle \n" + "#" * 18)
#PODEMOS INSERIR VARIAVEIS DENTRO DE UMA STRIG SEM SEPARAR 
nota = 8.50 
diciplina = "portugues"
resultado = "Voce tirou {} na diciplina de {}".format(nota, diciplina)
print (resultado)
# VEJA, .FORMAT SO FUNCIONA NAS VARIAVEIS, NAO FUCNIONA DIRETO NO PRINT
# F-STRINGS É UMA MANEIRA MAIS FACIL, PRECISAMOS PRIMEIRO COLOCAR UM F ANRES DA STRING
resultado = f"voce tirou {nota} na diciplina de {diciplina}"
print (resultado)

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