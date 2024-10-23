import random

# Direções de movimento: Cima, Baixo, Esquerda, Direita
DIRECOES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def criar_labirinto(tamanho=9):
    """
    Cria um labirinto de tamanho N x N com paredes e um caminho garantido do jogador até o item.
    """
    labirinto = [['🚧' for _ in range(tamanho)] for _ in range(tamanho)]
    
    def criar_caminho(x, y):
        labirinto[x][y] = '  '  # Marca a célula atual como parte do caminho
        
        direcoes = DIRECOES[:]
        random.shuffle(direcoes)
        
        for dx, dy in direcoes:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < tamanho and 0 <= ny < tamanho and labirinto[nx][ny] == '🚧':
                labirinto[x + dx][y + dy] = '  '
                criar_caminho(nx, ny)

    criar_caminho(0, 0)

    # Posiciona o jogador e o item
    labirinto[0][0] = '🤖'
    labirinto[tamanho-1][tamanho-1] = '👑'

    return labirinto

def imprimir_labirinto(labirinto):
    """
    Imprime o labirinto no terminal.
    """
    for linha in labirinto:
        print(' '.join(linha))

def atualizar_labirinto(labirinto, posicao_antiga, posicao_nova):
    """
    Atualiza a posição do jogador no labirinto.
    """
    x_antigo, y_antigo = posicao_antiga
    x_novo, y_novo = posicao_nova
    
    # Atualiza a posição do jogador
    labirinto[x_antigo][y_antigo] = '  '
    labirinto[x_novo][y_novo] = '🤖'

from aventura_pkg.utils import limpar_tela

def imprimir_labirinto(labirinto):
    """
    Limpa o terminal e imprime o labirinto no terminal.
    """
    limpar_tela()  # Limpa o terminal antes de reimprimir
    for linha in labirinto:
        print(' '.join(linha))
