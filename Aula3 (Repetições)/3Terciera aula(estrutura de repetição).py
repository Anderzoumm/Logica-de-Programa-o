valor = 0
while (valor != 10):
    valor = valor + 1
    print (valor)
print ("saiu do while")
#comparação
for i in range (1,11,1):
    print (i)
''' 
vamos fazer agora um algoritimo que calcule a media dos numeros pares de 0 a 100 usando for
'''
soma = 0 #precisamos definir as variaveis para fazer a media
qnt= 0
for i in range (1,101): #aqui ele vai fazer a lista
    if (i % 2 == 0): #e aqui a verificação se um numero é par
        soma += i #vai somar os pares, esse "I" é um numero par, aqui na soma ele vai pegar cada par e somar todos
        qnt += 1 # ja aqui ele vai verificar quantos numeros pares foram somados
media = soma / qnt # obviamente aqui ele calcula a media
print (f"A media dos pares de 1 a 100 é de {media}")

'''
Vamos fazer as tabuadas
'''
#usando apenas for
   #variavel
for tabuada in range (1,11): #aqui ele vai fazer as tabudadas
    print (f"Tabuada do {tabuada}")
    for i in range (1,11): #ja aqui ele vai fazer os denominador
        print (tabuada * i) 
#Usando apenas While
tabuada = 1
while (tabuada <= 10):
    print (f"Tabuada do {tabuada}")
    denominador = 1
    while (denominador <= 10):
        print ( tabuada * denominador)
        denominador += 1
    tabuada +=1
print ('saiu do while')
#Usando ambos

tabuada = 1 
while ( tabuada <= 10):
    print (f" Tabuada do {tabuada}")
    for i in range (1,11):
        print (tabuada * i)
    tabuada += 1
print ("saiu do while")     