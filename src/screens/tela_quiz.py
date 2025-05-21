import flet as ft
import requests

class TelaQuiz(ft.Container):
    def __init__(self, regiao: str):
        super().__init__()
        self.regiao = regiao # salva a região escolhida
        url = f"https://pokeapi.co/api/v2/pokedex/{regiao.lower()}" # salva a url para a api diretamente na região escolhida
        resposta = requests.get(url) # busca os dados da url correspondente

        self.gif_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/tela-inicial.gif", # caminho para o arquivo do GIF 
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
            width=1600,# define a largura do GIF 
            height=900, # define a altura do GIF
        )

        if resposta.status_code == 200: # verifica se a requisição na web foi bem-sucedida
            dados = resposta.json()
            entradas = dados["pokemon_entries"] # pega a lista de pokemon da regiao

            self.lista_pokemon = [] # cria a lista na qual será armazenados os pokemon

            for i, entrada in enumerate(entradas, start=1): # faz um loop sobre cada pokemon da regiao
                nome = entrada["pokemon_species"]["name"] # salva o nome do pokemon

                species_url = entrada["pokemon_species"]["url"] # salva a url de cada pokemon
                resposta_species = requests.get(species_url) # busca os dados na url correspondente

                if resposta_species.status_code == 200: # verifica se a requisição na web foi bem-sucedida
                    pokemon_id = resposta_species.json()["id"] # dentro do json que foi retornado à requisição HTTP, busca o campo "id" com o número correspondente na national dex
                    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png" # salva a url do sprite correspondente
                else:
                    sprite_url = "" # se a requisição HTTP não for bem-sucedida o pokemon fica sem sprite

                sprite = ft.Image(src=sprite_url, width=32, height=32, opacity=1) # cria o sprite de cada pokemon

                nome_texto = ft.Text(value=nome.capitalize(), visible=False, color="white") # cria o nome que fica escondido enquando não for descoberto

                pokemon_coluna = ft.Column( # cria uma coluna para cada pokemon com o número, sprite e nome
                    controls=[
                        ft.Text(str(i), color="white"),
                        sprite,
                        nome_texto
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )

                self.lista_pokemon.append((nome, sprite, nome_texto, pokemon_coluna)) # adiciona todas as informaçoes na lista_pokemon

            
            self.grid = ft.ResponsiveRow(
                controls=[coluna for _, _, _, coluna in self.lista_pokemon] # cria a linha com todos os pokemon dentro da lista_pokemon
            )

            self.conteudo_interface = ft.Column(
                controls=[
                    ft.Text(f"Quiz da região: {regiao}", size=30, color="white"),
                    self.grid
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

            self.content = ft.Stack(
                controls=[
                    self.gif_fundo,
                    self.conteudo_interface
                ]
            )
        else:  
            self.content = ft.Text(value="Erro ao carregar região", color="red")
