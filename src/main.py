import flet as ft

def main(page: ft.Page):
    page.title = 'Todo Mobile App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add()

if __name__ == '__main__':
    ft.app(target=main)
