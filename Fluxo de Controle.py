# Fluxo de Controle

# Fluxo de condição IF

condicao = False

if condicao == True:
	print("A condição é verdadeira.")
else:
	print("A condição é falsa.")
'''NOTA: Fazer ' if condicao == True: ' equivale dizer ' if condicao:' sendo esta ultima a mais utilizada.
Pois em Python o fluxo de condição if trata a variavel, string, por natureza como verdadeira, a variavel ou
a condição.'''

valor = input("Digite um valor: ")

if valor:
	print("condição verdadeira")
else:
	print("condição falsa")

''' O uso do is pode ser aplicado na primeira condição, veja:'''

if condicao is True:
	print("A condição é verdadeira.")
else:
	print("A condição é falsa.")

''' Python aconselha que ficaria mais elegante assim. A resposta seria a mesma. Mas se tratando do uso do is e do 
operador de igualdade, vale saber o seguinte: IS deve ser usado apenas para comparação da identidade do objeto,
enquanto  ==  é usado para comparar valores , ou qualquer outra coisa, de objeto. IS PARA IDENTIDADE == PARA 
IGUALDADE.'''

''' Condicionais em cadeia:'''

condicao1 = False
condicao2 = False

if condicao1:
	print("condicao 1 verdadeira.")
elif condicao2:
	print("condicao 2 verdadeira.")
else:
	print("Condicao 1 e condicao 2 sao falsas")

'''Caso String vazia'''

salario = int(input("Insira o salario: "))
imposto = input("Insira o imposto: ")  # retorna uma string vazia se usada a tecla enter, sem entrada.

if imposto == '':  # sendo a string vazia o valor sera igual a '' o primeiro bloco sera executado e o else, não.
	imposto = 12.5  # imposto é igual a 0 (nada?)? Sim, verdadeiro, então execute esta instrução.
else:
	imposto = float(imposto)
print("O valor do salario é {0} e o valor do imposto é {1}".format(salario, imposto))
''' Semanticamente uma string vazia em um bloco if equivale a false'''

salario = int(input("Insira o salario: "))
imposto = input("Insira o imposto: ")  
# O uso do not no lugar do operador de igualdade.
if not imposto:  # lembrando que o operador not retorna verdadeiro se o operador for falso. É a negação
	imposto = 12.5  # Lembre do ! em C. A expressão 'not imposto' é o mesmo que 'not '' '
else:
	imposto = float(imposto)
print("O valor do salario é {0} e o valor do imposto é {1}".format(salario, imposto))


# Fluxo de repetição FOR

''' Python itera sobre os itens de qualquer sequência (seja lista ou string), na ordem que aparecem na sequência.
'''

for i in [1, 2, 3, 4, 5, 6]:    
    print(i)
''' Para imprimir todos os números em uma só linha usamos end'''
for i in [1, 2, 3, 4, 5, 6]:
    print(i, end=' ')

for i in ["amor", "e", "guerra"]:    
    print(i)

palavras = ["fazenda", "cavalo", "estrada"]

for palavra in palavras:
	print(palavra)
for palavra in palavras:
	print(palavra, len(palavra))

''' A função range() itera sobre sequencias númericas, gera progressão aritméticas:'''
for numero in range(10):  # não inclui o 10 pelo indice começar do zero sempre, mas ha maneiras de incluirmos
	print(numero, end=' ')

for numero in range(5, 10):  # limita, selecionando um intervalo a ser trabalhado
    print(numero)  

for palavra in range(len(palavras)):  # para cada palavra em range no intervalo de tamanho da lista palavras (5)
	print(palavra, palavras[palavra])  # Imprima o numero pedido em range, imprima a palavra correspondente ao
# indice dentro da lista e apresentado por i
# Na maioria dos casos é mais conveniente usar a função enumerate().

'''  A instrução FOR exige inicialmente a definição de uma variável e, em seguida, a lista que será iterada.
for <variável>in<objeto iterável>:
A varivael a ser declarada na primeira parte da estrutura, receberá, a cada cilco, um elemento contido na lista 
que está sendo iterada. Ao término, todos os elementos terão sido percorridos e, a cada ciclo, o elemento segui-
te contido no objeto iterável terá sido passado pela variável definida inicialmente.
Lê-se o comando na seguinte forma: para cada elemento contido na lista [1, 2, 3 ,4] execute o código de bloco a
seguir e a cada execução atribua a variável item um item da lista.  '''

# Tecnicas de iteração

''' Iterando sobre dicionarios a chave e o valor correspondente pode ser obtidos simultaneamente usando o método
items()  '''

estados_capitais = {'Piaui': 'Teresina', 'Bahia': 'Salvador', 'Ceara': 'Fortaleza'}

