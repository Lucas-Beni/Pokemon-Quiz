import flet as ft
import requests
import asyncio

class TelaQuiz(ft.Container):
    def __init__(self, regiao: str, dificuldade: str, page: ft.Page):
        super().__init__()
        self.regiao = regiao # salva a região escolhida
        self.dificuldade = dificuldade
        self.page = page

        self.img_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/fundo_pc.png", # caminho para o arquivo do GIF 
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
        )

        self.lista_pokemon = [] # cria a lista na qual será armazenados os pokemon

        if regiao.lower() == "national":
            url = "https://pokeapi.co/api/v2/pokedex/national"  # salva a url para a api diretamente para a national dex
            resposta = requests.get(url) # busca os dados da url correspondente

            if resposta.status_code == 200: # verifica se a requisição na web foi bem-sucedida
                dados = resposta.json()
                entradas = dados["pokemon_entries"] # pega a lista de pokemon

                for i, entrada in enumerate(entradas, start=1): # faz um loop sobre cada pokemon
                    nome = entrada["pokemon_species"]["name"] # salva o nome do pokemon
                    pokemon_id = entrada["entry_number"]
                    self.adicionar_pokemon(i, nome, pokemon_id)

        else:
            url = f"https://pokeapi.co/api/v2/generation/{regiao}" # salva a url para a api diretamente na região escolhida
            resposta = requests.get(url) # busca os dados da url correspondente

            if resposta.status_code == 200: # verifica se a requisição na web foi bem-sucedida
                dados = resposta.json()
                especies = dados["pokemon_species"] # pega a lista de pokemon da regiao

                # Ordena por ID extraído da URL (ex: .../pokemon-species/25/)
                especies.sort(key=lambda especie: int(especie["url"].split("/")[-2]))

                for i, especie in enumerate(especies, start=1): # faz um loop sobre cada pokemon da regiao
                    nome = especie["name"] # salva o nome do pokemon
                    pokemon_id = int(especie["url"].split("/")[-2])
                    self.adicionar_pokemon(i, nome, pokemon_id)

        # Gera grid de Pokémon
        self.grid = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=pokemon["coluna"],
                    col={"xs": 4, "sm": 3, "md": 2, "lg": 1}, # configura a quantidade de colunas por tamanho de tela
                    padding=3
                )
                for pokemon in self.lista_pokemon
            ]
        )

        self.streak = 0
        self.ultimo_numero_descoberto = 0
        self.pontos = 0

        self.pontuacao = ft.Text(
            f"Pontos: {self.pontos} (Streak x{self.streak})",
            color="White",
            size=15
        )

        self.hora, self.min, self.sec = 0, 0, 0

        self.label_tempo = ft.Text(
            f"Tempo restante / {self.hora}:{self.min}:{self.sec}",
        )

        # Campo de input para adivinhação
        self.input_nome = ft.TextField(
            label="Digite o nome do Pokémon",
            width=300,
            color="White",
            on_change=self.verificar_nome
        )

        # Scroll com altura ajustada
        scroll_coluna = ft.Column(
            controls=[self.grid],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

        # Layout da tela
        self.conteudo_interface = ft.Column(
            controls=[
                ft.Container(  # linha com input e pontuação
                    content=ft.Row(
                        controls=[
                            self.label_tempo,
                            self.input_nome,
                            self.pontuacao
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # separa os elementos
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    width=800,  # largura máxima da linha (ajuste como quiser)
                    margin=ft.margin.only(top=20, bottom=130)
                ),
                ft.Container(content=scroll_coluna, height=600)
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.content = ft.Stack(
            controls=[
                self.img_fundo,
                ft.Container(
                    content=self.conteudo_interface,
                    padding=20,
                    alignment=ft.alignment.top_center
                )
            ]
        )

        print(self.lista_pokemon)

    async def rodar_tempo(self): # cria uma função assíncrona que permite que outras partes do programa rodem enquanto ela funciona em segundo plano
        if self.regiao == "national":
            self.tempo = 5400
        else:
            self.tempo = 900

        for t in range(self.tempo, 0, -1): # cria um loop que começa com o valor de self.tempo e diminui de 1 em 1 até zerar
            self.tempo_restante = t
            horas = t // 3600
            minutos = (t % 3600) // 60
            segundos = t % 60

            self.label_tempo.value = f"⏱ Tempo restante / {horas:02}:{minutos:02}:{segundos:02}" # atualiza o valor do label_tempo
            self.label_tempo.update() # atualiza o label_tempo na interface
            await asyncio.sleep(1) # espera 1 segundo antes de rodar o loop novamente
        
        self.label_tempo.value = "⏱ Tempo esgotado!" # quando o cronometro zerar o valor de self.tempo vira esse
        self.label_tempo.update() # atualiza o label_tempo na interface
        self.mostrar_popup_final(venceu=False)

    def did_mount(self): # did_mount é um método do próprio flet que é chamado automáticamente quanto o controle(tela) é adicionado na página
        self.page.run_task(self.rodar_tempo) # roda a função rodar_tempo assim que a pagina tela_quiz é carregada

    def adicionar_pokemon(self, numero, nome, pokemon_id): # função para adicionar os pokemon na lista_pokemon
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png" # salva o sprite do pokemon correspondente
        pokebola_url = "src/assets/pokebola.png"

        if self.dificuldade == "1":  # Modo Normal
            sprite = ft.Image(
                src=sprite_url,
                width=64,
                height=64,
                color="Black",  # silhueta preta
                opacity=1,
            )
       
        elif self.dificuldade == "2":  # Modo Difícil
            sprite = ft.Image(
                src=pokebola_url,
                width=64,
                height=64,
                opacity=1,
            )

        nome_texto = ft.Text(value=nome.capitalize(), opacity=0, color="white", size=15) # cria o nome do pokemon que fica escondido até ser descoberto

        descoberto = False

        coluna = ft.Column( # cria a coluna de cada pokemon
            controls=[
                ft.Text(str(numero), color="white", size=15), # coloca como item mais alto na coluna
                sprite, # coloca o sprite como item central na coluna
                nome_texto, # coloca o nome do pokemon como item mais baixo na coluna
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER # alinha todos os itens da coluna
        )

        self.lista_pokemon.append({
            "nome": nome, 
            "sprite": sprite, 
            "nome_texto": nome_texto, 
            "coluna": coluna,
            "descoberto": descoberto,
            "pokemon_id": pokemon_id
            }) # adiciona todas as informações dos pokemon na lista_pokemon

    def verificar_nome(self, e):
        nome_digitado = e.control.value.strip().lower()

        for i, pokemon in enumerate(self.lista_pokemon):
            if nome_digitado.lower() == pokemon["nome"].lower() and not pokemon["descoberto"]:
                if self.dificuldade == "1":
                    pokemon["sprite"].color = None
                    pokemon["nome_texto"].opacity = 1
                    pokemon["descoberto"] = True
                elif self.dificuldade == "2":
                    pokemon["sprite"].src = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon["pokemon_id"]}.png"
                    pokemon["nome_texto"].opacity = 1
                    pokemon["descoberto"] = True

                numero_atual = i + 1 # cria a variavel numero_atual que representa o número do pokémon na lista_pokemon

                if numero_atual == self.ultimo_numero_descoberto + 1: # verifica se o pokemon descoberto segue a sequência do anterior
                    self.streak = min(self.streak + 1, 3)  # aumenta o streak até no máximo x3
                else:
                    self.streak = 1  # se a sequência for interrompida o streak volta a ser x1
                
                self.ultimo_numero_descoberto = numero_atual

                self.pontos += 1000 * self.streak
                self.pontuacao.value = f"Pontos: {self.pontos} (Streak x{self.streak})"
                self.input_nome.value = ""

                self.pontuacao.update()
                pokemon["sprite"].update()
                pokemon["nome_texto"].update()
                self.input_nome.update()
                break  # já encontrou, não precisa continuar
            else:
                return
            
        if all(p["descoberto"] for p in self.lista_pokemon):
                tempo_restante = getattr(self, "tempo_restante", 0)
                self.mostrar_popup_final(venceu=True, tempo_restante=tempo_restante)

    def mostrar_popup_final(self, venceu: bool, tempo_restante: int = 0):
        if venceu:
            bonus = (tempo_restante // 60) * 10000
            self.pontos += bonus
            mensagem = f"🎉 Parabéns! Você descobriu todos os Pokémon!\n\nBônus: +{bonus} pontos\nPontuação final: {self.pontos}"
        else:
            mensagem = f"⏱ Tempo esgotado!\n\nPontuação final: {self.pontos}"

        popup = ft.AlertDialog(
            modal=True,  # <<< ESSENCIAL: impede interação com o fundo
            title=ft.Text("Fim de Jogo"),
            content=ft.Text(mensagem),
            actions=[
                ft.TextButton(
                    "OK",
                    on_click=lambda e: self.fechar_popup()
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            open=True,
        )

        self.page.dialog = popup
        self.page.update()

    def fechar_popup(self):
        self.page.dialog.open = False
        self.page.update()
        self.page.go("/")  # Redireciona de volta ao menu ou onde quiser