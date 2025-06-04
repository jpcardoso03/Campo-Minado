from tkinter import PhotoImage

class Sprites:
    def __init__(self):
        self.imagemBomba = None
        self.imagemBombaErrada = None
        self.imagemBotaoNada = None
        self.imagemBombaPerda = None
        self.imagemBandeira = None
        self.imagensNumeros = None

    def imagensCriar(self):
        """Carrega as imagens do jogo."""
        try:
            self.imagemBomba = PhotoImage(file='imagens/bomba.png')
        except:
            self.imagemBomba = PhotoImage(file='campo_minado/imagens/bomba.png')

        try:
            self.imagemBombaErrada = PhotoImage(file='imagens/bomba_errada.png')
        except:
            self.imagemBombaErrada = PhotoImage(file='campo_minado/imagens/bomba_errada.png')

        try:
            self.imagemBombaPerda = PhotoImage(file='imagens/bomba_perda.png')
        except:
            self.imagemBombaPerda = PhotoImage(file='campo_minado/imagens/bomba_perda.png')

        try:
            self.imagemBotaoNada = PhotoImage(file='imagens/campo_vazio.png')
        except:
            self.imagemBotaoNada = PhotoImage(file='campo_minado/imagens/campo_vazio.png')

        try:
            self.imagemBandeira = PhotoImage(file='imagens/bandeira.png')
        except:
            self.imagemBandeira = PhotoImage(file='campo_minado/imagens/bandeira.png')

        # Carregando imagens dos números
        self.imagensNumeros = []
        for i in range(1, 9):
            try:
                imagem = PhotoImage(file=f'imagens/numero{i}.png')
            except:
                imagem = PhotoImage(file=f'campo_minado/imagens/numero{i}.png')
            self.imagensNumeros.append(imagem)