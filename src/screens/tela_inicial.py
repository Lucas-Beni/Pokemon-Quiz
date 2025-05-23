import flet as ft

class TelaInicial(ft.Container):
    def __init__(self, ao_jogar_callback): # Construtor da classe TelaInicial, recebe a função que será chamada ao clicar em "Jogar"
        super().__init__() # esse comando é comum em classes que usam outras classes. Nesse caso o super() chama a classe mãe UserControl e permite que seja inicializado corretamente

        self.ao_jogar_callback = ao_jogar_callback # cria a função que será chamada quando o botão jogar for clicado

        self.gif_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/tela-inicial.gif", # caminho para o arquivo do GIF 
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
            width=1600,# define a largura do GIF 
            height=900, # define a altura do GIF
        )

        self.botao_jogar = ft.ElevatedButton( # variável que representa o botão de jogar
            text="Jogar", # texto dentro do botão
            on_click=self.ao_jogar_callback, # função que será chamada quando o botão jogar for clicado
            width=200, # largura do botão
            height=50 # altura do botão
        )

        self.content = ft.Stack( # variável que contém todo o conteúdo da tela. ft.Stack permite a sobreposição de elementos na tela
            controls=[
                self.gif_fundo, # coloca o GIF como a camada mais inferior da tela
                ft.Container( # conteiner que centraliza o conteúdo na tela
                    content=ft.Column( # (content) coloca o Column dentro do Container/ (Column) empilha elementos verticalmente
                        controls=[self.botao_jogar], # cria o botão jogar na tela
                        alignment=ft.MainAxisAlignment.CENTER, # ajusta o conteúdo no centro verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, # ajusta o conteúdo no centro verticalmente
                        spacing=20, # Espaçamento entre os elementos da coluna
                    ),
                    alignment=ft.alignment.center, # alinha o conteúdo dentro do Container no centro
                    expand=True # faz o container usar todo o espaço disponível
                )
            ],
            width=1600, # define a largura do conteudo na tela
            height=900 # define a altura do conteudo na tela
        )
