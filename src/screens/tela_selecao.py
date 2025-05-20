import flet as ft

class TelaSelecaoRegiao(ft.Container):
    def __init__(self, ao_selecionar_callback):
        super().__init__()

        self.ao_selecionar_callback = ao_selecionar_callback

        
        self.gif_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/tela-inicial.gif", # caminho para o arquivo do GIF 
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
            width=1600,# define a largura do GIF 
            height=900, # define a altura do GIF
        )

        regioes = [
            "Kanto", "Johto", "Hoenn", "Sinnoh",
            "Unova", "Kalos", "Alola", "Galar", "Paldea", "National Dex"
        ]

        botoes = [
            ft.ElevatedButton(
                text=regiao,
                on_click=lambda e, r=regiao: self.ao_selecionar_callback(r),
                width=200
            )
            for regiao in regioes
        ]

        self.conteudo_interface = ft.Column(
            controls=[
                ft.Text(
                    "Escolha uma região para o quiz:",
                    size=30,
                    weight="bold",
                    color=ft.Colors.WHITE
                ),
                ft.Row(
                    controls=botoes,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    run_spacing=20
                )
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

        # self.expand = True
        # self.alignment = ft.alignment.center