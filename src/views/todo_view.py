import flet as ft
from ..controllers.todo_controller import TodoController

class TodoViews:
    def __init__(self, controller: TodoController, page: ft.Page):
        self.controller = controller
        self.page = page
        self.page.title = 'Todo App'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Initialize UI Components
        self.title_field = ft.TextField(label='Title')
        self.deadline_field = ft.TextField(label='Deadline (YYYY-MM-DD)')
        self.create_result = ft.Text()
        self.todo_table = self.create_todo_table()
        self.list_result = ft.Text()
        self.id_field = ft.TextField(label='ID Todo')
        self.title_update_field = ft.TextField(label='New Title')
        self.deadline_update_field = ft.TextField(label='New Deadline (YYYY-MM-DD)')
        self.update_result = ft.Text()

    def create_todo_table(self):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text('#')),
                ft.DataColumn(ft.Text('Title')),
                ft.DataColumn(ft.Text('Create')),
                ft.DataColumn(ft.Text('Deadline')),
                ft.DataColumn(ft.Text('Finish at')),
                ft.DataColumn(ft.Text('Finish')),
                ft.DataColumn(ft.Text('Delete'))
            ],
            rows=[]
        )
    
    def build(self):
        return ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text='Create Todo', content=self.create_tab())
            ]
        )
    
    def create_tab(self):
        return ft.Column([
            self.title_field,
            self.deadline_field,
            self.create_result,
            ft.ElevatedButton(text='New Todo', on_click=self.create_todo_click)
        ], scroll=True)
    
    def list_tab(self):
        return ft.Column([
            self.todo_table,
            self.list_result,
            ft.ElevatedButton(text='List Todos', on_click=self.list_todo_click)
        ], scroll=True)
    
    def update_tab(self):
        return ft.Column([
            self.id_field,
            self.title_update_field,
            self.deadline_update_field,
            ft.ElevatedButton(text='Update Todo', on_click=self.update_todo_click)
        ], scroll=True)
    
    
