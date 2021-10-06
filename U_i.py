from Quine_McCluskey import *

def verifica_opcao(opcao, expressao_ou_binario_ou_decimais):
    """
    obseva a opcao que o usario vai mandar a expressao e faz as alteracoes com base em cada opcao:
    0: transforma variaveis em binario
    1: pega o input e coloca em uma lista
    2: transforma de decimal para binario

    Args:
        opcao ([Int]): opcao da expressao
        expressao_ou_binario_ou_decimais ([str]): expressao que pode ser em variaveis, binarios ou minetermos

    Returns:
        binarios [List]: Lista de binarios
    """
    if opcao == 0:
        binarios = transforma_em_binario(expressao_ou_binario_ou_decimais)
    elif opcao == 1:
        binarios = list(expressao_ou_binario_ou_decimais.split(CARACTERE_SEPARAR))
    elif opcao == 2:
        binarios = []
        decimais = list(map(int, expressao_ou_binario_ou_decimais.split(CARACTERE_SEPARAR)))
        
        for d in decimais:
            binarios.append(str(format(d, "b")))

        binarios = completa_variaveis(binarios)

    return binarios

def imprime_opcoes():
    """
    Imprime as opções de entrada
    """
    print(("""{}
    DIGITE:
         ______________________________________________________________________
        |                                                                      |
        |   {}0 {}-> {}Para Calcular passando a Expressão com Variaveis              |
        |   {}1 {}-> {}Para Calcular passando a Expressão com Binários               |
        |   {}2 {}-> {}Para Calcular passando a Expressão com Minetermos(Decimais)   |
        |______________________________________________________________________|
    {}""").format(CYAN, YELLOW, RED, CYAN, YELLOW, RED, CYAN, YELLOW, RED, CYAN, RESET))

def imprime_resultados(string_numeros_simplificados, string_crivo, simplificado_ao_maximo):
    """
    Imprime os resultados.
    """
    print("""
    ______________________________________________

        {}Numeros Simplificados: {}{}
        {}Com o Mapa de Crivo: {}{}
        {}Expressão Simplificada: {}{}
    ______________________________________________{}
    """.format(RED, YELLOW, string_numeros_simplificados, RED, YELLOW, string_crivo, RED, YELLOW, simplificado_ao_maximo, RESET))
 

imprime_opcoes()

opcao = int(input("{}       OPÇÃO: {}".format(GREEN, YELLOW)))
expressao_ou_binario_ou_decimais = input("\n    {}INFORME A EXPRESSÃO: \n       {}Y = {}".format(CYAN, GREEN, YELLOW))

binarios = verifica_opcao(opcao, expressao_ou_binario_ou_decimais)
numeros_simplificados = compara_n_vezes(binarios)[1]
crivo = calcula_crivo(numeros_simplificados)
simplificado_ao_maximo = transforma_em_variaveis(expressao_ou_binario_ou_decimais, binarios, crivo)

string_numeros_simplificados = ""
string_crivo = ""

for num in numeros_simplificados:
    string_numeros_simplificados += num + " "

for c in crivo:
    string_crivo += c + " "

imprime_resultados(string_numeros_simplificados, string_crivo, simplificado_ao_maximo)