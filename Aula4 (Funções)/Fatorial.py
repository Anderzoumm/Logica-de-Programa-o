"""Função que calcula fatorial"""
def fatorial (x):
    '''
    Essa função recebe um valor inteiro e retorna o fatorial desse valor.
    Na matemática, o fatorial de um número natural n, denotado por n!, é o produto de todos os naturais menores ou iguais a n.
    Parametos
    X = numero inteiro (OBRIGATRIO)    
    Função criada por: Anderzoum. 
    '''
    
    res = 1
    error = "Valor negativo, tente novamente"
    if x == 0:
        return res
    if x <=0:
        return error
    for i in range (1,x+1):
        res *= i #o I sempre vai ser a bola da vez, ele inicia em 1 e vai ate x, e o valor de res vai aumentar fatorialemnte
    return res
test = fatorial(int(input("Digite um valor: ")))
print (test)
help (fatorial)