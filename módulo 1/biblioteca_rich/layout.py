from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from pathlib import Path

console = Console()

def layout(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        
        # Dividindo o texto em "Ingredientes" e "Modo de Preparo"
        partes = texto.split("Modo de Preparo:")
        ingredientes = partes[0].strip()  # O que está antes de "Modo de Preparo"
        modo_preparo = "Modo de Preparo:" + partes[1].strip() if len(partes) > 1 else ""  # O que está depois de "Modo de Preparo"
        
        layout = Layout()
        layout.split_row(
            Layout(Panel(ingredientes, title="Ingredientes")),
            Layout(Panel(modo_preparo, title="Modo de Preparo"))
        )
        console.print(layout)
    
    except FileNotFoundError:
        console.print(f"[red]Erro: O arquivo '{caminho_arquivo}' não foi encontrado![/red]")
    except ValueError:
        console.print("[red]Erro: O arquivo não contém a seção 'Modo de Preparo'.[/red]")

def editar(caminho_arquivo,isArquivo):
    if isArquivo: #se positivo, chame a função anterior
            layout(caminho_arquivo)
    else: # se não, leia e imprima sem editção
          with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
                texto=arquivo.read()
                print(texto)

# Exemplo de uso
editar("personalizador/texto2.txt",True)
editar("personalizador/texto2.txt",False)
