import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    # Buttons
    def button_Ja(e):
        print("\033c", end="")
        print("Ja")
        page.update()

    def button_Nein(e):
        print("\033c", end="")
        print("Nein")
        page.update()

    # Start des UIs mit der main Page
    def route_change(route):
        page.views.clear()
        page.theme_mode = ft.ThemeMode.DARK
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Wähle Modus mit dem Discord Bot"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ft.ElevatedButton("Ja/Nein",
                                      height=50,
                                       width=100,
                                       bgcolor=ft.Colors.WHITE,
                                       color=ft.Colors.BLUE_900,
                                         on_click=lambda _: page.go("/JaNein")),
                ],
            )
        )
        # UI subfenster Ja/Nein Auswahl
        if page.route == "/JaNein":
            page.views.append(
                ft.View(
                    "/JaNein",
                    [
                        ft.AppBar(title=ft.Text("Ja/Nein"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                        ft.Row(
                            [
                                ft.Container( content=ft.ElevatedButton(
                                    "Ja",
                                    on_click=button_Ja,
                                    color=ft.Colors.GREEN_400,
                                    height=100,
                                    width=200,
                                    style=ft.ButtonStyle(
                                        color= ft.Colors.RED,
                                    ),
                                ),
                                alignment=ft.alignment.center,
                                expand=True
                                ),
                                ft.Container(
                                    content=ft.ElevatedButton(
                                        "Nein",
                                        on_click=button_Nein,
                                        color=ft.Colors.RED_400,
                                        height=100,
                                        width=200,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.RED,
                                        ),
                                    ),
                                    alignment=ft.Alignment(0, 0),
                                    expand=True,
                                )
                            ]
                        )
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



ft.app(main)