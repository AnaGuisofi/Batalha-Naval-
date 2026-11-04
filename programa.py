from funcoes import posicao_valida, preenche_frota

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
print(frota)  # exibe a frota completa e encerra o programa