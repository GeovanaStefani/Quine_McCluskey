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
        termos, eh_valida, mensagem = valida_expressao2(opcao, expressao_ou_binario_ou_decimais)
        binarios = transforma_em_binario(termos)
    elif opcao == 1:
        binarios, eh_valida, mensagem = valida_expressao2(opcao, expressao_ou_binario_ou_decimais)
        binarios = completa_variaveis(binarios)
        if eh_valida:
            eh_valida, mensagem = valida_expressao1(eh_valida, binarios)
    elif opcao == 2:
        binarios = []
        decimais, eh_valida, mensagem = valida_expressao2(opcao, expressao_ou_binario_ou_decimais)
        
        for d in decimais:
            binarios.append(str(format(d, "b")))  

        binarios = completa_variaveis(binarios)

    return binarios, eh_valida, mensagem

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
                ___________________________________________________________
                                                    
                {}{}{}  
                __________________________________________________________
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
        informa_invalidade("Informe uma opção válida")
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
        binarios, eh_valida, mensagem = verifica_opcao(opcao, expressao)
        if not eh_valida:
            informa_invalidade(mensagem)
            expressao = input("{}       Y = {}".format(GREEN, YELLOW))
        else:
            break

    return binarios

def valida_expressao2(opcao, expressao):
    lista_minitermos = []
    expressao = expressao.strip()
    expressao = expressao.strip(CARACTERE_SEPARAR)
    ultimo_indice = len(expressao)-1
    aux = ""
    for i in range (len(expressao)):
        eh_caractere_de_separar = False

        try:
            if opcao==1 or opcao == 2:
                numero = int(expressao[i])
            elif not(expressao[i] in VARIAVEIS_POSSIVEIS or expressao[i] == CARACTERE_BARRAMENTO):
                eh_caractere_de_separar = True

        except:
            eh_caractere_de_separar = True

        eh_ultimo = False

        if not eh_caractere_de_separar:
            aux += expressao[i]
            if i == ultimo_indice:
                eh_ultimo = True

        if (eh_caractere_de_separar and aux!= "") or eh_ultimo:
            if opcao == 2:
                aux = int(aux)
            lista_minitermos.append(aux)
            aux = ""

    eh_valida = True
    mensagem = ""
    qntd_minitermos = len(lista_minitermos)
    if qntd_minitermos == 0:
        mensagem = "Nenhum número informado, por favor, informe a expressao de acordo com o formato estabelecido"
        eh_valida = False
    elif  qntd_minitermos == 1:
        mensagem = "Você precisa informar no mínimo dois minitermos para serem comparados!"
        eh_valida = False
    
    return lista_minitermos, eh_valida, mensagem

def valida_expressao1(eh_valida, binarios):
    mensagem = ""
    for termo in binarios:   
        for t in termo:
            if t!=BINARIO_0 and t!=BINARIO_1:
                eh_valida = False
                mensagem = "Essa opção, só aceita números em binário, 0 ou 1!"

    return eh_valida, mensagem


def valida_saida(simplificado_ao_maximo, string_numeros_simplificados, string_crivo):
    if len(simplificado_ao_maximo) == 0: #se nao pode ser simplificada, recebe a propria expresao
       imprime_sem_simplificacoes()
    else:
        imprime_resultados(string_numeros_simplificados, string_crivo, simplificado_ao_maximo)

while True:
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
        break