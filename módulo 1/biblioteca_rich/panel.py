from rich.console import Console
from rich.panel import Panel
from pathlib import Path

console = Console() # imitando biblioteca rich

def panel(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: #abir arquivo incluindo codificação com "ç" e "´"
            texto = arquivo.read() #lendo arquivo
        console.print(Panel.fit(texto, title=caminho_arquivo)) #imprimindo em formato painel

def editar(caminho_arquivo,isArquivo):
    if isArquivo: #se positivo, chame a função anterior
            panel("personalizador/texto2.txt")
    else: # se não, leia e imprima sem editção
          with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                texto=arquivo.read()
                print(texto)

# Exemplo de uso
editar("personalizador/texto1.txt",True)
editar("personalizador/texto1.txt",False)

