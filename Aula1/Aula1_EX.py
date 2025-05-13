'''
Desenvolva um algoritomo que solicite ao usuario o preço de um produto
e um percentual de desconto a ser aplicado a ele.
'''

print (" CALCULADOR DE DESCONTO")
p1 = float(input ("Digite o valor do produto: "))
ds = float(input ("Digite o prencentual de desconto: "))
pf = float(( p1 - (p1 * (ds/100))))
resultado = f"O valor do produto com desconto é {pf}"
print (resultado)

'''
2° EXERCICIO: Escreva um programa que pergunte a quantidade de km percorridos por um carro de aluguel
assim como a quantidade de dias e calcule o valor a ser pago
dia: R$60
KM: R$0,15
'''

print (" CARRO DE ALUGUEL")
dia = float(input ("Quantos dias voce rodou?")) * 60 
km = float(input ("Quantos KM voce rodou?")) *0.15
total = km + dia
resultado = f"Voce deve {total} para a locadora"
print (resultado)


'''
EXERCICIO 3: crie uma variavel str em seguida uma 2° variavel que seja a metade da 1° e depois imprima os 2 ultimos caracters
'''

print ("BRINCANDO COM STRINGS")
st1 = input(" Digite a string: ")
st2_value =int(len(st1)//2)
st2 = (st1[:st2_value])
print (st2[-2] , st2[-1])