class Linguagem:
    def __init__(self, lingua='Português'):
        """Inicializa os textos conforme o idioma padrão."""
        self.definir_idioma(lingua)

    def definir_idioma(self, lingua):
        """Define os textos de acordo com o idioma escolhido."""
        self.lingua = lingua
        
        if lingua == 'Português':
            self.textoDificuldade = 'Dificuldade'
            self.textoDificuldade2 = 'Clique na dificuldade desejada:'
            self.opcaoDificuldade = ['9x9 (10 bombas)', '16x16 (40 bombas)', '16x30 (99 bombas)']
            self.textoSair = 'SAIR'
            self.textoRecomecar = 'RECOMEÇAR'
            self.marcadorMina = 'BANDEIRA'
            self.informacoesEbotoes = 'Info e botões'
            self.textoVitoria = 'Você ganhou'
            self.textoDerrota = 'Você perdeu'
            self.titulo = 'Campo Minado'
        
        elif lingua == 'English':
            self.textoDificuldade = 'Difficulty'
            self.textoDificuldade2 = 'Click on the desired difficulty:'
            self.opcaoDificuldade = ['9x9 (10 bombs)', '16x16 (40 bombs)', '16x30 (99 bombs)']
            self.textoSair = 'LEAVE'
            self.textoRecomecar = 'RESTART'
            self.marcadorMina = 'FLAG'
            self.informacoesEbotoes = 'Info and buttons'
            self.textoVitoria = 'You won'
            self.textoDerrota = 'You lost'
            self.titulo = 'Minefield'
        
        elif lingua == 'Español':
            self.textoDificuldade = 'Dificultad'
            self.textoDificuldade2 = 'Haga clic en la dificultad deseada:'
            self.opcaoDificuldade = ['9x9 (10 bombas)', '16x16 (40 bombas)', '16x30 (99 bombas)']
            self.textoSair = 'SALIR'
            self.textoRecomecar = 'REINICIAR'
            self.marcadorMina = 'BANDERA'
            self.informacoesEbotoes = 'Información y botones'
            self.textoVitoria = 'Has ganado'
            self.textoDerrota = 'Has perdido'
            self.titulo = 'Campo Minado'