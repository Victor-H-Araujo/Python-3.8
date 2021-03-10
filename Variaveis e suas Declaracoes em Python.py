#  Variáveis e suas Declarações em Python

#  Não apenas o valor da variavel muda durante o programa em excução, mas o tipo também.

i = 36

print(" o valor da variavel é: {0}".format(i))

i = i + 1

print("O valor da variavel somado a 1 é: {0}".format(i))

i = 36 + 0.12

print("O Valor da variavel  somado a 0.12 é: {0}".format(i))

i = "cadeira"

print("A variavel agora é ums string: {0}".format(i))

#  Variaveis podem ser declaradas com letras maiusculas e minusculas do alfabeto, com o anderline _, exceto como 
#  primeiro caracter, digitos de 0 a 9, além de caracteres. É casesensitive.

#  Numeros complexos podem ser declarados em python

equação_1 = 3 + 4j 
equação_2 = 2 - 3j

x = equação_1 + equação_2

print(x)

#  String, unicodigo e Python

s1 = 'Voce deveria ler isso!'
s2 = "Voce deveria ler isso!"

#  Pode ser usada com uma ou duas aspas.

print(s1, s2, sep=" ")

#  String pode ser sobrescrita ou indexada. Como em outras linguagens o primeiro caracter da string tem index 0.

print(s1[0])
#  Imprime o index 0, a primeira letra ou algarismo no caso.

print(len(s1))
#  Para medir o tamanho da string.

#  Concatenação: Aonde string podem ser concatenadas com o operador  +

s3 = s1 + s2

print(s3)

s4 = "Ola " + "Mundo"

print(s4)

#  ------------

#  Imprimindo uma string.
s = "Olá, mundo!"
print(s)

#  Tipo de uma string.
type(s)

#  Tamanho de uma string.
len(s)

#  Concatenação
print("Meu Brasil " + "brasileiro")

#  Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo", "meu abacate")

print(s1)

#  A string s começa com "Olá"?
print(s.startswith("Olá"))

#  A string s termina com "mundo"?
print(s.endswith("mundo"))

#  Quantas ocorrências da palavra "abacate" a string s1 possui?
print(s1.count("abacate"))

#  Como "capitalizar" (transformar a primeira letra da primeira palavra em maiúscula).
s = "ordem e progresso"
print(s.capitalize())

#  Como verificar se uma string só possui números.
'12345'.isdigit()
'12345abc'.isdigit()

#  Como verificar se uma string é alfanumérica (só possui letras e números).
'12345abc'.isalnum()


#  Slicing

s = "Olá, mundo!"
print(s[0])
print(s[2])
print(s[6])

s = "Olá, mundo!"
print(s[:3])

print(s[5:])

# Retorna toda a string
print(s[:])

