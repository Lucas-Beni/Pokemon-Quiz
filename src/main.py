import flet as ft
from screens.tela_inicial import TelaInicial
from screens.tela_selecao import TelaSelecaoRegiao
from screens.tela_quiz import TelaQuiz  # uma única tela para qualquer região

def main(page: ft.Page):
    # Configurações da janela
    page.title = "PokeQuizz - Tela Inicial"
    page.window.width = 1600
    page.window.height = 900
    page.window.center()
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE

    # Função chamada ao clicar em "Jogar"
    def iniciar_jogo(_):
        def iniciar_quiz(regiao):  # chamada quando a região é selecionada
            print(f"Iniciando quiz da região: {regiao}")
            page.clean()
            page.add(TelaQuiz(regiao))  # cria a tela do quiz com base na região

        page.clean()
        page.add(TelaSelecaoRegiao(iniciar_quiz))

    # Tela inicial
    page.add(TelaInicial(iniciar_jogo))

ft.app(target=main)