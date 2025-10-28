# TODO: Später könnte man hier eine Beschreibung zu den Todos hinzufügen

from flask import Flask, render_template_string, request, redirect
from datetime import datetime

app = Flask(__name__)

# Einfache In-Memory Datenbank
todos = []
next_id = 1


class Todo:
    def __init__(self, id, title, date, category="Allgemein"):
        self.id = id
        self.title = title
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.category = category


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 50px auto; 
            padding: 20px;
        }
        h1 { color: #333; }
        .todo-item { 
            background: #f4f4f4; 
            padding: 10px; 
            margin: 10px 0; 
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        input, select { 
            padding: 8px; 
            margin: 5px; 
        }
        button { 
            padding: 8px 15px; 
            background: #4CAF50; 
            color: white; 
            border: none; 
            border-radius: 4px; 
            cursor: pointer;
        }
        button:hover { background: #45a049; }
        .delete-btn { background: #f44336; }
        .delete-btn:hover { background: #da190b; }
        .category { 
            background: #2196F3; 
            color: white; 
            padding: 3px 10px; 
            border-radius: 3px; 
            font-size: 12px;
        }
    </style>
</head>
<body>
    <h1>📝 Meine Todos</h1>
    
    <form method="POST" action="/add">
        <input type="text" name="title" placeholder="Todo Titel" required>
        <input type="date" name="date" required>
        <select name="category">
            <option value="Arbeit">Arbeit</option>
            <option value="Privat">Privat</option>
            <option value="Schule">Schule</option>
        </select>
        <button type="submit">Hinzufügen</button>
    </form>
    
    <hr>
    
    {% if todos %}
        {% for todo in todos %}
        <div class="todo-item">
            <div>
                <strong>{{ todo.title }}</strong><br>
                <small>📅 {{ todo.date.strftime('%d.%m.%Y') }}</small>
                <span class="category">{{ todo.category }}</span>
            </div>
            <form method="POST" action="/delete/{{ todo.id }}" style="margin:0;">
                <button type="submit" class="delete-btn">🗑️ Löschen</button>
            </form>
        </div>
        {% endfor %}
    {% else %}
        <p>Keine Todos vorhanden. Füge dein erstes Todo hinzu!</p>
    {% endif %}
    
    <hr>
    <p><small>M324 LB - DevOps Projekt | Total Todos: {{ todos|length }}</small></p>
</body>
</html>
"""


@app.route("/")
def index():
    """Zeigt alle Todos"""
    # Sortiere nach Datum
    sorted_todos = sorted(todos, key=lambda x: x.date)
    return render_template_string(HTML_TEMPLATE, todos=sorted_todos)


@app.route("/add", methods=["POST"])
def add():
    """Fügt ein neues Todo hinzu"""
    global next_id
    title = request.form.get("title")
    date = request.form.get("date")
    category = request.form.get("category", "Allgemein")
    
    todo = Todo(next_id, title, date, category)
    todos.append(todo)
    next_id += 1
    
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    """Löscht ein Todo"""
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return redirect("/")


@app.route("/health")
def health():
    """Health Check für Azure"""
    return {"status": "healthy", "todos": len(todos)}, 200


if __name__ == "__main__":
    # Beispiel-Daten hinzufügen
    todos.append(Todo(1, "M324 LB fertigstellen", "2025-01-15", "Schule"))
    todos.append(Todo(2, "GitHub Repository aufsetzen", "2025-01-10", "Schule"))
    todos.append(Todo(3, "CI/CD Pipeline konfigurieren", "2025-01-12", "Schule"))
    next_id = 4
    
    app.run(debug=True, host="0.0.0.0", port=5000)
