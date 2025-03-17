import flet as ft

API_BASE_URL = 'https://localhost:8000/api/todos/'

def main(page: ft.Page):
    page.title = 'Todo Mobile App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create Todo
    title_field = ft.TextField(label='Title')
    deadline_field = ft.TextField(label='Deadline (DD-MM-YYYY)')
    todo_result = ft.Text()

    

    exemple_tab = ft.Column(
        [
            title_field,
            deadline_field
        ],
        scroll=True
    )
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Create Todo', content=exemple_tab)
        ]
    )

    page.add(
        tabs
        )

if __name__ == '__main__':
    ft.app(target=main)
