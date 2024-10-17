from rich.console import Console
from pathlib import Path

console = Console()

def styles(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        console.print(texto, style="magenta")


# Exemplo de uso
def editar(caminho_arquivo,isArquivo):
    if isArquivo: #se positivo, chame a função anterior
            styles(caminho_arquivo)
    else: # se não, leia e imprima sem editção
          with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                texto=arquivo.read()
                print(texto)

# Exemplo de uso
editar("personalizador/texto1.txt",True)
editar("personalizador/texto1.txt",False)

