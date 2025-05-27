import flet as ft

class TelaSelecaoRegiao(ft.Container):
    def __init__(self, ao_selecionar_callback):# Construtor da classe TelaInicial, recebe a função que será chamada ao clicar em "Jogar"
        super().__init__() # esse comando é comum em classes que usam outras classes. Nesse caso o super() chama a classe mãe UserControl e permite que seja inicializado corretamente


        self.ao_selecionar_callback = ao_selecionar_callback # cria a função que será chamada quando o botão jogar for clicado

        
        self.gif_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/tela-inicial.gif", # caminho para o arquivo do GIF 
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
            width=1600,# define a largura do GIF 
            height=900, # define a altura do GIF
        )

        self.regioes = { # cria uma lista com o nome de todas as regioes e a national dex
            "Kanto": "1",
            "Johto": "2",
            "Hoenn": "3",
            "Sinnoh": "4",
            "Unova": "5",
            "Kalos": "6",
            "Alola": "7",
            "Galar": "8",
            "Paldea": "9",
            "National Dex": "national"
        }

        botoes = [ # cria um botão com o nome de cada uma das regiões e aplica a função ao_selecionar_callback
            ft.ElevatedButton(
                text=nome_visivel,
                on_click=lambda e, valor_api=nome_api: self.ao_selecionar_callback(valor_api),
                width=200
            )
            for nome_visivel, nome_api in self.regioes.items()
        ]

        self.conteudo_interface = ft.Column( # variável que contém o titulo da pagina e os botões de cada região
            controls=[
                ft.Container(
                    content=ft.Text( # cria o texto que será utilizado como titulo
                        "Escolha uma região para o quiz:",
                        size=30,
                        weight="bold",
                        color=ft.Colors.WHITE,
                    ),
                margin=ft.margin.only(top=-200)
                ),
                ft.Container(
                    ft.Row( # cria uma linha que posiciona todos os botões em sequencia no meio da tela
                        controls=botoes,
                        wrap=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        run_spacing=20,
                    ),
                    width=1600
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER, # posiciona a variavel conteudo_interface no centro verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, # posiciona a variavel conteudo_interface no centro horizontalmente
            spacing=30 # coloca um espaçamento para as outras variaveis
        )

        self.content = ft.Stack( # coloca os elementos na tela por meio do comando .content original do flet
            controls=[
                self.gif_fundo, # coloca o gif de fundo como camada mais inferior da tela
                self.conteudo_interface # coloca a variavel conteudo_interface que contem os titulos e todos os botões
            ],
            width=1600, # define a largura do conteudo na tela
            height=900 # define a altura do conteudo na tela
        )