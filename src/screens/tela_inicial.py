import flet as ft

class TelaInicial(ft.UserControl): # a classe UserControl do flet permite que você crie seus próprios componentes e utilizá-los como se fossem um componente nativo do flet
    def __init__(self, ao_jogar_callback): # cria a função construtora __init__  que cria a função que será chamada quando o botão jogar for clicado
        super().__init__() # esse comando é comum em classes que usam outras classes. Nesse caso o super() chama a classe mãe UserControl e permite que seja inicializado corretamente
        self.ao_jogar_callback = ao_jogar_callback # cria a função que será chamada quando o botão jogar for clicado

    def build(self): # método que monta o conteúdo da tela, ele é chamado automáticamente pela tela
        self.gif_fundo = ft.Image( # componente para exibir uma imagem ou GIF
            src="src/assets/tela-inicial.gif", # caminho para o arquivo do GIF
            fit=ft.ImageFit.COVER, # ajusta a imagem para cobrir toda a área (mantendo proporção)
            width=1600, # define a largura do GIF
            height=900, # define a altura do GIF
        )


        botao_jogar = ft.ElevatedButton( # variável que representa o botão de jogar
            text="Jogar", # texto dentro do botão
            on_click=self.ao_jogar_callback, # função que será chamada quando o botão jogar for clicado
            width = 200,
            height = 50
        )

        conteudo = ft.Stack( # variável que contém todo o conteúdo da tela. ft.Stack permite a sobreposição de elementos na tela
            controls=[
                self.gif_fundo, # coloca o GIF como a camada mais inferior da tela
                ft.Container( # conteiner que centraliza o conteúdo na tela
                    content=ft.Column( # (content) coloca o Column dentro do Container/ (Column) empilha elementos verticalmente
                        controls=[botao_jogar], # cria o botão jogar na tela
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    alignment=ft.alignment.center, # alinha o conteúdo dentro do Container no centro
                    expand=True # faz o container usar todo o espaço disponível
                )
            ],
            width= self.page.window.width, # define a largura do conteudo como a largura da tela
            height= self.page.window.height, # define a altura do conteudo como a altura da tela
            # expand=True # garante que a variável conteudo use todo o espaço disponivel na tela
        )

        return conteudo