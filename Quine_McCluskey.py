from Constantes import *

def lista_de_termos(expressao):
    """ 
    Transforma a expressao em uma lista de termos

    Args:
        expressao ([String]): Expressao com a soma de n termos, cada um contendo variáveis barradas (a'), ou não (a). 

    Returns:
        termos ([List]): Lista com todos os termos, sem o +.
    """
    termos = expressao.split(CARACTERE_SOMA)

    return termos

def transforma_em_binario(expressao):
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
    termos = lista_de_termos(expressao)
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

def crivo_generico(decimais_comparados, todos_decimais, verificador, decimais_depois_do_crivo):
    """
    Ao calcular o Crivo, percebe-se duas situacoes:
    - A primeira, eh que os valores que devem ir pra expressao sao aqueles que nao podem mais ser simplificados,
    e seu numero nao eh utilizado mais de uma vez.
    - Jah a segunda situacao, eh aquela em que depois de se ter os primeiros numeros, eh analisado quais ainda estao faltando entrar, mesmo que estejam repetidos, pegando sempre o primeiro.

    O primeiro caso, identifiquei como 'C' remetendo ao contador, e o segundo com 'L', pois eh analisado se o elemento ja esta na lista.

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.
        todos os decimais [List]: Lista com todos esses decimais que foram usados na comparacao.
        verificador ([String]): 'C' ou 'L', dependendo do caso
        decimais_depois_do_crivo ([List]): Os decimais que ainda restaram na comparacao depois do crivo.

    Returns:
        [type]: [description]
    """
    simplificados_ao_maximo = []
    decimais_depois_do_crivo2 = []

    for elem in decimais_comparados:  #Percorre o dicionario
        validador = True 
        for decimal in decimais_comparados[elem]: #Percorre a Lista com os decimais que existe em cada valor das chaves
            if verificador == "C":
                contador = todos_decimais.count(decimal) #Primeiro caso, analisa se ha menos de dois elementos
                if contador < COMPARACOES_POR_VEZ:   #vai percorrendo a lista e se o numero tiver sido colocado na lista mais de uma vez, é pq tem em outros termos tbm, logo se todos os elem forem usados, pode sair.
                    validador = False
            elif verificador == "L":   #Segundo caso
                if decimal not in decimais_depois_do_crivo: #Se o elemento nao estiver na lista com todos os outros decimais, ele precisa ser incluido
                    validador = False
        
        if not validador:
            simplificados_ao_maximo.append(elem) #Lista so com as chaves do dicionario que foram simplificados ao maximo
            for d_c in decimais_comparados[elem]:
                if d_c not in decimais_depois_do_crivo: 
                    decimais_depois_do_crivo.append(d_c) #Adicionando na lista os elementos que ainda nao estao
                    decimais_depois_do_crivo2.append(d_c)
    
    if verificador == "L":
        decimais_depois_do_crivo = decimais_depois_do_crivo2.copy()

    return simplificados_ao_maximo, decimais_depois_do_crivo

def repete_crivo_nas_duas_opcoes(decimais_comparados, todos_decimais):
    """
    Chamada da funcao nos dois casos mencionados

    Args:
        decimais_comparados ([Dict]): Chave: Termos; Valores: Lista com os decimais que precisaram ser comparados para chegar nele.
        todos os decimais [List]: Lista com todos esses decimais que foram usados na comparacao.

    Returns:
        simplificados_1, simplificados_2 [List]: Com os termos simplificados em cada caso
    """

    simplificados_1, decimais_crivo1 = crivo_generico(decimais_comparados, todos_decimais, "C", [])
    simplificados_2 = crivo_generico(decimais_comparados, todos_decimais, "L", decimais_crivo1.copy())[0]

    return simplificados_1, simplificados_2

def adiciona_na_lista_simplificados(simplificados, simplificado_x):
    """
    Existe varias simplificacoes, e os elementos de cada lista precisam ser adionados em uma inteira

    Args:
        simplificados ([List]): Lista com todos os termos simplificados
        simplificado_x ([List]): Lista que vai ser adicionada dentro da que vai ter todos

    Returns:
        simplificados [List]: Com os novos termos adicionados.
    """
    for s in simplificado_x:
        if s not in simplificados:
            simplificados.append(s)

    return simplificados

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
    simplificados = adiciona_na_lista_simplificados(simplificados, simplificados_1)

    return simplificados, simplificados_2


def calcula_crivo(decimais_comparados, qntd_variaveis):
    """
    O crivo minimiza ainda mais a expressao.
    Para isso, pega-se todos os valores (em decimal) que foram comparados ate chegar naquele termo.
    Se todos os numeros ja estiverem sendo usados por outros termos, o termo é retirado. 
    No entanto, se nem todos os decimais ficaram na expressao, uma nova anlise tem que ser ealizada, adicionando eles.

    Args:
        decimais_comparados ([Dict]): Dicionario com decimais ja comparados.
        qntd_variaveis ([Int]): Quantidade de variaveis

    Returns:
        todos_os_simplificados [List]: Lista com os termos simplificados ao maximo
    """

    todos_os_simplificados = []
    simplificados_x = []
    eh_primeira_vez = True
    for i in range(qntd_variaveis//COMPARACOES_POR_VEZ):
        if i > 0:
            eh_primeira_vez = False
        todos_os_simplificados, simplificados_x = repete_processo_do_crivo(decimais_comparados, eh_primeira_vez, todos_os_simplificados, simplificados_x)

    return todos_os_simplificados

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
            
def transforma_em_variaveis(expressao_ou_binario_ou_decimais, qntd_variaveis, simplificados_ao_maximo):
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

    if len(expressao_simplificada) == 0: #se nao pode ser simplificada, recebe a propria expresao
        expressao_simplificada = expressao_ou_binario_ou_decimais

    return expressao_simplificada.rstrip(CARACTERE_SOMA)