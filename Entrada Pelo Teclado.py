#  Entrada Pelo Teclado

nome = input("Qual seu nome? ")
print("Então seu nome é " + nome + " certo?")
#  Dando entrada de modo simples e incluindo ela na saída dentro da função print

idade = input("Prazer em conhecê-lo " + nome + ". Qual sua idade?")
#  Fazendo menção a variavel global dentro da função input

print("Então " + nome + " sua idade é " + idade + " confere? ")
#  Uso de uma ou mais variavel global na função print. 
#  Podendo ocorrer o uso de outras formas vista em chamada de variaveis e valores em print

cidades_Piaui = input("Quais as maiores cidade do Piaui? ")
#  Recenbendo uma string como resposta

print(cidades_Piaui)
#  Saída da string da forma como foi captada

cidades_Piaui = str(input("Quais as maiores cidade do Piaui? "))
#  Entrada formatada como tipo pré-definido

print(cidades_Piaui)

populacao_Piaui = int(input("Qual a população do Piaui? "))

print(populacao_Piaui)