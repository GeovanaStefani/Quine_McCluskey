from Constantes import *

def transforma_em_binario(termos):
    """
    Transforma os termos, em binarios.

    O primeiro for percorre a lista de termos para poder verificar cada um.
    O segundo for, analisa todos os caracteres do termo, verificando apenas as variaveis, não os sinais de barramento.
    Dessa forma, é observado se o proximo elemento dessa variavel é o sinal de barramento, se sim, uma variavel auxiliar concatena o 0, se não, concatena o 1.

    Args:
        expressao ([String]): Expressao com a soma de n termos, cada um contendo variáveis barradas (a'), ou não (a).

    Returns:
        binarios [List]: Lista de binarios
    """
    binarios = []

    for termo in termos:
        aux = ""
        for t in range(len(termo)):
            if termo[t] != CARACTERE_BARRAMENTO:
                if t+1 <= len(termo)-1 and termo[t+1] == CARACTERE_BARRAMENTO:
                    aux += BINARIO_0
                else:
                    aux+= BINARIO_1
        binarios.append(aux)
    
    binarios.sort()

    return binarios

def numero_variaveis(binarios):
    """ 
    Conta o tanto de variáveis que a expressao tem, analisando pelo primeiro termo da lista de termos.

    Args:
        binarios ([List]): Lista de numeros em binário.

    Returns:
        qntd_variaveis ([Int]): Quantidade de ter variáveis que o termo possui
    """

    termo = binarios[0]
    qntd_variaveis = len(termo)

    return qntd_variaveis

def binario_para_decimal(binario):
    """
    Para transformar em decimal é preciso saber quantos elementos tem o numero, 
    fazendo o somatorio de cada um multiplicado por 2 (a base em binário), elevado a quantidade de elementos -1.
    
    EX: 110
        = 1*(2**2) + 1*(2**1) + 0*(2**0) = 6

    Args:
        binario ([String]): Numero em binario para calcular o tamanho do numero.

    Returns:
        decimal (Int): Numero em decimal
    """

    qntd_numeros = len(binario)
    decimal = 0
    for numero in binario:
        decimal+=(int(numero)*(BASE_BINARIA**(qntd_numeros-1))) 
        qntd_numeros -= 1
    
    return decimal

def separa_indices(binarios):
    """
    Para fazer o Quine-McCluskey é preciso separar os binarios em indíces, eles são a quantidade de 1's que o número tem
    Dessa forma, eu preciso de uma lista com várias listas dentros, cada uma posicionada no indice correto.
    Então, coloquei em uma lista, uma tupla para cada  binario e o seu indice correspondente.
    Além disso, verifiquei qual era o maior indice, para saber o total de indices
    Na lista que criei para colocar outras listas separadas pelo seu indice, adicionei n listas vazias, indo de 0 até o maior_indice+1 
    Depois percorri a lista de tuplas e fui adicionando na minha lista ordenada pelos indices os numeros em binario correspondentes a cada um.
    Ao final, removi todas as listas vazias que restaram, pois meu indice poderia ir até o 7, no entanto poderia não ter nenhum indice 3, por exemplo.

    Args:
        binarios ([List]): Lista de numeros em binário.

    Returns:
        indices [List]: Uma lista com outras listas dentro, cada uma dela contendo os numeros binarios de acordo com o indice de cada uma
    """

    maior_indice = 0
    indice_correspondente = []
    indices = []

    for binario in binarios:
        indice = binario.count(BINARIO_1)
        if indice > maior_indice:
            maior_indice = indice

        indice_correspondente.append((binario, indice))

    for l in range(maior_indice+1):
        indices.append([])

    for i in indice_correspondente:
        indices[i[1]].append(i[0])

    for m in indices:
        if len(m) == 0 : #avaliar isso: or m[0] == BINARIO_0*numero_variaveis(binarios)
            indices.remove(m)

    return indices

def verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo):
    """
    Observa a string inteira, se houver o caractere diferente, significa que nao tem como transformar, e nem eh preciso.

    Args:
        qntd_variaveis ([Int]): Diz a quantidade de variaveis
        termo ([String]): O termo que deve ser verificado

    Returns:
       pode_transformar_em_deci [Boolean]: variavel que diz se pode ou nao transformar
    """
    pode_transformar_em_decimal = True
    for f in range(qntd_variaveis):  #so transforma os valores para decimal, caso eles possam ser valores inteiros
        if termo[f] == CARACTERE_DIFERENTE :
            pode_transformar_em_decimal = False

    return pode_transformar_em_decimal

