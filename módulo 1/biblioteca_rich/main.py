import argparse
import layout
import panel
import progresso
import styles

# Função principal para decidir o que exibir
def imprimir_conteudo(texto_ou_arquivo, is_arquivo, modulo, funcao):
    if is_arquivo:
        with open(texto_ou_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
    else:
        conteudo = texto_ou_arquivo

    # Chamando a função correta do módulo selecionado
    if modulo == "layout":
        if funcao == "exibir":
            layout.exibir(conteudo)
    elif modulo == "panel":
        if funcao == "exibir":
            panel.exibir(conteudo)
    elif modulo == "progresso":
        if funcao == "mostrar":
            progresso.mostrar()
    elif modulo == "styles":
        if funcao == "aplicar":
            styles.aplicar(conteudo)

# Lista de módulos e funções disponíveis para ajuda
MODULOS_DISPONIVEIS = ['layout', 'panel', 'progresso', 'styles']
FUNCOES_DISPONIVEIS = {
    'layout': ['exibir'],
    'panel': ['exibir'],
    'progresso': ['mostrar'],
    'styles': ['aplicar']
}

# Função para criar a interface de linha de comando
def main():
    parser = argparse.ArgumentParser(description="Imprimir texto formatado ou conteúdo de arquivo com módulos específicos.")

    # Argumento obrigatório (texto ou caminho para arquivo)
    parser.add_argument(
        'input',
        type=str,
        help="Texto ou caminho para o arquivo que deseja imprimir formatado"
    )

    # Opção -a / --arquivo: indica se o argumento é um caminho para arquivo
    parser.add_argument('-a', '--arquivo',action='store_true',help="Indica que o argumento é um caminho para um arquivo")

    # Opção -m / --modulo: escolhe o módulo
    parser.add_argument('-m', '--modulo',choices=MODULOS_DISPONIVEIS,required=True,help=f"Escolhe o módulo para acessar. Disponíveis: {', '.join(MODULOS_DISPONIVEIS)}")

    # Opção -f / --funcao: escolhe a função do módulo
    parser.add_argument('-f', '--funcao',required=True,help="Escolhe a função do módulo. Consulte as opções disponíveis para o módulo escolhido.")

    # Parseia os argumentos
    args = parser.parse_args()

    # Valida se a função existe para o módulo escolhido
    if args.funcao not in FUNCOES_DISPONIVEIS[args.modulo]:
        parser.error(f"A função '{args.funcao}' não está disponível no módulo '{args.modulo}'. Funções disponíveis: {', '.join(FUNCOES_DISPONIVEIS[args.modulo])}")

    # Chama a função de exibição com os argumentos
    imprimir_conteudo(args.input, args.arquivo, args.modulo, args.funcao)

# Executa a função principal quando o script é rodado
if __name__ == '__main__':
    main()

#exemplo de uso:
#python personalizador/main.py "caminho/para/arquivo.txt" -a -m panel -f exibir
#python main.py "Texto estilizado" -m styles -f aplicar
#ou
#python main.py "texto" -m progresso -f mostrar
