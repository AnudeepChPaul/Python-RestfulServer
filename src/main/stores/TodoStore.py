from models.TodoModel import TodoModel


class TodoStore:
    def __init__(self, data=[]):
        self._data = data

    def get_todos(self):
        return self._data

    def get_todo(self, id):
        try:
            return self._data.__getitem__(id)
        except:
            return None

    def add_todo(self, todo):
        if todo is not None:
            self._data.append(todo)

    def clear_list(self):
        self._data.clear()

    def __len__(self):
        return len(self._data)