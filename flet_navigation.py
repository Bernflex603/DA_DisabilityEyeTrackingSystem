# pylint: disable=unexpected-keyword-arg
# pylint: disable=too-many-functions
import os #Kann entfernt werden, wenn die Funktion clear_terminal nicht mehr benötigt wird
import flet as ft



def clear_terminal(text: str):
    os.system("cls" if os.name == "nt" else "clear")
    print(text)


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Flet UI"
    page.padding = 0

    # -------- Button Style --------
    Default_Style = ft.ButtonStyle(
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLUE_900,
        text_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
    )
     #Eventuell Styles nur für Ja nein etc. machen für schöneres Design 

    # -------- Navigation --------
    def show(view_func):
        page.clean()
        page.add(view_func())
        page.update()

    def appbar(title: str):
        return ft.AppBar(
            title=ft.Text(title),
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda e: show(main_page),
            ),
        )

    # -------- Main Page --------
    def main_page():
        return ft.Column(
            controls=[
                ft.AppBar(title=ft.Text("Main Page")),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Ja / Nein",
                            style=Default_Style,
                            on_click=lambda e: show(ja_nein),
                        ),
                        ft.ElevatedButton(
                            "4-Auswahl",
                            style=Default_Style,
                            on_click=lambda e: show(vier),
                        ),
                        ft.ElevatedButton(
                            "Bild-Auswahl",
                            style=Default_Style,
                            on_click=lambda e: show(bilder),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            expand=True,
        )

    # -------- Ja / Nein --------
    def ja_nein():
        return ft.Column(
        controls=[
            appbar("Ja / Nein"),
            ft.Row(
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        expand=True,
                        alignment=ft.Alignment(-0.25, 0),  # links + etwas nach unten
                        content=ft.ElevatedButton(
                            "Ja",
                            height=120,
                            width=200,
                            style=Default_Style,
                            on_click=lambda e: clear_terminal("Ja"),
                        ),
                    ),
                    ft.Container(
                        expand=True,
                        alignment=ft.Alignment(0.25, 0),  # rechts + Mitte
                        content=ft.ElevatedButton(
                            "Nein",
                            height=120,
                            width=200,
                            style=Default_Style,
                            on_click=lambda e: clear_terminal("Nein"),
                        ),
                    ),
                ],
            ),
        ],
        expand=True,
    )

    # -------- 4-Auswahl --------
    def vier():
        def btn(n):
            return ft.ElevatedButton(
                str(n),
                width=120,
                height=120,
                style=Default_Style,
                on_click=lambda e, x=n: clear_terminal(str(x)),
            )

        return ft.Column(
            controls=[
                appbar("4-Auswahl"),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[btn(1), btn(2)],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                        ft.Row(
                            controls=[btn(3), btn(4)],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            expand=True,
        )

    # -------- Bilder --------
    def bilder():
        text1 = ft.TextField(hint_text="Text für Bild 1")
        text2 = ft.TextField(hint_text="Text für Bild 2")

        def click_1():
            clear_terminal(text1.value)

        def click_2():
            clear_terminal(text2.value)

        def img(src, click_fn):
            return ft.GestureDetector(
                on_tap=lambda e: click_fn(),
                content=ft.Image(src=src, width=160, height=160),
            )

        return ft.Column(
        controls=[
            appbar("Bild-Auswahl"),
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            img("C:\\HTL\\DIP. Arbeit\\Programm\\Bild1.jpg", click_1),
                            img("C:\\HTL\\DIP. Arbeit\\Programm\\Bild2.jpg", click_2),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                    text1,
                    text2,
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        expand=True,
    )

    # -------- Start --------
    show(main_page)


ft.app(target=main)