import os

import time

def mostrar_fogos_de_artificio():
    """
    Simula a animação de fogos de artifício no terminal, aparecendo gradativamente.
    """
    fogos = [
        "     🎇     ",
        "    🎇🎇    ",
        "   🎇🎇🎇   ",
        "  🎇🎇🎇🎇  ",
        "🎇🎇🎇🎇🎇🎇"
    ]
    
    # Imprime os fogos de artifício em etapas, com uma pausa entre cada uma
    for estagio in fogos:
        print(estagio)
        time.sleep(0.5)  # Pausa de 0.5 segundos entre cada estágio

    # Adiciona uma animação "explosiva"
    for _ in range(3):
        print("🎆🎇🎈🎉💥💥🎆🎇🎈🎉💥")
        time.sleep(0.5)
        print("\n" * 3)
        time.sleep(0.5)

def limpar_tela():
    """
    Limpa a tela do terminal para dar a impressão de atualização contínua.
    Funciona em Windows, Linux e macOS.
    """
    os.system('clear')

def checar_vitoria(posicao_jogador, posicao_item):
    """
    Verifica se o jogador chegou na posição do item.
    """
    return posicao_jogador == posicao_item
