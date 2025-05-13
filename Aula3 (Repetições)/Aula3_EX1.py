#aquecimento
'''for i in range (3,13):
    print (i)
x=0
while ( x <=9):
    print (x)
    x += 2
    '''


itens = "1-coxinha = R$5,0 \n2-Paste = R$7,0 \n3-Café = R$3,0 \n4-Suco = R$6.0"
painel = "Bem vindo a lanchonete\n" + "#" *22 + '\n1- adicionar itens\n2-encerrar compras'
valor = 0
quant = 0
total2 = 0
total3 = 0
total4 = 0
while True:
    print (painel)
    escolha1 = int(input("Escolha uma opção: "))
    
    if escolha1 == 1:
       
        print(itens)
        iten = int(input("escolha um dos itens: "))
        quant = int(input("Quantidade: "))
      
        if iten == 1:
            total1 = 5 * quant
                   
        elif iten == 2:
            total2 = 7 * quant  
            
        elif iten == 3:
            total3 = 3 * quant  
            
        elif iten == 4:
            total4 = 6 * quant  
            

        else:
            print ("Iten invalido")  
    
    elif escolha1 == 2:
        geral = total1 + total2 + total3 + total4
        print (f'O total da sua compra deu R${geral}, aceitamos xerecard')
        break