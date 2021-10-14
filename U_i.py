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

def imprime_sem_simplificacoes():
     print("""{}
         _______________________________________________________________
        |                                                               |
        |    A expressao informada não pode ser mais simplificada!      |
        |_______________________________________________________________|
     {}""".format(RED, RESET))

def informa_invalidade(informacao_invalida):
    print(""" {}
                        ____________________________________
                                                    
                            {}Informe uma {} válida{}  
                        ____________________________________
        """.format(RED, YELLOW, informacao_invalida, RED))

def valida_sair(sair):
    sair = sair.strip().upper()
    while sair != "S" and sair != "":
        sair = input("{}'S' para Sair, Enter para continuar: {}".format(GREEN, RESET))
        sair = sair.strip().upper()

    return sair

def valida_opcao(opcao):
    opcao = opcao.strip()
    while opcao != "0" and opcao != "1" and opcao != "2":
        informa_invalidade("opção")
        imprime_opcoes()
        opcao = input("{}       OPÇÃO: {}".format(GREEN, YELLOW))
        opcao = opcao.strip()

    return int(opcao)

def imprime_formato_de_entrada(opcao, exemplo, recado):
    """
    Imprime as opções de entrada
    """
    print(("""{}
         ______________________________________________________________________

            {}Formato de entrada:
                                                                              
            {}A entrada da Opção {} deve seguir esse formato:

                Ex: 
                                        {}{}     

            {}{}{}
         ______________________________________________________________________{}

    INFORME A EXPRESSÃO:{}""").format(YELLOW, RED, GREEN, opcao, YELLOW, exemplo, CYAN, recado, YELLOW, CYAN, RESET))

def formato_de_entrada_opcoes(opcao):
    if opcao == 0:
        exemplo = "abc + a'b'c + abc'"
        recado = """
        Nesse exemplo, é possivel observar que todos os termos possuem as mesmas
        variaveis. Além disso, para o caractere de barramamento (') Usa-se as 
        aspas simples. E para somar (' + ')."""

    elif opcao == 1:
        exemplo = "000,011,111"
        recado = """
        Nesse exemplo, é possivel observar que todos os termos possuem a mesma
        quantidade de variaveis. Além disso, são utilizados apenas os números
        1 ou 0. E para separar um termo de outro, usa apenas a vírgula sem 
        espaçamento."""

    elif opcao == 2:
        exemplo = "0,1,3,5,7"
        recado = """
        Nesse exemplo, é possivel observar que todos os minitermos são separados
        por vírgulas,sem espaçamento."""

    imprime_formato_de_entrada(opcao, exemplo, recado)


def valida_expressao(opcao, expressao):
    while True:
        expressao = expressao.strip()
        try:
            binarios = verifica_opcao(opcao, expressao)
            break
        except:
            informa_invalidade("expressão")
            expressao = input("{}       Y = {}".format(GREEN, YELLOW))

    return binarios

def valida_expressao2(opcao, expressao):
    #1,2,3
    while expressao != "":
        lista_minitermos = []
        expressao = expressao.strip()
        expressao = expressao.strip(CARACTERE_SEPARAR)
        ultimo_indice = len(expressao)-1
        aux = ""
        for num in expressao:
            eh_caractere_de_separar = False
    
            try:
                num = int(num)
            except:
                #if num == CARACTERE_SEPARAR or num == ESPACO:
                eh_caractere_de_separar = True

            eh_ultimo = False

            if not eh_caractere_de_separar:
                aux += str(num)
                indice = expressao.index(str(num))
                if indice == ultimo_indice:
                    eh_ultimo = True

            if (eh_caractere_de_separar and aux!= "") or eh_ultimo:
                lista_minitermos.append(int(aux))
                aux = ""

        qntd_minitermos = len(lista_minitermos)
        if qntd_minitermos == 0:
            print("não dá")
        elif  qntd_minitermos == 1:
            print("Você precisa informar no mínimo dois minitermos para serem comparados")
        print(lista_minitermos)
        expressao = input()
    
    return expressao


def valida_saida(simplificado_ao_maximo, string_numeros_simplificados, string_crivo):
    if len(simplificado_ao_maximo) == 0: #se nao pode ser simplificada, recebe a propria expresao
       imprime_sem_simplificacoes()
    else:
        imprime_resultados(string_numeros_simplificados, string_crivo, simplificado_ao_maximo)


valida_expressao2(1, input())

'''while True:
    imprime_opcoes()
    opcao = input("{}       OPÇÃO: {}".format(GREEN, YELLOW))
    opcao = valida_opcao(opcao)
    formato_de_entrada_opcoes(opcao)
    expressao_ou_binario_ou_decimais = input("{}        Y = {}".format(GREEN, YELLOW))
    binarios = valida_expressao(opcao, expressao_ou_binario_ou_decimais)

    qntd_variaveis = numero_variaveis(binarios)
    numeros_simplificados = compara_n_vezes(qntd_variaveis, binarios)[1]
    crivo = calcula_crivo(numeros_simplificados, qntd_variaveis)
    ordenados = ordena_simplificados(numeros_simplificados, crivo)
    simplificado_ao_maximo = transforma_em_variaveis(qntd_variaveis, ordenados)
    string_numeros_simplificados = ""
    string_crivo = ""

    for num in numeros_simplificados:
        string_numeros_simplificados += num + ESPACO

    for c in crivo:
        string_crivo += c + " "

    valida_saida(simplificado_ao_maximo, string_numeros_simplificados, string_crivo)

    sair = input("{}Deseja sair? Se sim, Digite 'S'. Caso o contrário, apenas Tecle Enter! {}".format(GREEN, RESET))
    sair = valida_sair(sair)

    if sair == "S":
        break'''