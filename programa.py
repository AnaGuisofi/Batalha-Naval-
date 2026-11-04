from funcoes import (posicao_valida, preenche_frota, posiciona_frota, monta_tabuleiros, faz_jogada, afundados)

# cada tipo de navio tem uma lista no formato [tamanho, quantidade]
embarcacoes = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
}
frota ={}  # guarda os navios de acordo com o posicionamento escolhido pelo jogador

for nome_navio in embarcacoes:  # vai seguir a ordem das embarcações
    tamanho = embarcacoes[nome_navio][0]  # obtém o tamanho desse tipo
    quantidade = embarcacoes[nome_navio][1]  # obtém quantos devem ser colocados

    posicionados = 0  # conta quantos navios desse tipo foram colocados com sucesso

    while posicionados < quantidade:  # até posicionar todos desse tipo
        print(
            f"Insira as informações referentes ao navio {nome_navio} "
            f"que possui tamanho {tamanho}"
        )
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if tamanho > 1:  # apenas navios maiores que 1
            escolha = int(input("[1] Vertical [2] Horizontal >"))

            if escolha == 1:
                orientacao = "vertical"  # converte 1 para o texto usado nas funções            
            else:
                orientacao = "horizontal"  # converte 2 para horizontal

        else:
            orientacao = "horizontal"  # qualquer orientação ocupa a mesma casa

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)  # vai guardar o navio somente quando todas as posições são válidas
            posicionados += 1  # após um sucesso, avança para o próximo navio

        else: 
            print("Esta posição não está válida!")

# FROTA FIXA DO OPONENTE:

frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [ 
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios = 0  # quantos navios inimigos precisam ser afundados

for nome_navio in frota_oponente:
    total_navios += len(frota_oponente[nome_navio])  # conta apenas os navios, não as casas que eles ocupam

# LOOP PRINCIPAL DOS ATAQUES:
jogando = True  # vai manter a partida em andamento até a vitória

while jogando: 
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))  # vai mostrar o tabuleiro do jogador e o do oponente com os navios escondidos

    jogada_valida = False  # vai reiniciar a validação a cada rodada

    while jogada_valida == False:
        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if tabuleiro_oponente[linha][coluna] in ["X", "-"]:
            print(
                f"A posição linha {linha} e coluna {coluna} "
                "já foi informada anteriormente!"
            )  # jogada_valida continua False -> volta a perguntar linha e coluna

        else:
            jogada_valida = True  # coordenada liberada e ainda

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)  # registra o tiro -> 1/X ou 0/-

    afundou = afundados(frota_oponente, tabuleiro_oponente)
    if afundou == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False  # encerra sem pedir outro ataque