from rich.console import Console
import time
from time import sleep
from rich.progress import track
from pathlib import Path

console = Console()

def progresso(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        for _ in track(range(5), description= "[green] Carregando conteúdo"):
            sleep(1)
        print(f"Completo!")


def editar(caminho_arquivo,isArquivo):
    if isArquivo: #se positivo, chame a função anterior
            progresso(caminho_arquivo)
    else: # se não, leia e imprima sem editção
          with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                texto=arquivo.read()
                print(texto)

# Exemplo de uso
editar("personalizador/texto3.txt",True)
editar("personalizador/texto3.txt",False)


