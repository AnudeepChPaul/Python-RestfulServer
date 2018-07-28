from http.server import BaseHTTPRequestHandler
from io import BytesIO
# from pymongo import MongoClient
import urllib

# client = MongoClient('localhost', 27017)

# db = client.test
# collection = db.collection
from models.TodoModel import TodoModel
from stores.TodoStore import TodoStore


class RestfulServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        store = TodoStore()
        todo1 = TodoModel("todo1", "dataaaaaaa")
        todo2 = TodoModel("todo2", "dataaaaaaa")

        store.add_todo(todo1)
        store.add_todo(todo2)

        print(store.get_todo(1))

        response = BytesIO()
        response.write(
            bytes({"success: True, path": "{path}".format(path=self.path).__str__(), "data": str(store.get_todo(2))}.__str__(), 'utf-8')
        )

        self.wfile.write(response.getvalue())

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        payload = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        print(self.request)

        # payload = self.headers.get('query')
        response = BytesIO()
        data = []

        for rawdata in entry:
            data.extend([rawdata])

        response.write(
            bytes({"data": store.get_todos().__getitem__(0)}.__str__(), 'utf-8')
        )
        self.set_headers()
        self.wfile.write(response.getvalue())
