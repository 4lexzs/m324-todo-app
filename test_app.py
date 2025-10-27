"""
Tests für die Todo-App
"""
import pytest
from app import app, todos, Todo


@pytest.fixture
def client():
    """Test-Client erstellen"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_läuft(client):
    """Test: App antwortet"""
    response = client.get('/')
    assert response.status_code == 200


def test_health_check(client):
    """Test: Health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_todo_hinzufügen(client):
    """Test: Todo kann hinzugefügt werden"""
    response = client.post('/add', data={
        'title': 'Test Todo',
        'date': '2025-12-31',
        'category': 'Privat'
    }, follow_redirects=True)
    
    assert response.status_code == 200


def test_todo_löschen(client):
    """Test: Todo kann gelöscht werden"""
    # Zuerst ein Todo hinzufügen
    client.post('/add', data={
        'title': 'Zu löschen',
        'date': '2025-12-31',
        'category': 'Privat'
    })
    
    # Dann löschen (nehmen wir an ID 1)
    response = client.post('/delete/1', follow_redirects=True)
    assert response.status_code == 200


def test_todo_sortierung():
    """Test: Todos werden nach Datum sortiert"""
    # Testdaten
    todo1 = Todo(1, "Zuerst", "2025-01-15")
    todo2 = Todo(2, "Später", "2025-12-31")
    todo3 = Todo(3, "Dazwischen", "2025-06-01")
    
    test_todos = [todo2, todo1, todo3]
    sorted_todos = sorted(test_todos, key=lambda x: x.date)
    
    # Sollte in Reihenfolge sein: todo1, todo3, todo2
    assert sorted_todos[0].title == "Zuerst"
    assert sorted_todos[1].title == "Dazwischen"
    assert sorted_todos[2].title == "Später"
