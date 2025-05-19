import flet as ft

class TelaSelecaoRegiao(ft.UserControl):
    def __init__(self, ao_selecionar_callback):
        super().__init__()
        self.ao_selecionar_callback = ao_selecionar_callback

    def build(self):
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

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Escolha uma região para o quiz:", size=30, weight="bold", color=ft.colors.WHITE),
                    ft.Row(
                        controls=botoes,
                        wrap=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        run_spacing=20,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30
            ),
            expand=True,
            alignment=ft.alignment.center
        )
