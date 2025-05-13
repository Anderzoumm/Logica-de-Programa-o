#Funções sao comando na programação, podemos usar os que ja temos na linguagem ou criarmos nossos proprios.
#Funções recebem parametros () que podem ser obrigatorios ou nao
""" Caixinha """
def box (name):
    x = len(name)
    barra = f"+"+"-"*x +"+"
    print (barra)
    print (f"+{name}+")
    print (barra)

box ("anderzoum")  

""" Recebe nome, numero minimo e maximo de letras, e faz uma verificação"""

def confirm (nome, min, max):
    ver = len(nome)

    if ver >= min and ver <=max:
  
        resp=True
  
    else:
        resp = False
  
    return resp


teste = confirm("cacildas", 2, 5)
print (teste)