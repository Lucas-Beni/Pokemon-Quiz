import flet as ft

def main(page: ft.Page):
    page.title = "PokeQuizz - Tela Inicial"
    page.padding = 0
    page.bgcolor = ft.Colors.BLACK

    # Força o GIF a ter tamanho da página
    gif_fundo = ft.Image(
        src="src/assets/tela-inicial.gif",
        fit=ft.ImageFit.COVER,
        width=page.width,
        height=page.height
    )

    botao_jogar = ft.ElevatedButton(
        text="Jogar",
        on_click=lambda e: print("Iniciar jogo...")
    )

    conteudo = ft.Stack(
        controls=[
            gif_fundo,
            ft.Container(
                content=ft.Column(
                    controls=[botao_jogar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ],
        expand=True
    )

    page.add(conteudo)


# Para rodar em janela de app nativo (desktop ou mobile)
ft.app(target=main,view=ft.WEB_BROWSER)