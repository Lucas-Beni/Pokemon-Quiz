import flet as ft
import requests

class TelaQuiz(ft.Container):
    def __init__(self, regiao: str):
        super().__init__()
        self.regiao = regiao # salva a região escolhida

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
                    content=coluna,
                    col={"xs": 4, "sm": 3, "md": 2, "lg": 1},
                    padding=3
                )
                for _, _, _, coluna in self.lista_pokemon
            ]
        )

        # Campo de input para adivinhação
        self.input_nome = ft.TextField(
            label="Digite o nome do Pokémon",
            width=300
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
                ft.Container(content=self.input_nome, margin=ft.margin.only(top=20, bottom=130)),
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

    def adicionar_pokemon(self, numero, nome, pokemon_id): # função para adicionar os pokemon na lista_pokemon
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png" # salva o sprite do pokemon correspondente
        sprite = ft.Image(
            src=sprite_url,
            width=64,
            height=64,
            color="Black", # Aplica cor preta
            opacity=1,
        ) # cria a imagem do sprite
        nome_texto = ft.Text(value=nome.capitalize(), opacity=0, color="white", size=15) # cria o nome do pokemon que fica escondido até ser descoberto

        coluna = ft.Column( # cria a coluna de cada pokemon
            controls=[
                ft.Text(str(numero), color="white", size=15), # coloca como item mais alto na coluna
                sprite, # coloca o sprite como item central na coluna
                nome_texto # coloca o nome do pokemon como item mais baixo na coluna
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER # alinha todos os itens da coluna
        )

        self.lista_pokemon.append((nome, sprite, nome_texto, coluna)) # adiciona todas as informações dos pokemon na lista_pokemon