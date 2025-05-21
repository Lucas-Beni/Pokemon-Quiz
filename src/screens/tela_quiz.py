import flet as ft
import requests

class TelaQuiz(ft.Container):
    def __init__(self, regiao: str):
        super().__init__()
        self.regiao = regiao
        url = f"https://pokeapi.co/api/v2/pokedex/{regiao.lower()}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            self.content = ft.Column(
                controls=[
                    ft.Text(f"Quiz da região: {regiao}", size=30, color="white"),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        else:  
            self.content = ft.Text(value="Erro ao carregar região", color="red")
