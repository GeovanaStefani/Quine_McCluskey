import unittest

# TESTE
# site para verificar = https://atozmath.com/KMap.aspx?q=quine&q1=4%2C8%2C10%2C11%2C12%2C15%60%60a%2Cb%2Cc%2Cd%601&do=1#tblSolution
# y = a'b'c' + ab'c + abc' + a'b'c + a'bc + ab'c'
# Em binário = 000,101,110,001,011,100
# Em ordem = 000, 001, 011, 100, 101, 110
# Decimal = 0,1,3,4,5,6
# indices separados = [['000'], ['001', '100'], ['011', '101', '110']]

#a'b'c + a'bc' + ab'c' + a'bc + abc' + abc
#["001", ""010, "011", "100",  "110", "111"]
#x'y'z + xy'z' + x'yz' + x'yz + xy'z + xyz
#abcd + abcd' + abc'd'
#a'b'c'd' + a'b'cd + a'bcd' + a'bc'd + abc'd'
#0000, 0011, 0110, 0101, 1100
#y = a'bc'd' + abc'd' + a'b'c'd + a'bc'd + a'bcd' + abcd'

from U_i import *

class TestQuineMcCluskey(unittest.TestCase):
    def test_lista_de_termos(self):
        self.assertEquals(lista_de_termos("xz'"), ["xz'"])
        self.assertEquals(lista_de_termos("x'y'z + x'yz'"), ["x'y'z", "x'yz'"])
        self.assertEquals(lista_de_termos("a'b'c + a'bc' + ab'c' + a'bc + abc' + abc"), ["a'b'c", "a'bc'", "ab'c'", "a'bc", "abc'", "abc"])
        
    def test_transforma_em_binario(self):
        self.assertEquals(transforma_em_binario("abcdefg"),["1111111"])
        self.assertEquals(transforma_em_binario("ab'cd'ef'g"),["1010101"])
        self.assertEquals(transforma_em_binario("a'b'c' + a'bc + ab'c"),["000", "011", "101"])

    def test_numero_variaveis(self):
        self.assertEquals(numero_variaveis(["011"]), 3)
        self.assertEquals(numero_variaveis(["011", "110"]), 3)
        self.assertEquals(numero_variaveis(["01111100001"]), 11)

    def test_binario_para_decimal(self):
        self.assertEquals(binario_para_decimal("000"), 0)
        self.assertEquals(binario_para_decimal("001"), 1)
        self.assertEquals(binario_para_decimal("010"), 2)
        self.assertEquals(binario_para_decimal("011"), 3)
        self.assertEquals(binario_para_decimal("100"), 4)

    def test_separa_indices(self):
        self.assertEquals(separa_indices(["000", "101", "110", "001", "011", "100"]), [['000'],['001', '100'], ['101', '110', '011']])
        self.assertEquals(separa_indices(["001", "100", "111"]), [["001", "100"],["111"]])

    #def teste_compara_indices(self):
        #self.assertEquals(compara_indices(3, ['001', '011', '100', '1000', '101', '110']), (['0_1', '_01', '10_', '1_0', '10_', '1_0'], [], {'0_1': [1, 3], '_01': [1, 5], '10_': [8, 5], '1_0': [8, 6]}))
        #self.assertEquals(compara_indices(3, ['00_', '_00', '0_1', '_01', '10_', '1_0'], []), (['_0_', '_0_'], ['0_1', '1_0'], {'00_': [0, 1], '_00': [0, 4], '0_1': [1, 3], '_01': [1, 5], '10_': [4, 5], '1_0': [4, 6], '_0_': [0, 1, 4, 5]}))
        #self.assertEquals(compara_indices(3, ['_0_', '_0_'], ['0_1', '1_0', '0_1', '1_0']), ([], ['0_1', '1_0', '0_1', '1_0', '_0_', '_0_'], {'00_': [0, 1], '_00': [0, 4], '0_1': [1, 3], '_01': [1, 5], '10_': [4, 5], '1_0': [4, 6], '_0_': [0, 1, 4, 5]}))
        #self.assertEquals(compara_indices(3, ['_0_', '_0_'], ['0_1', '1_0', '0_1', '1_0', '_0_', '_0_', '_0_', '_0_', '0_1', '1_0', '0_1', '1_0', '_0_', '_0_', '_0_', '_0_', '0_1', '1_0', '0_1', '1_0']), ([], ['0_1', '1_0', '0_1', '1_0', '_0_', '_0_', '_0_', '_0_', '0_1', '1_0', '0_1', '1_0', '_0_', '_0_', '_0_', '_0_', '0_1', '1_0', '0_1', '1_0', '_0_', '_0_'], {'00_': [0, 1], '_00': [0, 4], '0_1': [1, 3], '_01': [1, 5], '10_': [4, 5], '1_0': [4, 6], '_0_': [0, 1, 4, 5]}))

    #def teste_compara_n_vezes(self):
        #self.assertEquals(compara_n_vezes(3, ['000', '001', '011', '100', '101', '110']), (['0_1', '1_0', '_0_', '_0_'], {'0_1': [1, 3], '1_0': [4, 6], '_0_': [0, 1, 4, 5]}))
        #self.assertEquals(compara_n_vezes(4, ["0000", "0011", "0110", "0101", "1100"]), (['1', '0000', '0011', '0110', '0101', '1100'], {}))
    
    def teste_calcula_crivo(self):
        self.assertEquals(calcula_crivo({'0_1': [1, 3], '1_0': [4, 6], '_0_': [0, 1, 4, 5]}), ['0_1', '1_0', '_0_'])

    def teste_completa_variaveis(self):
        self.assertEquals(completa_variaveis(["0", "100"]), ["000", "100"])
        self.assertEquals(completa_variaveis(["0", "100", "1001001"]), ["0000000", "0000100", "1001001"])
        self.assertEquals(completa_variaveis(["0", "10010110", "101"]), ["00000000", "10010110", "00000101"])

    def teste_transforma_em_variaveis(self):
        self.assertEquals(transforma_em_variaveis("a'b'c' + ab'c + abc' + a'b'c + a'bc + ab'c'", 3, ['0_1', '1_0', '_0_']), "a'c + ac' + b'")