# Todo App - M324 LB Projekt

Einfache Todo-Verwaltungs-App für die Modulabschlussprüfung M324.

## Quick Start

### 1. Repository auf GitHub erstellen
```bash
# Auf GitHub: Neues Repository "m324-todo-app" erstellen
# Dann lokal:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/IHR-USERNAME/m324-todo-app.git
git push -u origin main
```

### 2. Lokal ausführen
```bash
# Virtual Environment erstellen
python -m venv venv

# Aktivieren
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Dependencies installieren
pip install -r requirements.txt

# App starten
python app.py
```

App läuft auf: http://localhost:5000

### 3. Tests ausführen
```bash
pytest
```

### 4. Pre-commit Hooks einrichten
```bash
pip install pre-commit
pre-commit install
```

## Projektstruktur
```
m324-todo-app/
├── app.py                      # Hauptapplikation
├── test_app.py                 # Tests
├── requirements.txt            # Dependencies
├── .gitignore                  # Git Ignores
├── .pre-commit-config.yaml     # Pre-commit Hooks
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions CI
```


## 📝 Lizenz
MIT
