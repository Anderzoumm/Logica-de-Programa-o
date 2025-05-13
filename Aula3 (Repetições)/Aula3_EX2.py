''' contador de notas'''
valor = int(input("Digite o valor em reais: "))

while True:

    cont100 = valor // 100
    valor = valor - cont100 *100
    cont50 = valor // 50
    valor = valor - cont50 *50
    cont20 = valor // 20
    valor = valor - cont20 * 20
    cont10 = valor //10
    valor = valor - cont10 *10
    cont5 = valor // 5 
    valor = valor - cont5 *5
    cont1 = valor // 1
    valor = valor - cont1 * 1
    print (f"Voce precisa de:  \n{cont100} notas de 100\n{cont50} notas de 50\n{cont20} notas de 20\n{cont10} notas de 10\n{cont5} notas de 5 \n{cont1} moedas de 1")
    break