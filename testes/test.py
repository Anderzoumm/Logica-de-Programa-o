fra = "frase bacana"
print (fra[:2])
for i in range (1, 11,):
    tipo = type(i)
    print(tipo)
while True:
    print(painel)
    escolha1 = int(input("Escolha uma opção: "))
    
    if escolha1 == 1:
        while True:
            print(itens)
            iten = int(input("Escolha um dos itens: "))
            
            if iten == 1:
                x1 = 5
                quant = int(input("Quantidade: "))
                total1 = x1 * quant
                break
                
            elif iten == 2:
                x1 = 7  # Exemplo: outro valor
                quant = int(input("Quantidade: "))
                total1 = x1 * quant
                break
                
            else:
                print("Opção de item inválida. Tente novamente.")
    
    elif escolha1 == 2:
        # Verifica se a variável total1 foi definida
        try:
            geral = total1  # + total2 + total3 + total4, se existirem
        except NameError:
            geral = 0
        print(f'O total da sua compra deu R${geral}, aceitamos xerecard')
        break

    else:
        print("Opção inválida. Tente novamente.")