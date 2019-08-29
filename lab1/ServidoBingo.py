from SOAPpy import SOAPServer
import random

tabuleiro = []

def sorteio(n_bolas, terminal):

        if terminal == 1:
                bola = random.randrange(1, n_bolas+1, 1)
                while bola in tabuleiro:
                        bola = random.randrange(1, n_bolas, 1)

                tabuleiro.append(bola)
                return "bola "+ str(bola) + " inserida no tabuleiro"
        if terminal == 2:
                texto = "Bolas sorteadas:"
                for i in tabuleiro:
                        texto = texto + str(i) + ' '

                return texto
        if terminal == 3:
                for i in tabuleiro:
                        tabuleiro.pop()
                tabuleiro.pop()
                return "Tabuleiro reiniciado"



server = SOAPServer(('localhost',8081))
server.registerFunction(sorteio)
server.serve_forever()