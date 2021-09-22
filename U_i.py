# TESTE
# site para verificar = https://atozmath.com/KMap.aspx?q=quine&q1=4%2C8%2C10%2C11%2C12%2C15%60%60a%2Cb%2Cc%2Cd%601&do=1#tblSolution
# y = a'b'c' + ab'c + abc' + a'b'c + a'bc + ab'c'
# Em binário = 000, 101, 110, 001, 011, 100
# Em ordem = 000, 001, 011, 100, 101, 110
# Decimal = 0, 1, 3, 4, 5, 6
# indices separados = [['001', '100'], ['011', '101', '110']]

#a'b'c + a'bc' + ab'c' + a'bc + abc' + abc
#x'y'z + xy'z' + x'yz' + x'yz + xy'z + xyz
#abcd + abcd' + abc'd'
#a'b'c'd' + a'b'cd + a'bcd' + a'bc'd + abc'd'
#0000, 0011, 0110, 0101, 1100
#y = a'bc'd' + abc'd' + a'b'c'd + a'bc'd + a'bcd' + abcd'

from Quine_McCluskey import *

print("""
Digite:
    0 -> Para Calcular passando a Expressão com Variaveis
    1 -> Para Calcular passando a Expressão com Binários
    2 -> Para Calcular passando a Expressão com Minetermos(Decimais)
""")

opcao = int(input())
expressao_ou_binario_ou_decimais = input()

binarios = verifica_opcao(opcao, expressao_ou_binario_ou_decimais)

numeros_simplificados = compara_n_vezes(binarios)[1]
print(numeros_simplificados)
print("Numeros Simplificados: ", end = "")
for num in numeros_simplificados:
    print(num, end=" ")
print()

numeros_simplificados_crivo = calcula_crivo(binarios)
print("CRIVO: ", end = "")
for num in numeros_simplificados_crivo:
    print(num, end=" ")
print()

print("Expressão Simplificada: {}".format(transforma_em_variaveis(expressao_ou_binario_ou_decimais, binarios)))
