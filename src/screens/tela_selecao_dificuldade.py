import flet as ft

class TelaDificuldade(ft.Container):
    def __init__(self, ao_dificuldade_callback): # Construtor da classe TelaInicial, recebe a função que será chamada ao clicar em "Jogar"
        super().__init__() # esse comando é comum em classes que usam outras classes. Nesse caso o super() chama a classe mãe UserControl e permite que seja inicializado corretamente

        self.ao_dificuldade_callback = ao_dificuldade_callback # cria a função que será chamada quando o botão jogar for clicado

        self.descricao_texto = ft.Text(
            value="",
            size=20,
            color=ft.Colors.WHITE,
            italic=True
        )

        self.gif_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/tela-inicial.gif", # caminho para o arquivo do GIF 
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
            width=1600,# define a largura do GIF 
            height=900, # define a altura do GIF
        )

        def ao_hover(e, mensagem):
            self.descricao_texto.value = mensagem if e.data == "true" else ""
            self.update()

        btn_normal = ft.ElevatedButton(
            text="Normal",
            on_click=lambda e: self.ao_dificuldade_callback("1"),
            width=200,
            on_hover=lambda e: ao_hover(e, "Modo Normal: Quiz com silhuetas dos pokémon.")
        )

        btn_dificil = ft.ElevatedButton(
            text="Difícil",
            on_click=lambda e: self.ao_dificuldade_callback("2"),
            width=200,
            on_hover=lambda e: ao_hover(e, "Modo Difícil: Quiz sem silhuetas.")
        )

        self.conteudo_interface = ft.Column(
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
                ft.Row(
                    controls=[btn_normal, btn_dificil],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                self.descricao_texto  # texto dinâmico
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30
        )

        self.content = ft.Stack(
            controls=[
                self.gif_fundo,
                self.conteudo_interface
            ],
            width=1600,
            height=900
        )