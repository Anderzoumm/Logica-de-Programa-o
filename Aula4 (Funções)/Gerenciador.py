'''colecionador de jogos'''
#Funções criadas para esse programa.
def valida_int (pergunta, min, max):
    '''
    Essa função faz uma validação de um numero inteiro, so sai dessa função se o numero estiver na lista que o usuario definir
    Parametros
    pergunta:deve inserir uma pergunta que sera feita ao usuario
    min: deve ser colocado um valor minimo da lista
    max: deve ser colocado o valor maximo da lista
    '''
    
    while True:
        try:
            x = int(input(pergunta))
            break
        except:
            print('Houve um erro, tente novamente')        
    while ((x < min) or (x > max)):
        try:
            x = int(input(pergunta))
        except (ValueError):
                print('Houve um erro, tente novamente')
    return x        

def existeAquivo (nome):
    """Verifica se existe um arquivo com esse nome
    Parametros
    nome : Nome do arquivo que deseja verificar.
    """
    try:
        x = open (nome, "rt") 
        x.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo (nome):
    '''
    Essa função vai criar o arquivo para ser usado no programa.
    Parametro:
    nome: nome para o arquivo (recomenda-se usar um .txt)
    '''
    try:
        x = open (nome, "wt") #a diferença ta em mudar R para W, ao invez de ler, ele vai abrir um arquivo vazio, criar um
        x.close()
    except:
        print ("Erro na criação do arquivo")
    else:
        print (f"Arquivo {nome} criado com sucesso")
    return nome   #Isso acontece devido ao fato de eu estar comendo o cu de quem ta lendo

def adicionaIten (arquivo, nomeJogo, nomeConsole):
    '''
    essa função vai adicionar um item ao arquivo criado.
    Parametros:
    Arquivo: nome do arquivo que sera armazenado os dados
    nomeJogo : nome do jogo
    nomeConsole : nome do console
    '''
    try :
        a= open (arquivo, "at")
    except:
        print ("erro ao abrir o arquivo")
    else :
        a.write (f'Jogo: {nomeJogo} Console:{nomeConsole} \n')

def lerArquivo (arquivo):
    
    try:
        x = open (arquivo, "rt")
    except:
        print("Error ao ler arquivo")
    else:
        print (x.read())
    finally:
        x.close()
arquivo = "jogos.txt"
menu = "     MENU DE FUNÇÔES     \n"+"#"*25 +"\n1-Cadastrar iten"+"\n2-Listar os cadastros"+'\n3-Sair'
#Programa principal
if existeAquivo (arquivo):
    print ("Arquivo localizado com sucesso!")

else:
    print ("Arquivo não localizado, tente outro nome ou crie um arquivo!")
    arquivo = criarArquivo("jogos.txt")        

while True:
    print (menu)
    opc = valida_int ("Digite uma opção acima: ", 1, 3)

    if  opc == 3:
        print("Fechando programa...")
        break

    elif opc == 1: #Adiciona iten
        print ("Opção de adicionar iten selecionda...")
        nomeJogo = input('Digite o nome do jogo: ')
        nomeConsole = input ("Digite o nome do Console: ")
        adicionaIten (arquivo, nomeJogo, nomeConsole)
        print ("jogo adicionado com sucesso!!")

    elif opc == 2: #Listagem
        print ("Opção de listar adicionda")    
        lerArquivo(arquivo)
