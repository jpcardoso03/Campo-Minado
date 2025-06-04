from tkinter import Tk
from os import system
from campo_minado import CampoMinado

# Limpa o terminal
try:
    system('cls')
except:
    system('clear')

# Inicia o jogo
if __name__ == "__main__":
    jogo = CampoMinado()
    jogo.configuracoes_iniciais()
    if not jogo.saida:
        jogo.janela.mainloop()