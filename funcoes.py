# PARTE 1
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []  #vai guardar as posições que o navio vai ocupar

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])  # aumenta a linha e mantém a coluna -> O NAVIO CRESCE PARA BAIXO

        else:
            posicoes.append([linha, coluna + i])  # mantém a linha e aumenta a coluna -> O NAVIO CRESCE PARA A DIREITA

    return posicoes  # vai devolver a lista completa após terminar



# PARTE 2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)  # usa a função anterior para calcular as posições do novo navio

    if nome_navio not in frota:  # olha se esse tipo de navio ainda não está no dicionário
        frota[nome_navio] = []  # lista que vai guardar esses tipos de navios

    frota[nome_navio].append(posicoes)  # vai adicionar o novo navio -> sem apagar os navios anteriores

    return frota  # vai devolver a lista completa atualizada



# PARTE 3
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:  # verifica se há navio na casa escolhida
        tabuleiro[linha][coluna] = "X"  # marca que acertou o navio

    elif tabuleiro[linha][coluna] == 0:  # verifica se a casa está vazia
        tabuleiro[linha][coluna] = "-"  # marca que o tiro acertou a água

    return tabuleiro  # devolve o tabuleiro atualizado



# PARTE 4
def posiciona_frota(frota): 
    tabuleiro = []  # vai guardar as 10 linhas do tabuleiro

    for i in range(10):  # repete a criação de uma linha 10 vezes
        linha = [0] * 10  # cria uma nova linha com 10 casas vazias
        tabuleiro.append(linha)  # adiciona essa linha ao tabuleiro 

    for nome_navio in frota:  # percorre os tipos de embarcação
        for navio in frota[nome_navio]:  # percorre cada navio desse tipo
            for posicao in navio:  # percorre as posições ocupadas pelos navios
                linha = posicao[0]  # primeiro número da posição -> linha
                coluna = posicao[1]  # segundo número da posição -> coluna

                tabuleiro[linha][coluna] = 1  # marca que tem um navio

    return tabuleiro  # vai devolver o tabuleiro com os navios já posicionados



# PARTE 5
def afundados(frota, tabuleiro):
    quantidade = 0  # naios afundados

    for nome_navio in frota:  # passa pelos tipos de embarcação
        for navio in frota[nome_navio]:  # vai analisar cada navio desse tipo
            atingidas = 0  # zera a contagem de acertos para cada navio

            for posicao in navio:  # percorre as posições desse navio
                linha = posicao[0]  # pega a linha da posição
                coluna = posicao[1]  # pega a coluna da posição

                if tabuleiro[linha][coluna]  == "X":
                    atingidas += 1  # pra contar mais uma parte atingida

            if atingidas == len(navio):  # vai verificar se todas as partes foram atingidas
                quantidade += 1  # pra contar mais um navio afundado

    return quantidade  # vai devolver o total de navios afundados 



# PARTE 6 
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)  # vai calcular as posições que o novo navio ocuparia

    for posicao in posicoes:  # verifica cada posição do novo navio
        linha_atual = posicao[0]  # pega a linha dessa posição
        coluna_atual = posicao[1]  # pega a coluna dessa posição

        # AS LINHAS E COLUNAS DO TABULEIRO VÃO DE 0 ATÉ 9
        if linha_atual < 0 or linha_atual >= 10:
            return False # para que nenhuma parte do navio fique fora das linhas

        if coluna_atual < 0 or coluna_atual >= 10:
            return False  # para que nenhuma parte do navio fique fora das colunas

        for nome_navio in frota:  # percorre os tipos de embarcação existentes
            for navio in frota[nome_navio]:  # vai percorrer todos os navios já posicionados
                if posicao in navio:  # vai verificar se essa posição já está ocupada
                    return False  # o novo navio sobreporia outro navio 

    return True  # vai devolver todas as posições que estão dentro do tabuleiro e estão livres



# PARTE 7
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])   # mostra todos os valores da linha do jogador, incluindo seus navios
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])    # mostra apenas os tiros no oponente; navios intactos aparecem como 0
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto   # vai devolver o texto para ser exibido