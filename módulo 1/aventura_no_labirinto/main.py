import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto, atualizar_labirinto
from aventura_pkg.jogador import mover_jogador
from aventura_pkg.utils import checar_vitoria, mostrar_fogos_de_artificio


def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument('--name', required=True, help="Nome do jogador")
    parser.add_argument('--color', choices=['vermelho', 'azul', 'verde'], default='verde', help="Escolha a cor principal do jogo")
    parser.add_argument('--dificuldade', type=int, choices=[1, 2, 3], default=1, help="Escolha a dificuldade (1=fácil, 2=médio, 3=difícil)")
    parser.add_argument('--disable-sound', action='store_true', help="Desliga a música do jogo")
    # Removido o argumento --help, pois já existe um padrão

    args = parser.parse_args()

    # Configurações do jogo com base nos argumentos
    nome_jogador = args.name
    dificuldade = args.dificuldade
    cor_jogo = args.color
    som_ativado = not args.disable_sound

    print(f"Bem-vindo(a), {nome_jogador}! Você escolheu a cor {cor_jogo} e a dificuldade {dificuldade}.")
    if not som_ativado:
        print("Som está desativado.")
    
    # Inicializa o labirinto e as posições
    tamanho = 9
    labirinto = criar_labirinto(tamanho)
    posicao_jogador = (0, 0)
    posicao_item = (tamanho - 1, tamanho - 1)

    # Imprime o labirinto inicial
    imprimir_labirinto(labirinto)
    
    # Loop principal do jogo
    while True:
        direcao = input("Digite a direção (w, s, a, d): ").strip().lower()
        
        # Move o jogador
        nova_posicao = mover_jogador(direcao, posicao_jogador, labirinto)
        
        # Atualiza o labirinto e imprime novamente
        atualizar_labirinto(labirinto, posicao_jogador, nova_posicao)
        imprimir_labirinto(labirinto)
        
        # Atualiza a posição do jogador
        posicao_jogador = nova_posicao
        
        # Verifica se o jogador venceu
        if checar_vitoria(posicao_jogador, posicao_item):
            print("Parabéns! Você encontrou o item!")
            mostrar_fogos_de_artificio()
            break

if __name__ == "__main__":
    main()
