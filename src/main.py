import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)
    t = ft.Text(value=f"Você está no clique n°{counter.value}", color="green")

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        t.value = f"Você está no clique n°{counter.data}"
        counter.update()
        t.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        t,
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )


ft.app(main)
