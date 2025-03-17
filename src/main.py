import flet as ft
import requests

API_BASE_URL = 'http://localhost:8000/api/todos/'

def main(page: ft.Page):
    page.title = 'Todo Mobile App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create Todo
    title_field = ft.TextField(label='Title')
    deadline_field = ft.TextField(label='Deadline (DD-MM-YYYY)')
    creata_result = ft.Text()

    def creat_todo(e):
        payload = {
            'title': title_field.value,
            'deadline': deadline_field.value,
        }

        response = requests.post(API_BASE_URL + '', json=payload)
        if response.status_code == 201:
            todo = response.json()
            creata_result.value = f'Create Todo: {todo}'
        else:
            creata_result.value = f'Erro: {response.text}'

        page.update()

    creata_button = ft.ElevatedButton(text='New Todo', on_click=creat_todo)

    creat_todo_tab = ft.Column(
        [
            title_field,
            deadline_field,
            creata_result,
            creata_button,
        ],
        scroll=True
    )
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Create Todo', content=creat_todo_tab)
        ]
    )

    page.add(
        tabs
        )

if __name__ == '__main__':
    ft.app(target=main)
