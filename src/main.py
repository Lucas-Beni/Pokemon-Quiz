import flet as ft
from screens.tela_inicial import TelaInicial
from screens.tela_selecao import TelaSelecaoRegiao
from screens.tela_selecao_dificuldade import TelaDificuldade
from screens.tela_quiz import TelaQuiz  # uma única tela para qualquer região
from screens.tela_leaderboard import TelaLeaderboard
import sqlite3

conn = sqlite3.connect("pokequiz.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pontuacoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nick TEXT,
    regiao TEXT,
    dificuldade TEXT,
    pontuacao INTEGER
)
""")

def main(page: ft.Page):
    # Configurações da janela
    page.title = "PokeQuizz - Tela Inicial"
    page.window.width = 1600
    page.window.height = 900
    page.window.center()
    page.padding = 0
    page.bgcolor = ft.Colors.ORANGE_100
    
    # Configuração importante para diálogos
    page.overlay.clear()

    def iniciar_leaderboard(e):
        def selecionar_regiao_para_leaderboard(regiao):
            page.clean()
            page.add(TelaLeaderboard(regiao, voltar_callback=mostrar_menu))
        def mostrar_menu():
            page.clean()
            page.add(TelaInicial(iniciar_jogo_com_nick, iniciar_leaderboard))
        
        page.clean()
        page.add(TelaSelecaoRegiao(selecionar_regiao_para_leaderboard))

    # Função chamada ao clicar em "Jogar"
    def iniciar_jogo_com_nick(nick):
        def iniciar_quiz(regiao):  # chamada quando a região é selecionada
            def selecionar_dificuldade(dificuldade):
                print(f"Iniciando quiz da região: {regiao}")
                page.clean()
                def voltar_para_inicio():
                    page.clean()
                    page.add(TelaInicial(iniciar_jogo_com_nick, iniciar_leaderboard))

                quiz = TelaQuiz(regiao, dificuldade, page, nick, voltar_callback=voltar_para_inicio)

                page.add(quiz)
                # Garante que o quiz foi montado na página
                quiz.did_mount() if hasattr(quiz, 'did_mount') else None
            page.clean()
            page.add(TelaDificuldade(selecionar_dificuldade))
        page.clean()
        page.add(TelaSelecaoRegiao(iniciar_quiz))

    # Tela inicial
    page.add(TelaInicial(iniciar_jogo_com_nick, iniciar_leaderboard))

ft.app(target=main)