def adiciona_no_dicionario_os_termos_comparados(qntd_variaveis, decimais_comparados, termo_i_aux, termo_i = 0, termo_i_mais_1 = 0):
    """
    Adiciona no dicionario os termos que foram comparados

    Args:
        qntd_variaveis ([Int]): Quantidade de variaveis
        decimais_comparados ([Dict]): Dicionario com os decimais comparados
        termo_i_aux ([String]): Uma string nova com o caractere marcando os valores que estão diferentes Ex: '1_0'
        termo_i (int, optional): O primeiro termo da comparacao. Eh opcional, pois se o numero nao tiver comparacoes, ele ja vem no termo_aux. Defaults to 0.
        termo_i_mais_1 (int, optional): o segundo termo da comparacao. Eh opcional, pois se o numero nao tiver comparacoes, ele ja vem no termo_aux. Defaults to 0.

    Returns:
        decimais_comparados [Dict]: O dicionario
    """

    if termo_i == 0 and termo_i_mais_1 == 0:
        pode_transformar_em_decimal = verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo_i_aux)
        if pode_transformar_em_decimal:
            decimais_comparados[termo_i_aux] = [binario_para_decimal(termo_i_aux)]
    else:
        pode_transformar_em_decimal_1 = verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo_i)
        pode_transformar_em_decimal_2 = verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo_i_mais_1)
                    
        if pode_transformar_em_decimal_1 and pode_transformar_em_decimal_2:
            decimais_comparados[termo_i_aux] = ([binario_para_decimal(termo_i), binario_para_decimal(termo_i_mais_1)])
            if termo_i in decimais_comparados:
                del decimais_comparados[termo_i]
            if termo_i_mais_1 in decimais_comparados:
                del decimais_comparados[termo_i_mais_1]
        else:   #Se nao puder transformar em binario, significa que a compracao ja esta em outra tabela, logo os valores que eram para serem transformados em decimais ja foram, e agora e so juntar esses numeros para o px termo
            decimais_comparados[termo_i_aux] = []
            for w in range(COMPARACOES_POR_VEZ):
                decimais_comparados[termo_i_aux].append(decimais_comparados[termo_i][w])
                decimais_comparados[termo_i_aux].append(decimais_comparados[termo_i_mais_1][w])

    return decimais_comparados

def adiciona_na_lista_termos_que_nao_sairam_da_interacao(termo, sairam_da_interacao):
    """
    Se o termo nao sair da lista de comparacao da funcao de comparar indices, entao ele e adicionado em uma lista.

    Args:
        termo ([String]): o termo para ser adicionado.
        sairam_da_interacao ([List]): Com os valores que ja estao na lista

    Returns:
        sairam_da_interacao ([List]): Com o elemento adicionado
    """
    if termo not in sairam_da_interacao: 
        sairam_da_interacao.append(termo)

    return sairam_da_interacao