for estado, capital in estados_capitais.items():
	print(estado, capital)

# Função enumerate
for numero, indice in enumerate(range(1, 10)):
	print(numero, indice)  # Conte como menos um, excluindo o numero final indicado sempre.
''' o primeiro numero indica ponto de partida, o segundo o alcance do intervalo e o terceiro o intervalo de pa'''

# Função reversed - Para percorrer uma função em ordem inversa

for numero in reversed(range(5, 10)):  
    print(numero)  

# Função sorted - Percorre uma sequência de maneira ordenada, retorna uma lista ordenada com os itens, mantendo
# a sequencia original inalterada

palavras2 = ["zona", "fazenda", "cavalo", "estrada", "abacate", "campo", "azeitona", "cidade", "zona", "cavalo"]

for palavra in sorted(set(palavras2)):
	print(palavra)
# Se retirar set() as palavras irão se repetir, mas ainda assim ficarão ordenadas. Ou seja, ela evita repetições.

# Função zip - Para percorrer duas funções ao mesmo tempo, as entradas podem ser pareadas com esta função.

raça = ["Malore", "Vacanti", "Donattus"]
especie = ["Calango", "cavalo", "bezerro"]

for i, n in zip(raça, especie):
	print("A raça {0} é da especie {1}".format(i, n))

# Criando uma lista a partir de uma outra lista

import math # importa os a biblioteca de matematica

dados = [52.8, float('NaN'), 12.1, 4, 6.3, float('NaN')]

dados_filtrados = []

for valor in dados:
	if not math.isnan(valor):
	    dados_filtrados.append(valor)


print(dados_filtrados)

# Atenção ao uso de tab ou espaços

for num_primario in range(1, 11):
	print("TABUADA DO {0}".format(num_primario))
	for num_secundario in range(1, 11):
		print(num_primario, "X", num_secundario, "=", num_primario * num_secundario)
	continue  # É aconselhavel o uso de tab ao invés de espaço.Já ocorreu erro de identação com o uso de espaço.
	print(end=' ')


impostos = ['MEI', 'Simples']

for imposto in impostos:
	if imposto.startswith("S"):  # a função start with retorna true se a string começar com o valor especico
		continue  # Se a função print estivesse aqui, ela retornaria a condição de if.
	print(imposto)  # ela retorna o item excluso na condição de if.

# O Fluxo de condição WHILE

i = 1

while i < 5:
	print(i)
	i = i + 1

''' Um exemplo útil do uso do enquanto é o fatorial'''
n = 6
fatorial = 1

while n > 1:  # Enquanto n for maior que 1, faça:
	fatorial *= n  # o valor da variavel fatorial é multiplicado por n
	n -= 1  # n finaliza atribuindo -1 ao seu valor
print(fatorial)


salario = int(input("Salario?"))
imposto = 27

while imposto > 0:
	imposto = input("Imposto ou (0) pra sair: ")
	if not imposto:
		imposto = 27
	else:
		imposto = float(imposto)
	print("Valor real: {0}".format(salario * (imposto * 0.01)))  # Condicional até usuario desejar sair.


# Comando BREAK, CONTIUE, e clausula ELSE.

# BREAK
salario = int(input("Salario?"))
imposto = 27

while imposto > 0:
	imposto = input("Imposto ou (0) pra sair: ")
	if not imposto:
		imposto = 27
	elif imposto == 's':  # com um caracter pra sair ao inves de zero
		break  # O comando break sai imediatamente do laço de repetição mais interno
	else:
		imposto = float(imposto)
	print("Valor real: {0}".format(salario * (imposto * 0.01)))

# ELSE

''' Laços também podem ter a clausula else, que é executada sempre que o laço se encerra de forma natural 
ou quando a condição se torna falsa.'''
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'igual', x, '*', n // x)
	else:  # O laço acaba sem encontrar o fator
		print(n, "é um numero primo")
''' Quando usado em um laço a clausula else tem mais em comum com a clausula else de um comando TRY, do que 
com um comando if'''

# CONTINUE

impostos = ['MEI', 'Simples']

for imposto in impostos:
	if imposto.startswith("S"):  # a função start with retorna true se a string começar com o valor especico
		continue  # Se a função print estivesse aqui, ela retornaria a condição de if.
	print(imposto)  # ela retorna o item excluso na condição de if.
#  essa função continua com a procima iteração do laço.

# PASS

# Este comando não faz nada, pode ser usado quando a sintaxe exige um comando mas a semantica do programa não
#  quer nenhuma ação

while True:
	pass

if True:
	pass

impostos = ['MEI', 'Simples']

for i in impostos:
	pass

