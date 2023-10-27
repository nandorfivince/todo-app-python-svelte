from flask import Flask, jsonify, request
from flask_cors import CORS
from tinydb import TinyDB, Query
import os

app = Flask(__name__)
CORS(app)  # CORS beállítása az alkalmazás számára

# Abszolút elérési út beállítása
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'todos.json')

db = TinyDB(DATABASE_PATH)

def get_next_id():
    todos = db.all()
    if todos:
        return max([todo["id"] for todo in todos]) + 1
    return 1

@app.route('/add', methods=['POST'])
def add_todo():
    data = request.json
    todo_text = data.get('text')
    if not todo_text:
        return jsonify({'error': 'Text is required'}), 400
    todo_id = get_next_id()
    db.insert({'id': todo_id, 'text': todo_text, 'completed': False})
    return jsonify({'message': 'Todo added successfully'}), 200

@app.route('/list', methods=['GET'])
def list_todos():
    todos = db.all()
    return jsonify(todos), 200

@app.route('/delete/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    Todo = Query()
    todo = db.get(Todo.id == todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    db.remove(Todo.id == todo_id)
    return jsonify({'message': 'Todo deleted successfully'}), 200

@app.route('/clear', methods=['DELETE'])
def clear_todos():
    db.truncate()
    return jsonify({'message': 'All todos deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
