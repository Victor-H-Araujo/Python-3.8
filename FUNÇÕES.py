# FUNÇÕES 

# NOTA : O TERMO OBJETO AQUI SE REFERE A VÁRIAVEL, O MESMO QUE É TRATADO EM R.

def soma(a, b):  # A palavra def inicia uma função, seguida do nome da função da lista e de parametros
    ''' função de soma '''  # Uma literal strin coma descrição da função
    valor = a + b  # a execução da função cria uma nova tabela de simbolos para as variaveis locais da função
    print("O valor de {0} + {1} = {2}".format(a, b, valor))  # Variaveis são armazenadas localmente
    return print()
#  Embora possam ser referenciadas, variaveis globais e de funções externas não podem ter atribuições exceto 
#  com uso do comando global oara varivaeis globais e nonlocal, para variaveis de funções externas.


soma(10, 2) 
''' Argumentos são passados por valor (onde o valor é sempre uma referencia para objeto, 
não valor do objeto)'''

var = soma  # Otras variaveis podem chamar outras funções, renomenaod elas, como um ponteiro
var(2, 3)


def soma(a, b):
    ''' função de soma '''  # Uma literal strin coma descrição da função
    valor = a + b  
    print("O valor de {0} + {1} = {2}".format(a, b, valor))  


soma  # Soma poderia sser um procedimento, nao uma função, neste momento em que ela nao devolve valor.
# Mesmo funções que nao usam return devolvem um valor, ainda que nao seja interessante ou usado. Esse valor é None

print(soma(0, 0))
# none

# Função que devolve uma lista de números


def temperatura(n):
    '''fibonati mas nomeado como se fosse um medido de temperatura'''
    resultado = []
    a, b = 0, 1
    while a < n:
    	resultado.append(a)
    	a, b = b, a + b
    return resultado  # Ou simplesmente a função print poderia  ser incluida aqui e o resultado poderia sair direto  
# Return finaliza a função e retorna um valor da função. Sem qualquer expressão com argumento retorna none.


temp = temperatura(100)

print(temp)

''' A instrução result.append(a)  chama o metodo do objeto lista resultado. Método é uma função que 'pertence'
 a um objeto, e é chamada de obg.nomemetodo, onde obj é um objeto qualquer (pode ser uma expressao), e nomemetodo
 é o nome de um método que foi definido pelo tipo do objeto. Tipos diferentes definem métodos diferentes.
 O metodo append(), mostrado no exemplo é definido para objetos do tipo lista.'''

''' Existem 3 formas de definir funções com um número variavel de argumentos, são eles:
		- Argumentos com valor padrão
		- Argumentos nomeados
		- Parâmetros Especiais
		     - Argumentos posicional-ou-nomeados
		     - Argumentos somente nomeados
		     - Exemplos de funções
    Outras formas:
		- Listas de argumentos arbitrários
		- Desempacotamento de lista de argumentos
		- Expressões lambda
		- String de documentação
		- Anotações de função  '''

# Argumentos com valor padrão


def pergunta_ok(prompt, tentativas=4, aviso='Por favor tente de novo'):  # Há 3 argumentos sendo dois padrões
    while True: 
    	ok = input(prompt)
    	if ok in ('s', 'si', 'sim'):
    	    return True
    	if ok in ('n', 'na', 'nao'):
    	    return False
    	tentativas -= 1
    	if tentativas < 0:
    	    raise ValueError('Resposta invalida pelo usuario')  # Encerrando as tentativas, apresenta-se o erro
    	print(aviso)


pergunta_ok('Voce realmente quer sair?')
''' A intuição do codigo acima é mostrar que somente o primeiro argumento é obrigatorio, visto que nao tem valor
definido como padrão, os demais que tem valor como padrão nao sao obrigatorios serem passados pelo usuario, ja que
se nao for passado, usará os valores padrões.

Este exemplo introduz o operador in, que verifica se uma sequência contém ou não um determinado valor.

Os valores padrões são avaliados no momento da definição da função, e no escopo em que a função foi definida, 
portando: '''

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


''' NOTA:  VALORES PADRÕES SÃO AVALIADOS APENAS UMA VEZ. ISSO FAZ DIFERENÇA QUANDO UM VALOR É UM OBJETO MUTÁVEL,
COMO UMA LISTA, DICIONÁRIO, OU INSTÂNCIAS DE CLASSES. POR EXEMPLO, A FUNÇÃO A SEGUIR ACUMULA OS ARGUMENTOS PASSADOS
NAS CHAMADAS SUBSEQUENTES:'''


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# O o argumento passado vai icrementando na lista


def f(a, L=None):  # Agora o valor padrão na será compartilhado entre chamadas subsequentes
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# Argumentos  nomeados

# funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

def papagaio(voltagem, estado='duro', ação='voou', type='Azul Ciano'):
    print("O papagaio acabou", ação, end=' ')
    print("Se voce colocar", voltagem, "volts atravez disso")
    print("Gosto da plumagem desse tipo:", type)
    print("Ele esta", estado, "!")
# Aceita um argumento obrigatorio e três arfumentos opcionais


papagaio(1000)
papagaio(voltagem=1000, ação='morto')
# Em uma chamada de função  argumentos nomeados devem vir depois dos argumentos posicionais. Todos os argumentos
# nomeados passados devem corresponder com argumentos aceitos pela função. 
# NENHUM ARGUMENTOS PODE RECEBER MAIS DE UM VALOR.


''' Quando o último parametro formal no formato **nome esta presente, ele recebe um dicionário contendo todos os 
argumentos  nomeados, exceto aqueles que correspondem a um parâmetro formal. Isto pode ser combinado com um parâme-
tro  formal no formato de *nome que recebe uma tupla contendo os argumentos posicionais, além da lista de parâmetros
formais.(*nome deve ocorrer antes de **nome)'''


def loja_queijo(tipo, *argumentos, **Keywords):
    print("-- Voce tem algum", tipo, "?")
    print("-- Desculpe temos algum pedidos de", tipo)
    for arg in argumentos:
        print(arg)
    print("-" * 40)
    for kw in Keywords:
        print(kw, ":", Keywords[kw])


loja_queijo("Kingburger", "É muito ruim senhor",
            "É muito mas muito ruim senhor",
            cerveja="Brahma",
            cliente="Victor H Araujo",


# A ordem com que os argumentos nomeados são exibidos é garantida para corresponder à ordem em que foram fornecidos
# na chamada da função


# FALTA FINALIZAR O ASSUNTO DE FUNÇÕES