def compara_indices(qntd_variaveis, binarios, nao_sairam = [], decimais_comparados = {}):
    """
    Precisa-se comparar cada numero de um indice por todos os numeros do proximo indice.
    Caso na comparacao so exista um numero diferente, ele e colocado na lista para ser comparado novamente

    E os valores que nao conseguem ser comparados sao armazenados para serem usados na hora de montar a expressao.

    Alem disso, esta sendo guardado em um dicionario os valores que foram usados na comparacao, so quem em decimal.

    Args:
        qntd_variaveis ([Int]): Quantidade de variaveis
        binarios ([List]): Lista com binarios;

        nao_sairam ([List]): Lista com os valores que nao sairam da expressao, e por isso serão usados no momento de montar a expressão simplificada.
        caso nao seja informada nenhuma lista, recebe por default uma vazia;

        decimais_comparados ([Dict]): Dicionario que tem como chave o termo ja comparado e como valor, os respectivos numeros em decimal que foram usados para fazer a sua comparacao.
        caso nao seja informado nenhum dicionario, recebe por default um vazio.

    Returns:
        lista_para_ser_comparada_novamente ([List]): Lista com os binarios já comparados, para ser comparada novamente;

        nao_sairam ([List]): Lista com os valores que nao sairam da expressao, e por isso serão usados no momento de montar a expressão simplificada.;

        decimais_comparados([Dict]): Dicionario que tem como chave os binarios que foram transformados a partir da comparacao de outros 2,
        e como valor tem uma lista com os valores em decimais que foram usados na compracao dele.
    """

    indices = separa_indices(binarios)
    tamanho_indices = len(indices)
    sairam_da_interacao = []
    lista_para_ser_comparada_novamente = []


    for binarios_indice_i in indices: #pega as listas dentro da lista de indices
        indice_da_px_lista = indices.index(binarios_indice_i)+1 # pega o indice da px lista da lista de indices

        if indice_da_px_lista <= tamanho_indices-1: # verifica se esse px indice existe na lista
            binarios_indice_i_mais_1 = indices[indice_da_px_lista]  #pega a lista no px indice

            for termo_i in binarios_indice_i: #pega cada termo que tem dentro da lista
                for termo_i_mais_1 in binarios_indice_i_mais_1: #pega cada termo dentro da px lista
                    cont = 0
                    termo_i_aux = ""
                    for interador in range(qntd_variaveis):  #vai olhar cada numero dos termos comparando
                        if termo_i[interador] != termo_i_mais_1[interador]:
                            cont += 1
                            termo_i_aux += CARACTERE_DIFERENTE
                        else:
                            termo_i_aux += termo_i[interador]

                    if cont == 1: # so pode ter um termo diferente para poder sair
                        lista_para_ser_comparada_novamente.append(termo_i_aux)

                        sairam_da_interacao = adiciona_na_lista_termos_que_nao_sairam_da_interacao(termo_i, sairam_da_interacao)
                        sairam_da_interacao = adiciona_na_lista_termos_que_nao_sairam_da_interacao(termo_i_mais_1, sairam_da_interacao)

                        decimais_comparados = adiciona_no_dicionario_os_termos_comparados(qntd_variaveis, decimais_comparados, termo_i_aux, termo_i, termo_i_mais_1)

                    else:
                        decimais_comparados = adiciona_no_dicionario_os_termos_comparados(qntd_variaveis, decimais_comparados, termo_i)
                        decimais_comparados = adiciona_no_dicionario_os_termos_comparados(qntd_variaveis, decimais_comparados, termo_i_mais_1)
    
        for b_i in binarios_indice_i:
            if b_i not in sairam_da_interacao:
                nao_sairam.append(b_i)

    return lista_para_ser_comparada_novamente, nao_sairam, decimais_comparados

def compara_n_vezes(qntd_variaveis, binarios):
    """
    Enquanto ainda houver elementos na lista que foi comparada, ela deve ser comparada novamente.

    Args:
        qntd_variaveis ([Int]): Quantidade de variaveis
        binarios ([type]): Lista com binarios.

    Returns:
        lista_para_ser_comparada ([List]): Lista vazia sem mais comparacoes;

        decimais_comparados_so_com_termos_nao_sairam ([Dict]): O dicionario com os termos e valores em decimal que foram comparados, só que apenas os que nao sairam da interacao,
        e por isso, precisam ser analisados.
    """

    lista_para_ser_comparada, nao_sairam, decimais_comparados= compara_indices(qntd_variaveis, binarios)
    while len(lista_para_ser_comparada) != 0:
        lista_para_ser_comparada, nao_sairam, decimais_comparados = compara_indices(qntd_variaveis, lista_para_ser_comparada, nao_sairam, decimais_comparados)

    decimais_comparados_so_com_termos_nao_sairam = {}
    for elem in nao_sairam:
        if elem in decimais_comparados:
            decimais_comparados_so_com_termos_nao_sairam[elem] = decimais_comparados[elem]
    
    return nao_sairam, decimais_comparados_so_com_termos_nao_sairam

