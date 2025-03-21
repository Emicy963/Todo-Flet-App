import flet as ft
from src.models.todo_model import TodoModel
from src.controllers.todo_controller import TodoController
from src.views.todo_view import TodoViews

API_BASE_URL = 'http://localhost:8000/api/'

def main(page:ft.Page):
    model = TodoModel(API_BASE_URL)
    controller = TodoController(model)
    view = TodoViews(controller, ft.Page)
    page.add(view.build())

if __name__=='__main__':
    ft.app(target=main)
"""import flet as ft
import requests

API_BASE_URL = 'http://localhost:8000/api/'

def main(page: ft.Page):
    page.title = 'Todo Mobile App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create Todo
    title_field = ft.TextField(label='Title')
    deadline_field = ft.TextField(label='Deadline (YYYY-MM-DD)')
    create_result = ft.Text()

    def creat_todo(e):
        payload = {
            'title': title_field.value,
            'deadline': deadline_field.value,
        }
        try:
            response = requests.post(API_BASE_URL + 'todos', json=payload)
            if response.status_code == 201:
                todo = response.json()
                create_result.value = f'Create Todo: {todo}'
            else:
                create_result.value = f'Erro: {response.text}'

            page.update()
        except Exception as ex:
            create_result.value = f'Erro: {str(ex)}'

    creata_button = ft.ElevatedButton(text='New Todo', on_click=creat_todo)

    creat_todo_tab = ft.Column(
        [
            title_field,
            deadline_field,
            create_result,
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
            ft.DataColumn(ft.Text('Finish')),
            ft.DataColumn(ft.Text('Delete')),
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
                    on_hover=True,
                    disabled=bool(todo.get('finished_at'))
                    )
                #Delete Button
                delete_button = ft.ElevatedButton(
                    text='Delete Todo',
                    data=todo['id'],
                    on_click=delete_todo,
                    on_hover=True,
                )
                
                row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(todo.get('id'))),
                        ft.DataCell(ft.Text(todo.get('title'))),
                        ft.DataCell(ft.Text(todo.get('created_at'))),
                        ft.DataCell(ft.Text(todo.get('deadline'))),
                        ft.DataCell(ft.Text(todo.get('finished_at'))),
                        ft.DataCell(finish_button),
                        ft.DataCell(delete_button),
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

    #Delete Todo
    def delete_todo(e):
        todo_id = e.control.data
        try:
            response = requests.delete(f'{API_BASE_URL}todo/{todo_id}')

            if response.status_code == 204:
                list_todo(None)
                list_result.value = 'Sucess Delete'
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

    #Update Todo
    id_field = ft.TextField(label='ID Todo')
    title_update_field = ft.TextField(label='Title')
    deadline_update_field = ft.TextField(label='Deadline (YYYY-MM-DD)')

    def update_todo(e):
        payload = {
            'title': title_update_field.value,
            'deadline': deadline_update_field.value
        }
        try:
            response = requests.put(f'{API_BASE_URL}{int(id_field.value)}', json=payload)

            if response.status_code == 200:
                update_result.value = 'Todo Sucess Update'
                page.update()
        except Exception as ex:
            update_result.value = f'Erro: {str(ex)}'
            page.update()

    update_result = ft.Text()
    update_button = ft.ElevatedButton(text='Update Todo', on_click=update_todo)
    update_todo_tab = ft.Column(
        [
            id_field,
            title_update_field,
            deadline_update_field,
            update_result,
            update_button,
        ],
        scroll=True
    )

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text='Create Todo', content=creat_todo_tab),
            ft.Tab(text='List Todos', content=list_todos_tab),
            ft.Tab(text='Update Todos', content=update_todo_tab),
        ]
    )

    page.add(
        tabs
        )

if __name__ == '__main__':
    ft.app(target=main)
"""