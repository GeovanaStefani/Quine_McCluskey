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

def binario_para_decimal(expressao):
    """
    Para transformar em decimal é preciso saber quantos elementos tem o numero, 
    fazendo o somatorio de cada um multiplicado por 2 (a base em binário), elevado a quantidade de elementos -1.
    
    EX: 110
        = 1*(2**2) + 1*(2**1) + 0*(2**0) = 6

    Args:
        expressao ([String]): Expressao com a soma de n termos, cada um contendo variáveis barradas (a'), ou não (a).

    Returns:
        decimais ([List]): Lista de decimais
    """

    binarios = transforma_em_binario(expressao)
    decimais = []

    for binario in binarios:
        qntd_numeros = numero_variaveis(expressao)
        decimal = 0
        for numero in binario:
            decimal+=(int(numero)*(2**(qntd_numeros-1)))
            qntd_numeros -= 1
        decimais.append(decimal)

    return decimais

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
        if len(m) == 0 or m[0] == "0"*numero_variaveis(binarios):
            indices.remove(m)

    return indices

def compara_indices(binarios):
    """
    Precisa-se comparar cada numero de um indice por todos os numeros do proximo indice.
    Caso na comparacao so exista um numero diferente, ele e colocado na lista para ser comparado novamente

    Args:
        binarios ([type]): Lista com binarios

    Returns:
        lista_para_ser_comparada_novamente ([List]): Lista com os binarios já comparados, para ser comparada novamente
    """
    indices = separa_indices(binarios)
    qntd_variaveis = numero_variaveis(binarios)
    tamanho_indices = len(indices)
    sairam_da_interacao = []
    lista_para_ser_comparada_novamente = []

     # [['001', '100'], ['011', '101', '110']]

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
                        if termo_i not in sairam_da_interacao: #fiz a funcao mas ainda nao uso essa lista de sairam da interacao
                            sairam_da_interacao.append(termo_i)
                        if termo_i_mais_1 not in sairam_da_interacao:
                            sairam_da_interacao.append(termo_i_mais_1)

                        print("O elemento do primeiro indice analisado {} saiu pois encontrou o termo {} na px lista que só tem um numero diferente".format(termo_i, termo_i_mais_1))
    
    return lista_para_ser_comparada_novamente

def compara_n_vezes(binarios):
    """
    Enquanto ainda houver elementos na lista que foi comparada, ela deve ser comparada novamente.

    Args:
        binarios ([type]): Lista com binarios

    Returns:
        lista_para_ser_comparada ([List]): Lista vazia sem mais comparacoes
    """
    
    lista_para_ser_comparada = compara_indices(binarios)
    while len(lista_para_ser_comparada) != 0:
        print(lista_para_ser_comparada)
        lista_para_ser_comparada = compara_indices(lista_para_ser_comparada)

    return lista_para_ser_comparada