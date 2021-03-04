#  Formatação de entrada e saída
#  saída (print)

a = 'z'
palavra = 'girafa'
n = 2
c = 2.896
d = 0.58

print(n, n * d)
#  Palavra chave de parâmetro "sep"
print('Apenas valores sem o sep:')
print(2, 3, 4)
print('Apenas valores com o sep:')
print(2, 3, 4, sep=', ')
print('Valores e variaveis com o sep:')
print(8, n, n * d, sep=', ')
print(8, n, n * d, end=' ')
print('Uma frase mista:')
print('A', palavra, 'possuia', n, 'metros de altura, diminuiu', n * d)

#  Usando concatenação de string
print(str(n) + " " + str(d) + " " + str(n * d))

#  A maniera antiga ou inexistente 
print("Arte: %5d, Preços por unidade: %8.2f" % (352, 39.063))
#  É composto pelo formato string + operador de modulo string + tupla com valores.
#  Ver documentos sobre marcadores de posição e seus tipos.
#  Ver códigos de formatação e seus significados.

# O jeito Pythonico: O metodo String "format"

print("Arte: {0:5d}, preço pela unidade: {1:8.2f}".format(352, 39.063))
#  Argumentos de acordo com posições (o primeiro é sempre zero, o codigo acima tem dois argumentos)
#  Melhor metodo para se trabalhar, pois a ordem dos argumentos não importam, basta altera-los.
print("Arte: {a:5d}, preço pela unidade: {b:8.2f}".format(a=352, b=39.063))
#  Argumento de acordo com palavras chaves (Seomente uso de palavras para declarar)
print("Arte: {a:d}, preço pela unidade: {b:.2f}".format(a=352, b=39.063))
#  Argumentos sem valor de espaçamento
print("Arte: {a}, preço pela unidade: {b}".format(a=n, b=c))
#  Argumento fazendo apenas chamada com o parametro
print("Arte: {a:d}, preço pela unidade: {b:.2f}".format(a=n, b=c))
#  Argumento fazendo chamada com o parametro e convertendo casas decimais

#  Usando dicionário em "format"

#  Há dois meios para acessar esses valores nesse formato: Posição ou Index.
print("A capital do {0:s} é {1:s}".format("Piaui", "Teresina"))
#  Usando palavras-chave como parâmetros:
print("A capital do {estado} é {capital}".format(estado="Piaui", capital="Teresina"))
#  Para declarar variaveis como palavras basta utilizar o método acima.
#  Usando dicionario:
dados = dict(estado="Piaui", capital="Teresina")
#  Verificação do dicionario:
print(dados) 
#  Chamando na saída:
print("A capital do {estado} é {capital}".format(**dados))
#  O uso dos dois "*" na frente do dicionario chama o dicionario automaticamente em sua forma.

#  OBSERVAÇÕES: Faltam o estudo sobre o uso do laço for no dicionario, o uso do nome da variavel local em função