def todos_os_decimais_comparados(decimais_comparados):
    """
    Faz uma lista com os valores de todas as chaves, para poder ser analisado quando tiver montando o mapa de crivo.

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.

    Returns:
        todos os decimais [List]: Lista com todos esses decimais que foram usados na comparacao.
    """
    todos_decimais = []
    for elem in decimais_comparados:
        for decimal in decimais_comparados[elem]:
            todos_decimais.append(decimal)   #faz uma lista com todos os decimais que estao sendo usados

    return todos_decimais

def crivo_generico(decimais_comparados, todos_decimais, decimais_depois_do_crivo):
    """
    Faz a primeira comparacao do crivo, analisando quais numeros que participaram da expressao final.
    são eles, apenas os decimais que foram usados só uma vez.
    Além disso, faz uma lista com elementos que precisaram ir para o segundo round do crivo, criando um dicionario de contribuicoes para ele

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.
        todos os decimais [List]: Lista com todos esses decimais que foram usados na comparacao.
        decimais_depois_do_crivo ([List]): Os decimais que ainda restaram na comparacao depois do crivo.

    Returns:
       simplificados [List]: Com os elementos que foram simplificados nessa rodada
       decimais_depois_do_crivo [List]: Com os decimais que os numeros simplificados foram usados
       dic_contribuicoes [Dict]: Dicionario, que tem como chave o termo e como o valor o tanto de contribuicoes que ele tem
       precisa_ordenar [List]: Com os elementos que irão para a parte 2 do crivo
    """
    dic_contribuicoes = {}
    simplificados = []
    precisa_ordenar = []

    for elem in decimais_comparados:  #Percorre o dicionario
        num_contribuicoes = 0
        validador = False
        for decimal in decimais_comparados[elem]:
            contador = todos_decimais.count(decimal) 
            if contador < COMPARACOES_POR_VEZ:  
                validador = True

        if validador:
            for decimal in decimais_comparados[elem]:
                if decimal not in decimais_depois_do_crivo:
                    num_contribuicoes += 1
                    decimais_depois_do_crivo.append(decimal)

            simplificados.append(elem) #Lista so com as chaves do dicionario que foram simplificados ao maximo

            if elem not in dic_contribuicoes:
                dic_contribuicoes[elem] = num_contribuicoes
        else:
            precisa_ordenar.append(elem)

            
    return simplificados, decimais_depois_do_crivo, dic_contribuicoes, precisa_ordenar

def compara_termos_ordenados(decimais_comparados, precisa_ordenar, decimais_crivo, dic_contribuicoes):
    """
    Depois que foi percorrido pela primeira vez o crivo, uma nova verificacao precisa ser feita.
    Antes disso, é preciso pegar as contribuicoes dos elementos que serão analisados no round 2

    Args:
        decimais_comparados ([Dict]): Com os termos e uma lista com os decimais que foram comparados para chegar nele
        precisa_ordenar ([List]): Com os elemetos que participaram do round 2
        decimais_crivo ([List]): Com os decimai que já estão no cirvo
        dic_contribuicoes ([Dict]): Dicionario com o termo e as contribuicoes dele

    Returns:
        dic_contribuicoes ([Dict]): Dicionario com o termo e as contribuicoes dele
    """
    for termo in precisa_ordenar:
        num_contribuicoes = 0
        for decimal in decimais_comparados[termo]:
            if decimal not in decimais_crivo:
                num_contribuicoes += 1
        
        if termo not in dic_contribuicoes:
                dic_contribuicoes[termo] = num_contribuicoes

    return dic_contribuicoes

def compara_ordenados(ordenados, decimais_comparados, decimais_crivo, simplificados):
    """
    Round 2 do crivo, analisando os termos que já estão ordenados

    Args:
        ordenados ([List]): Com os elementos que serão analisados
        decimais_comparados ([Dict]): Dicionario que tem o termo como chave e como valor os decimais comparados que foram usados para chegar no termo
        decimais_crivo ([List]): Decimais que já estão no crivo
        simplificados ([List]): Com os termos que ja foram simplificados

    Returns:
        simplificados_2 [List]: Com os termos simplificados na segunda rodada
    """
    simplificados_2 = []
    for ordenado in ordenados:
        for decimal in decimais_comparados[ordenado]:
            if decimal not in decimais_crivo:
                decimais_crivo.append(decimal)
                if ordenado not in simplificados:
                    simplificados_2.append(ordenado)

    return simplificados_2

