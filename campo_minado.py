from tkinter import Tk, Button, Label, PhotoImage, DISABLED
from random import randint
from lingua import Linguagem
from sprite import Sprites
from pyautogui import confirm 



class CampoMinado:
    def __init__(self):
        self.janela = None
        self.totalBombas = 0
        self.tabuleiro = []
        self.tamanhoBotão = 0
        self.saida = False
        self.aN = 0
        self.lN = 0
        self.totalBandeiras = 0
        self.largura = 0
        self.altura = 0
        self.fim = False
        self.lang = ''
        self.janela2 = None
        self.bandeiraAD = False
        self.campoBotoes = []
        self.txtBombas = None
        self.txtTempo = None
        self.tempoIniciado = False
        self.tempoTotal = 0
        self.tempoID = None
        self.campoBombas = []
        self.tentativa = 0
        self.bnd = 0
        self.bmb = 0

        self.linguagem = Linguagem()
        self.sprites = Sprites()

    def configuracoes_iniciais(self):
        self.saida = False
        self.fim = False
        while True:
            if self.lang == '':
                respL = confirm(title='Language', text='Choose your language:', buttons=['Português', 'English', 'Español'])
                if respL is None:
                    self.saida = True
                    break
                else:
                    self.lang = respL
                    self.linguagem.definir_idioma(respL)

            respD = confirm(title=self.linguagem.textoDificuldade, text=self.linguagem.textoDificuldade2, buttons=self.linguagem.opcaoDificuldade)
            if respD is None:
                self.saida = True
                break
            # tamanho do tabuleiro
            if respD == self.linguagem.opcaoDificuldade[0]:
                #                 Y, X
                self.tabuleiro = [9, 9]
                self.totalBombas = 10
                self.aN = 175
                self.lN = 157
            elif respD == self.linguagem.opcaoDificuldade[1]:
                self.tabuleiro = [16, 16]
                self.totalBombas = 40
                self.aN = 295
                self.lN = 280
            else:
                self.tabuleiro = [16, 30]
                self.totalBombas = 99
                self.aN = 295
                self.lN = 525
            self.totalBandeiras = self.totalBombas
            # abrir a janela
            self.janela = Tk()
            self.janela.resizable(False, False)
            try:
                icone = PhotoImage(file='imagens/icone campo minado.png')
            except:
                icone = PhotoImage(file='campo_minado/imagens/icone campo minado.png')
            self.janela.iconphoto(False, icone)
            # pegando altura e largura
            self.altura, self.largura = int(self.janela.winfo_screenheight()/2) - self.aN, int(self.janela.winfo_screenwidth()/2) - self.lN
            # criar as imagens
            self.sprites.imagensCriar()
            # titulo da janela
            self.janela.title(self.linguagem.titulo)
            # tamanho do botao
            self.tamanhoBotão = 35
            # x e y da janela
            y, x = self.tabuleiro[0] * self.tamanhoBotão, self.tabuleiro[1] * self.tamanhoBotão
            # tamanho da tela
            self.janela.geometry(f'{x}x{y}+{self.largura}+{self.altura}')
            self.criarSegundaJanela()

            if not self.saida:
                self.criarBotoes()  # Adicione esta linha
            break

    def criarSegundaJanela(self):
        self.janela2 = Tk()
        self.janela2.resizable(False, False)
        self.janela2.title(self.linguagem.informacoesEbotoes)
        self.janela2.geometry(f'360x70+{self.largura+self.lN-180}+{self.altura-75}')
        self.janela2.attributes('-topmost', True)
        self.bandeiraAD = False

        def destruirJanela():
            if self.tempoID:
                self.janela.after_cancel(self.tempoID)  # Cancela o cronômetro
            try:
                self.janela2.destroy()
                self.janela.destroy()
            except:
                pass

        def recomecar():
            if self.tempoID:
                self.janela.after_cancel(self.tempoID)  # Cancela a execução pendente
                self.tempoID = None  # Reseta a variável

            self.tempoIniciado = False  # Permite que o cronômetro reinicie corretamente
            self.tempoTotal = 0  # Zera o tempo ao recomeçar o jogo

            destruirJanela()
            self.configuracoes_iniciais()

            if not self.saida:
                self.criarBotoes()

        def bandeira(botao):
            if not self.fim:
                if botao['text'] == f'{self.linguagem.marcadorMina} / ON':
                    botao['text'] = f'{self.linguagem.marcadorMina} / OFF'
                    self.bandeiraAD = False
                else:
                    botao['text'] = f'{self.linguagem.marcadorMina} / ON'
                    self.bandeiraAD = True

        def resetarBandeiras():
            try:
                if not self.fim and self.janela.state():
                    for x in range(self.tabuleiro[0]):
                        for y in range(self.tabuleiro[1]):
                            if self.campoBotoes[x][y]['image'] == str(self.sprites.imagemBandeira):
                                self.campoBotoes[x][y]['image'] = self.sprites.imagemBotaoNada
                    self.totalBandeiras = self.totalBombas
                    self.txtBombas['text'] = f'{self.totalBandeiras}'
            except:
                pass

        txtSair = Button(self.janela2, text=self.linguagem.textoSair, fg='black', bg='red3', font='Impact', activebackground='red4', command=destruirJanela)
        txtSair.place(x=0, y=0, height=35, width=120)
        txtRecomecar = Button(self.janela2, text=self.linguagem.textoRecomecar, fg='black', bg='green3', font='Impact', activebackground='green', command=recomecar)
        txtRecomecar.place(x=120, y=0, height=35, width=120)
        txtBandeira = Button(self.janela2, text=f'{self.linguagem.marcadorMina} / OFF', fg='black', bg='red2', font='Impact', activebackground='red3')
        txtBandeira['command'] = lambda botao = txtBandeira: bandeira(botao)
        txtBandeira.place(x=240, y=0, height=35, width=120)
        txtDesfazerBandeiras = Button(self.janela2, text=f'{self.linguagem.marcadorMina}S RESET', fg='black', bg='blue', font='Impact', activebackground='blue3', command=resetarBandeiras)
        txtDesfazerBandeiras.place(x=240, y=35, height=35, width=120)
        txtBandeira.place(x=240, y=0, height=35, width=120)
        self.txtBombas = Label(self.janela2, text=f'{self.totalBandeiras}', font=('Impact', 30), fg='red', bg='black')
        self.txtBombas.place(x=120, y=35, height=35, width=120)
        self.txtTempo = Label(self.janela2, text='0s', font=('Impact', 30), fg='white', bg='black')
        self.txtTempo.place(x=240, y=35, height=35, width=120)
        fundoPreto = Label(self.janela2, bg='black')
        fundoPreto.place(x=0, y=35, height=35, width=120)

    def atualizarTempo(self):
        if self.tempoIniciado and self.janela:  # Verifica se a janela ainda existe
            self.tempoTotal += 1
            self.txtTempo.config(text=f'{self.tempoTotal}s')
            self.tempoID = self.janela.after(1000, self.atualizarTempo)

    def verificarNumerosCampoBombas(self, x, y):
        for a in range(9):
            try:
                if self.campoBombas[x][y][0] == a:
                    self.campoBombas[x][y][0] += 1
                    self.campoBombas[x][y][1] = self.sprites.imagensNumeros[a]
                    break
            except:
                pass

    def criarBombas(self, l, c):
        z = 1
        while z <= self.totalBombas:
            n1 = randint(0, self.tabuleiro[0]-1)
            n2 = randint(0, self.tabuleiro[1]-1)
            
            if self.campoBombas[n1][n2][1] == '💣' or (n1, n2) == (l, c):
                continue
            self.campoBombas[n1][n2][1] = '💣'
            self.campoBombas[n1][n2][0] = -1
            for a in range(n1-1, n1+2):
                for b in range(n2-1, n2+2):
                    if a >= 0 and b >= 0:
                        self.verificarNumerosCampoBombas(a, b)
            z += 1

    def criarBotoes(self):
        # Inicializa o campo de bombas e botões
        self.campoBombas = [[[0, ''] for x in range(self.tabuleiro[1])] for x in range(self.tabuleiro[0])]
        self.campoBotoes = [[] for x in range(self.tabuleiro[0])]
        self.tentativa = 0

        # Alternar bandeiras com clique direito
        def alternarBandeira(event, linha, coluna):
            if self.fim:
                return  # Não permite interações após o jogo terminar

            botao = self.campoBotoes[linha][coluna]
            if botao['image'] == str(self.sprites.imagemBandeira):  # Se o botão já tem uma bandeira
                botao.config(image=self.sprites.imagemBotaoNada)  # Remove a bandeira
                self.totalBandeiras += 1
            elif self.totalBandeiras > 0:  # Adiciona bandeira apenas se houver disponível
                botao.config(image=self.sprites.imagemBandeira)
                self.totalBandeiras -= 1

            # Atualiza o contador de bandeiras restantes
            self.txtBombas['text'] = f'{self.totalBandeiras}'

        # Criando os botões do tabuleiro
        for l in range(self.tabuleiro[0]):
            for c in range(self.tabuleiro[1]):
                posX = c * self.tamanhoBotão
                posY = l * self.tamanhoBotão
                b = Button(self.janela, activebackground='gray75', bg='gray90', image=self.sprites.imagemBotaoNada)

                # Clique esquerdo: ação principal
                b['command'] = lambda linha=l, coluna=c: self.clicar(linha, coluna)

                # Clique direito: alternar bandeira
                b.bind('<Button-3>', lambda event, linha=l, coluna=c: alternarBandeira(event, linha, coluna))

                # Posiciona o botão no tabuleiro
                b.place(x=posX, y=posY, height=self.tamanhoBotão, width=self.tamanhoBotão)
                self.campoBotoes[l].append(b)

    def mostrarGP(self, gp, linha, coluna):
        for x in range(self.tabuleiro[0]):
            for y in range(self.tabuleiro[1]):
                self.campoBotoes[x][y]['state'] = DISABLED
                if self.campoBombas[x][y][1] == '💣' and gp == 'p' and self.campoBotoes[x][y]['image'] != str(self.sprites.imagemBandeira):
                    if (x, y) == (linha, coluna):
                        self.campoBotoes[x][y]['bg'] = 'red'
                        j = Label(self.janela, image=self.sprites.imagemBombaPerda, bg='red')
                    else:
                        self.campoBotoes[x][y]['bg'] = 'gray75'
                        j = Label(self.janela, image=self.sprites.imagemBomba, bg='gray75')
                else:
                    if self.campoBotoes[x][y]['image'] == str(self.sprites.imagemBotaoNada):
                        j = Label(self.janela, image=self.sprites.imagemBotaoNada, bg='gray75')
                    elif self.campoBotoes[x][y]['image'] == '':
                        continue
                    elif self.campoBotoes[x][y]['image'] == str(self.sprites.imagemBandeira) and self.campoBombas[x][y][1] != '💣':
                        j = Label(self.janela, image=self.sprites.imagemBombaErrada, bg='gray75')
                    elif self.campoBotoes[x][y]['image'] == str(self.sprites.imagemBandeira):
                        j = Label(self.janela, image=self.sprites.imagemBandeira, bg='gray75')
                    else:
                        j = Label(self.janela, image=self.campoBombas[x][y][1], bg='gray75')
                j.place(x=y*35, y=x*35, height=33, width=33)
        textoGP = [self.linguagem.textoVitoria, 'green2'] if gp == 'g' else [self.linguagem.textoDerrota, 'red']
        j = Label(self.janela, text=textoGP[0], font=('Impact', 24), fg=textoGP[1], bg='gray75')
        if self.linguagem.textoVitoria == 'You won!':
            j.place(x=self.lN-57, y=self.aN-39)
        else:
            j.place(x=self.lN-90, y=self.aN-39)
    def verificarZeros(self):
        for az in range(10):
            for x in range(self.tabuleiro[0]):
                for y in range(self.tabuleiro[1]):
                    if self.campoBotoes[x][y]['image'] == '':
                        for a in range(x-1, x+2):
                            for b in range(y-1, y+2):
                                if a >= 0 and b >= 0:
                                    try:
                                        if self.campoBotoes[a][b]['image'] == str(self.sprites.imagemBandeira):
                                            continue
                                        self.campoBotoes[a][b].config(image=self.campoBombas[a][b][1], bg='gray75')
                                        if self.campoBotoes[a][b]['image'] == '':
                                            self.campoBotoes[a][b]['state'] = DISABLED
                                    except:
                                        pass

    def verificarEmVolta(self, n1, n2):
        self.bnd = 0
        self.bmb = 0
        for x in range(n1-1, n1+2):
            for y in range(n2-1, n2+2):
                if x >= 0 and y >= 0:
                    self.trysVerificarEmVolta(x, y)

        if self.bnd == self.campoBombas[n1][n2][0]:
            if self.bmb >= 1:
                return False
            else:
                for x in range(n1-1, n1+2):
                    for y in range(n2-1, n2+2):
                        if x >= 0 and y >= 0:
                            try:
                                if self.campoBotoes[x][y]['image'] == str(self.sprites.imagemBotaoNada):
                                    self.campoBotoes[x][y].config(image=self.campoBombas[x][y][1], bg='gray75')
                            except:
                                pass
                self.verificarZeros()

        return True

    def trysVerificarEmVolta(self, x, y):
        try:
            if self.campoBotoes[x][y]['image'] == str(self.sprites.imagemBandeira):
                self.bnd += 1
            elif self.campoBombas[x][y][1] == '💣':
                self.bmb += 1
        except:
            pass

    def verificarGanho(self):
        #Verifica se o jogador ganhou o jogo.
        b = 0
        for x in self.campoBotoes:
            for y in x:
                if y['image'] == str(self.sprites.imagemBotaoNada) or y['image'] == str(self.sprites.imagemBandeira):
                    b += 1
        return b

    def clicar(self, linha, coluna):
        if self.fim:
            return  # Se o jogo acabou, ignora cliques

        # Se for a primeira jogada, cria as bombas e inicia o cronômetro
        if self.tentativa == 0:
            self.criarBombas(linha, coluna)
            self.tentativa = 1
            if not self.tempoIniciado:  # Verifica se o cronômetro ainda não foi iniciado
                self.tempoIniciado = True
                self.atualizarTempo()  # Inicia o cronômetro

        botao_atual = self.campoBotoes[linha][coluna]
        celula_atual = self.campoBombas[linha][coluna]

        # Se estiver no modo bandeira, alterna a marcação
        if self.bandeiraAD:
            if botao_atual['image'] == str(self.sprites.imagemBandeira):
                botao_atual.config(image=self.sprites.imagemBotaoNada)
                self.totalBandeiras += 1
            elif self.totalBandeiras > 0:
                botao_atual.config(image=self.sprites.imagemBandeira)
                self.totalBandeiras -= 1
            self.txtBombas['text'] = f'{self.totalBandeiras}'
            return

        # Se clicar numa bomba e não for uma bandeira, perde o jogo
        if celula_atual[1] == '💣' and botao_atual['image'] != str(self.sprites.imagemBandeira):
            self.tempoIniciado = False  # Para o cronômetro ao perder
            self.mostrarGP('p', linha, coluna)
            self.fim = True
            return

        # Se clicar em uma célula vazia, abre as células adjacentes
        if celula_atual[0] == 0:
            botao_atual.config(image='', bg='gray75', state=DISABLED)
            self.verificarZeros()
        else:
            botao_atual.config(image=celula_atual[1], bg='gray75')

        # Se a jogada revelou números e há um erro na contagem de bombas, perde o jogo
        if not self.verificarEmVolta(linha, coluna):
            self.tempoIniciado = False  # Para o cronômetro ao perder
            self.mostrarGP('p', linha, coluna)
            self.fim = True

        # Se todas as células sem bomba foram abertas, ganha o jogo
        if self.verificarGanho() == self.totalBombas:
            self.tempoIniciado = False  # Para o cronômetro ao ganhar
            self.mostrarGP('g', linha, coluna)
            self.fim = True

        # Atualiza a contagem de bandeiras restantes
        self.txtBombas['text'] = f'{self.totalBandeiras}'