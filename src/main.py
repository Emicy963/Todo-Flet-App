import flet as ft
import requests

API_BASE_URL = 'http://localhost:8000/api/'

def main(page: ft.Page):
    page.title = 'Todo Mobile App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create Todo
    title_field = ft.TextField(label='Title')
    deadline_field = ft.TextField(label='Deadline (YYYY-MM-DD)')
    creata_result = ft.Text()

    def creat_todo(e):
        payload = {
            'title': title_field.value,
            'deadline': deadline_field.value,
        }
        try:
            response = requests.post(API_BASE_URL + 'todos', json=payload)
            if response.status_code == 201:
                todo = response.json()
                creata_result.value = f'Create Todo: {todo}'
            else:
                creata_result.value = f'Erro: {response.text}'

            page.update()
        except Exception as ex:
            creata_result.value = f'Erro: {str(ex)}'

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

    # List Todos
    todo_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('#')),
            ft.DataColumn(ft.Text('Title')),
            ft.DataColumn(ft.Text('Create at')),
            ft.DataColumn(ft.Text('Deadline')),
            ft.DataColumn(ft.Text('Finish at')),
            ft.DataColumn(ft.Text('Options')),
        ],
        rows=[]
    )

    def list_todo(e):
        try:
            response = requests.get(API_BASE_URL + 'todos')
            todos = response.json()

            todo_table.rows.clear()

            for todo in todos:
                finish_button = ft.ElevatedButton(
                    text='Finish Todo',
                    data=todo['id'],
                    on_click=finish_todo,
                    disabled=bool(todo.get('finished_at'))
                    )
                
                row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(todo.get('id'))),
                        ft.DataCell(ft.Text(todo.get('title'))),
                        ft.DataCell(ft.Text(todo.get('created_at'))),
                        ft.DataCell(ft.Text(todo.get('deadline'))),
                        ft.DataCell(ft.Text(todo.get('finished_at'))),
                        ft.DataCell(finish_button)
                    ]
                )
                todo_table.rows.append(row)
            list_result.value = f'{len(todos)} todos founds'
            page.update()
        except Exception as ex:
            list_result.value = f'Erro: {str(ex)}'
            page.update()

    # Finished Todo
    def finish_todo(e):
        todo_id = e.control.data
        try:
            response = requests.put(f'{API_BASE_URL}todo/complete/{todo_id}')

            if response.status_code == 200:
                list_todo(None)
                list_result.value = 'Sucess Finished'
                page.update()
        except Exception as ex:
            list_result.value = f'Conection Error: {str(ex)}'
            page.update()

    list_result = ft.Text()
    list_button = ft.ElevatedButton(text='List Todos', on_click=list_todo)
    list_todos_tab = ft.Column(
        [todo_table,
         list_result,
         list_button,
         ],
         scroll=True
    )

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Create Todo', content=creat_todo_tab),
            ft.Tab(text='List Todos', content=list_todos_tab),
        ]
    )

    page.add(
        tabs
        )

if __name__ == '__main__':
    ft.app(target=main)
