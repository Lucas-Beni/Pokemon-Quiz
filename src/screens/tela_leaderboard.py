# tela_leaderboard.py
import flet as ft
import sqlite3

class TelaLeaderboard(ft.Container):
    def __init__(self, regiao, voltar_callback):
        super().__init__()
        self.regiao = regiao
        self.voltar_callback = voltar_callback

        # Conecta ao banco
        con = sqlite3.connect("pokequiz.db")
        cursor = con.cursor()

        # Consulta top 10 por região
        cursor.execute("SELECT nick, pontuacao, dificuldade FROM pontuacoes WHERE regiao = ? ORDER BY pontuacao DESC LIMIT 10", (regiao,))
        resultados = cursor.fetchall()
        con.close()

        # Monta tabela de texto
        lista = []
        for i, (nick, pontos, dificuldade) in enumerate(resultados, start=1):
            lista.append(
                ft.Text(f"{i}. {nick} - {pontos} pts ({dificuldade})", color="white", size=20)
            )

        self.content = ft.Stack(
            controls=[
                ft.Image(src="src/assets/tela-inicial.gif", fit=ft.ImageFit.COVER, width=1600, height=900),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"🏆 Ranking da Região {regiao.capitalize()}", size=30, color="white", weight="bold"),
                            *lista,
                            ft.ElevatedButton("Voltar", on_click=self.voltar)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.center,
                    padding=20
                )
            ]
        )

    def voltar(self, e):
        self.voltar_callback()

