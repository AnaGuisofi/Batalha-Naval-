def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []  #vai guardar as posições que o navio vai ocupar

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])  # aumenta a linha e mantém a coluna -> O NAVIO CRESCE PARA BAIXO

        else:
            posicoes.append([linha, coluna + i])  # mantém a linha e aumenta a coluna -> O NAVIO CRESCE PARA A DIREITA

    return posicoes  # vai devolver a lista completa após terminar



def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)  # usa a função anterior para calcular as posições do novo navio

    if nome_navio not in frota:  # olha se esse tipo de navio ainda não está no dicionário
        frota[nome_navio] = []  # lista que vai guardar esses tipos de navios

    frota[nome_navio].append(posicoes)  # vai adicionar o novo navio -> sem apagar os navios anteriores

    return frota  # vai devolver a lista completa atualizada



def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:  # verifica se há navio na casa escolhida
        tabuleiro[linha][coluna] = "X"  # marca que acertou o navio

    elif tabuleiro[linha][coluna] == 0:  # verifica se a casa está vazia
        tabuleiro[linha][coluna] = "-"  # marca que o tiro acertou a água

    return tabuleiro  # devolve o tabuleiro atualizado