def repete_crivo_nas_duas_opcoes(decimais_comparados, todos_decimais):
    """
    Chamada da funcao nos dois casos mencionados

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.
        todos os decimais [List]: Lista com todos esses decimais que foram usados na comparacao.

    Returns:
        simplificados_1, simplificados_2 [List]: Com os termos simplificados em cada caso
    """

    simplificados_1, decimais_depois_do_crivo, dic_contribuicoes, precisa_ordenar = crivo_generico(decimais_comparados, todos_decimais, [])
    dic_contribuicoes = compara_termos_ordenados(decimais_comparados, precisa_ordenar, decimais_depois_do_crivo, dic_contribuicoes)
    ordenados = ordena_por_contribuicoes(dic_contribuicoes, precisa_ordenar)
    simplificados_2 = compara_ordenados(ordenados, decimais_comparados, decimais_depois_do_crivo, simplificados_1)

    return simplificados_1, simplificados_2

def ordena_por_contribuicoes(dic_contribuicoes, precisa_ordenar):
    """
    Analisa o dicionario com as contribuicoes, e ordena de acordo com quem tem mais contribuicoes

    Args:
        dic_contribuicoes ([Dict]): Com os termos e a quantidade de contribuicoes
        precisa_ordenar ([List]): Com os elementos que precisaram ser ordenados

    Returns:
        ordenados[List]: com os termos ordenados
    """
    dic_repetidos = {}
    lista_contribuicoes = []
    lista_termos_correspondentes = []

    for elem in precisa_ordenar:
        if dic_contribuicoes[elem] in lista_contribuicoes:
            if dic_contribuicoes[elem] not in dic_repetidos:
                dic_repetidos[dic_contribuicoes[elem]] = []

            indice = lista_contribuicoes.index(dic_contribuicoes[elem])
            if lista_termos_correspondentes[indice] not in dic_repetidos[dic_contribuicoes[elem]]:
                dic_repetidos[dic_contribuicoes[elem]].append(lista_termos_correspondentes[indice])

            dic_repetidos[dic_contribuicoes[elem]].append(elem)
            
        else:
            lista_contribuicoes.append(dic_contribuicoes[elem])
            lista_termos_correspondentes.append(elem)

    for a in range(len(lista_contribuicoes)):
        for b in range(a+1, len(lista_contribuicoes)):
            if lista_contribuicoes[a] <= lista_contribuicoes[b]:
                temp = lista_termos_correspondentes[a]
                lista_termos_correspondentes[a] = lista_termos_correspondentes[b]
                lista_termos_correspondentes[b] = temp

                temp2 = lista_contribuicoes[a]
                lista_contribuicoes[a] = lista_contribuicoes[b]
                lista_contribuicoes[b] = temp2

    ordenados = lista_termos_correspondentes.copy()
    for num in dic_repetidos:
        indice = lista_contribuicoes.index(num)
        termo = lista_termos_correspondentes[indice]
        indice_termo = ordenados.index(termo)
        del ordenados[indice_termo]
        for i in range(len(dic_repetidos[num])):
            ordenados.insert(indice_termo+i, dic_repetidos[num][i])

    return ordenados


def cria_dicionario_mais_simplificado(decimais_comparados, simplificados_2):
    """
    Cria o dicionario que vai ser analisado, ou seja, um mais simplificado que o anterior.

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.
        simplificados_2 ([List]): Com a ultima lista de termos simplificados que teve

    Returns:
        Decimais_comparados_2 [Dict]: Dicionario com termos agora mais simplificados
    """
    decimais_comparados_2 = {}
    for elem in decimais_comparados:
        for s in simplificados_2:
            if elem == s:
                decimais_comparados_2[elem] = decimais_comparados[elem]

    return decimais_comparados_2
    
