from ..models.todo_model import TodoModel

class TodoController:
    def __init__(self, model: TodoModel):
        self.model = model

    def handle_get_all_todo(self):
        return self.model.get_all_todos()
    
    def handle_create_todo(self, title, deadline):
        return self.model.create_todo(title, deadline)
    
    def handle_update_todo(self, todo_id, title, deadline):
        return self.model.update_todo(todo_id, title, deadline)
    
    def handle_delete_todo(self, todo_id):
        return self.model.delete_todo(todo_id)
    
    def handle_complete_todo(self, todo_id):
        return self.model.complete_todo(todo_id)
