import requests

class TodoModel:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def get_all_todos(self):
        return requests.get(f'{self.api_base_url}todos')

    def create_todo(self, title, deadline):
        payload = {'title': title, 'deadline': deadline}
        return requests.post(f'{self.api_base_url}todos', json=payload)
    
    def update_todo(self, todo_id, title, deadline):
        payload = {'title': title, 'deadline': deadline}
        return requests.put(f'{self.api_base_url}todo/{todo_id}', json=payload)
    
    def delete_todo(self, todo_id):
        return requests.delete(f'{self.api_base_url}todo/{todo_id}')
    
    def complete_todo(self, todo_id):
        return requests.put(f'{self.api_base_url}complete/{todo_id}')
