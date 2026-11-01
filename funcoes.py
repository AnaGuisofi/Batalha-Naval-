def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []  #vai guardar as posições que o navio vai ocupar

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])  # aumenta a linha e mantém a coluna -> O NAVIO CRESCE PARA BAIXO

        else:
            posicoes.append([linha, coluna + i])  # mantém a linha e aumenta a coluna -> O NAVIO CRESCE PARA A DIREITA

    return posicoes  # vai devolver a lista completa após terminar