import flet as ft
import asyncio

class TelaInicial(ft.Container):
    def __init__(self, ao_jogar_callback, ao_leaderboard_callback): # Construtor da classe TelaInicial, recebe a função que será chamada ao clicar em "Jogar"
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
            on_click=self.enviar_nick, # função que será chamada quando o botão jogar for clicado
            width=200, # largura do botão
            height=50 # altura do botão
        )

        self.botao_leaderboard = ft.ElevatedButton( # variável que representa o botão de jogar
            text="Leaderboard", # texto dentro do botão
            on_click=ao_leaderboard_callback, # função que será chamada quando o botão jogar for clicado
            width=200, # largura do botão
            height=50 # altura do botão
        )

        self.input_nick = ft.TextField(
            label="Digite seu nick",
            width=300,
            color="White",
            border_color="White",
            label_style=ft.TextStyle(color="white")
        )

        self.erro = ft.Text(
            "Você precisa inserir um nick antes de jogar!!",
            size=16,
            weight="bold",
            color=ft.Colors.RED,
            opacity=0
        )

        self.content = ft.Stack( # variável que contém todo o conteúdo da tela. ft.Stack permite a sobreposição de elementos na tela
            controls=[
                self.gif_fundo, # coloca o GIF como a camada mais inferior da tela
                ft.Container( # conteiner que centraliza o conteúdo na tela
                    content=ft.Column( # (content) coloca o Column dentro do Container/ (Column) empilha elementos verticalmente
                        controls=[self.botao_jogar, self.botao_leaderboard], # cria o botão jogar na tela
                        alignment=ft.MainAxisAlignment.CENTER, # ajusta o conteúdo no centro verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, # ajusta o conteúdo no centro verticalmente
                        spacing=20, # Espaçamento entre os elementos da coluna
                    ),
                    alignment=ft.alignment.center, # alinha o conteúdo dentro do Container no centro
                    expand=True # faz o container usar todo o espaço disponível
                ),
                ft.Container(
                    ft.ResponsiveRow(
                        controls=[
                            self.input_nick,
                            self.erro
                        ],
                        width=350,
                    ),
                    margin=ft.margin.only(top=50, left=1100)
                )
            ],
            width=1600, # define a largura do conteudo na tela
            height=900 # define a altura do conteudo na tela
        )

    async def enviar_nick(self, e):
        nick = self.input_nick.value.strip()
        if nick:
            self.ao_jogar_callback(nick)
        else:
            self.erro.opacity = 1
            self.erro.update()
            await asyncio.sleep(2)
            self.erro.opacity = 0
            self.erro.update()