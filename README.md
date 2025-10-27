# 📝 Todo App - M324 LB Projekt

Einfache Todo-Verwaltungs-App für die Modulabschlussprüfung M324.

## 🚀 Quick Start

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

## 📁 Projektstruktur
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

## 🎯 Features

- ✅ Todo erstellen mit Titel, Datum und Kategorie
- ✅ Todos nach Datum sortiert anzeigen
- ✅ Todos löschen
- ✅ Kategorien (Arbeit, Privat, Schule)
- ✅ Automatische Tests
- ✅ CI/CD Pipeline

## 🔧 Für LB benötigte Schritte

### A1: Anforderungsverwaltung
1. GitHub Issues erstellen:
   - "Als User möchte ich Todos erstellen"
   - "Als User möchte ich Todos löschen"
   - "Als User möchte ich Todos nach Datum sortiert sehen"
2. Labels erstellen: `feature`, `bug`, `priority-high`, `priority-low`
3. Screenshot machen

### B1: Entwicklungsumgebung
1. Pre-commit hooks aktivieren: `pre-commit install`
2. Virtual Environment aktivieren
3. Screenshot vom Terminal machen

### C1: Versionsverwaltung
1. Feature Branch erstellen: `git checkout -b feature/add-categories`
2. Änderung machen
3. Pull Request erstellen
4. Merge
5. Screenshot machen

### D1: Continuous Integration
1. `.github/workflows/ci.yml` in Repo hochladen
2. Push machen
3. GitHub Actions laufen automatisch
4. Screenshot von grünem Haken machen

### E1: Continuous Deployment
1. Azure App Service erstellen
2. Publish Profile als GitHub Secret speichern
3. CD Workflow hinzufügen
4. Bei Push wird automatisch deployed
5. Screenshot von laufender App

## 📸 Benötigte Screenshots

1. ✅ GitHub Issues mit Labels
2. ✅ Pull Request
3. ✅ GitHub Actions (grün)
4. ✅ GitHub Release (v1.0.0)
5. ✅ Terminal mit aktiviertem venv
6. ✅ App läuft lokal (Browser)
7. ✅ App deployed auf Azure

## 🏷️ Release erstellen
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Dann auf GitHub: Releases → Draft new release → v1.0.0

## 📝 Lizenz
MIT

## CI/CD Pipeline
Automatische Tests laufen bei jedem Push.
