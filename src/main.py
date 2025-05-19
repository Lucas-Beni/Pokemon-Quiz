import flet as ft
from screens.tela_inicial import TelaInicial
from screens.tela_selecao import TelaSelecaoRegiao

def main(page: ft.Page):
    # Configuração da janela
    page.title = "PokeQuizz - Tela Inicial"
    page.window.width = 1600
    page.window.height = 900
    page.window.center()
    page.padding = 0
    page.bgcolor = ft.Colors.BLACK

    # Função chamada ao clicar em "Jogar"
    def iniciar_jogo(e):
        def iniciar_quiz(regiao):
            print(f"Iniciando quiz da região: {regiao}")
            # Futuramente: page.clean(); page.add(TelaQuiz(regiao))
        
        page.clean()
        tela_selecao = TelaSelecaoRegiao(iniciar_quiz)
        page.add(tela_selecao)

    # Tela inicial
    tela = TelaInicial(iniciar_jogo)
    page.add(tela)

ft.app(target=main)