def repete_processo_do_crivo(decimais_comparados, eh_primeira_vez, simplificados, simplificados_x):
    """
    O processo do Crivo precisa ser repetido varias vezes dependendo do numero de variaveis

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.
        eh_primeira_vez ([Boolean]): Diz se eh a primeira vez que ta rodando
        simplificados ([List]): Lista comos termos simplificados
        simplificados_x ([List]): Com os simplificados que vieram em outra rodada

    Returns:
        simplificados[List]: Com os termos simplificados
        simplificados_2[List]: Ultima lista com termos simplificados que sera necessario para verificar a px.
    """
    if not eh_primeira_vez:
        decimais_comparados = cria_dicionario_mais_simplificado(decimais_comparados, simplificados_x)

    todos_decimais = todos_os_decimais_comparados(decimais_comparados)
    simplificados_1, simplificados_2 = repete_crivo_nas_duas_opcoes(decimais_comparados, todos_decimais)

    return simplificados_1, simplificados_2


def calcula_crivo(decimais_comparados):
    """
    O crivo minimiza ainda mais a expressao.
    Para isso, pega-se todos os valores (em decimal) que foram comparados ate chegar naquele termo.
    Se todos os numeros ja estiverem sendo usados por outros termos, o termo é retirado. 
    No entanto, se nem todos os decimais ficaram na expressao, uma nova anlise tem que ser ealizada, adicionando eles.

    Args:
        decimais_comparados ([Dict]): Dicionario com decimais ja comparados.

    Returns:
        lista_final [List]: Lista com os termos simplificados ao maximo
    """
    lista_com_lista_dos_processos = []
    todos_os_simplificados= []
    simplificados_x= []
    eh_primeira_vez = True
    lista_final = []

    cont = 0
    while True:
        todos_os_simplificados, simplificados_x = repete_processo_do_crivo(decimais_comparados, eh_primeira_vez, todos_os_simplificados, simplificados_x)
        
        if cont > 0:
            eh_primeira_vez = False
        
        simplificados_aux = todos_os_simplificados.copy()
        
        lista_com_lista_dos_processos.append(simplificados_aux)
        cont += 1

        if len(simplificados_x) == 0:
            break

    for lista in lista_com_lista_dos_processos:
        for num in lista:
            lista_final.append(num)

    return lista_final

def ordena_simplificados(numeros_simplificados, crivo):
    """
    Vai ordenando a partir do primeiro dicionario com todos os termos

    Args:
        numeros_simplificados ([Dict]): Com todos os termos e valores comparados
        crivo ([List]): Com os elementos passados pelo Crivo

    Returns:
        ordenados [List]: termos ordenados
    """
    ordenados = []
    for elem in numeros_simplificados:
        if elem in crivo:
            ordenados.append(elem)
    
    return ordenados

def completa_variaveis(binarios):
    """
    Quando transforma os valores de decimal para binario, retirasse os 0's que ficam no comeco, e isso nao pode acontecer.
    Então eu completo com o tanto de variaveis que o numero tem

    Args:
        binarios ([Lista]): lista de binarios

    Returns:
        binarios [List]: binarios completados
    """
    maior = 0
    for b in binarios:
        if len(b)> maior:
            maior = len(b)

    for b in binarios:
        aux = b
        while len(aux) < maior:
            aux = "0" + aux

        indice = binarios.index(b)
        binarios[indice] = aux

    return binarios
            
def transforma_em_variaveis(qntd_variaveis, simplificados_ao_maximo):
    """
    Transforma os elementos que nao sairam da lista de comparacao em variaveis e, consequentemente, termos da expressao.
    Bem parecida com a funcao que transforma em binarios, sendo que ao contrario.

    Args:
        expressao ([String]): Expressao com a soma de n termos, cada um contendo variáveis barradas (a'), ou não (a).
        binarios ([List]): Lista com binarios
        simplificados_ao_maximo ([List]):  Lista com os numeros simplificados ao maximo

    Returns:
        expressao_simplificada ([String]): expressao inicial, so que agora simplificada
    """

    variaveis = VARIAVEIS_POSSIVEIS
    expressao_simplificada = ""

    for num in simplificados_ao_maximo:
        aux = ""
        for i in range(qntd_variaveis):
            if num[i] == BINARIO_0:
                aux += variaveis[i]+CARACTERE_BARRAMENTO
            elif num[i] == BINARIO_1:
                aux += variaveis[i]
        
        expressao_simplificada += aux+CARACTERE_SOMA

    return expressao_simplificada.rstrip(CARACTERE_SOMA)