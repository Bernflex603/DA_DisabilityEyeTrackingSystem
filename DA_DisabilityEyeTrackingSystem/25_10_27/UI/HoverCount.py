import flet as ft
import time

#def hoverCount(btnTxt:str):
#    startTime = time.time()
#    elapsedTime = time.time() - startTime
#    if elapsedTime < 1:
#        print("Focus on {btnTxt}")

#def hoverSim(ButtonText:str):
#    print(f"Clicked on {ButtonText}")

def mainpage(page: ft.Page):
    page.title = "Hover Count Example"

    def buttonClick(ButtonNr:int):
        print(f"Clicked on Button{ButtonNr}")

    page.add(
        ft.ElevatedButton(
            text="Button1", 
            icon=ft.Icons.WAVES_ROUNDED, 
            width=150, 
            height=400,
            on_click=buttonClick(1)
        ),
        
        ft.ElevatedButton(
            text="Button2",
            icon=ft.Icons.PARK_ROUNDED,
            icon_color=ft.Colors.GREEN_400,
            height=200,
            width=500,
            style=ft.ButtonStyle(
                color= ft.Colors.RED,
            ),
            on_click=buttonClick(2)
        )
    )
    
ft.app(target=mainpage)
    
    

