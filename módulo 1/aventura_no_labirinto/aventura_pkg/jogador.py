def mover_jogador(direcao, posicao_atual, labirinto):
    """
    Move o jogador no labirinto se a direção for válida.
    """
    x, y = posicao_atual
    movimentos = {
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1)
    }
    
    dx, dy = movimentos.get(direcao, (0, 0))
    nova_posicao = x + dx, y + dy
    
    # Verifica se a nova posição está dentro dos limites e não é uma parede
    if 0 <= nova_posicao[0] < len(labirinto) and 0 <= nova_posicao[1] < len(labirinto[0]):
        if labirinto[nova_posicao[0]][nova_posicao[1]] != '🚧':
            return nova_posicao  # Retorna a nova posição se o movimento for válido
    return posicao_atual  # Caso contrário, o jogador não se move
