from SOAPpy import SOAPProxy



server = SOAPProxy('http://localhost:8081/')
n_bolas = 10

def main():
    tabuleiro = []
    qtd_bolas = n_bolas
    print("Bem vindo ao Bingo!")
    print("Escolha a opcao:")
    print("1 - Para novo sorteio")
    print("2 - Imprimir tabuleiro")
    print("3 - zerar tabuleiro")
    print("4 - Encerrar bingo")
    terminal = 0
    while terminal != 4:
        if qtd_bolas == 0:
            print("Sorteio terminado.\nReiniciando tabuleiro")
            print(str(server.sorteio(n_bolas, 3)))
            qtd_bolas = n_bolas
        else:
            print("---------------------------")
            terminal = input('Digite sua opcao:\n')
            print(str(server.sorteio(n_bolas, terminal)))
            if terminal == 1:
                qtd_bolas = qtd_bolas - 1
            elif terminal == 3:
                qtd_bolas = n_bolas







if __name__ == "__main__":
    main()