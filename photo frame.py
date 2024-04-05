import time
import flet as ft
from threading import Timer

def main(page: ft.Page):
    i = ft.Image(src="https://picsum.photos/150/150", width=250, height=250)

    def automatically_change_image():
        i.src = f"https://picsum.photos/150/150?{time.time()}"
        page.update()
        image = Timer(2, automatically_change_image)
        image.start()

    def skip(e):
        automatically_change_image()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30

    page.add(
        i,
        ft.ElevatedButton("Skip!", on_click=skip),
    )

    automatically_change_image()

if __name__ == "__main__":
    ft.app(target=main)

#references: https://docs.python.org/3/library/threading.html and https://flet.dev/docs/ 