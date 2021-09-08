# TESTE
# site para verificar = https://www.profelectro.info/mapa-de-karnaugh-onlie-para-simplificacao-de-funcoes-booleanas-a-partir-da-tabela-da-verdade/
# y = a'b'c' + ab'c + abc' + a'b'c + a'bc + ab'c'
# Em binário = 000, 101, 110, 001, 011, 100
# Em ordem = 000, 001, 011, 100, 101, 110
# Decimal = 0, 1, 3, 4, 5, 6
# indices separados = [['001', '100'], ['011', '101', '110']]

from Quine_McCluskey import *

expressao = input()

compara_indices(expressao)