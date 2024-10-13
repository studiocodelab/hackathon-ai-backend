# Digital Training Manager - Backend AI

## PPPT, projekt 8

## Autorzy

<!-- <h1 style="text-align: center;">Studio CodeLab</h1>

<div style="display: flex; justify-content: space-between; width: 100%;">
  <div style="width: 25%; text-align: center;"><h1>Grzegorz Pisarczyk</h1><img style="width: 100%; border-radius: 5
0%;" src="img/pisarczyk.jpg" alt="Grzegorz Pisarczyk"/><h3>Architekt rozwiązania, UI/UX Designer</h3></div>
  <div style="width: 25%; text-align: center;"><h1>Michał Borzuchowski</h1><img style="width: 100%; border-radius:
50%;" src="img/borzuchowski.png" alt="Michał Borzuchowski"/><h3>Web/Mobile developer</h3></div>
  <div style="width: 25%; text-align: center;"><h1>Artur Borecki</h1><img style="width: 100%; border-radius: 50%;"
src="img/borecki.jpg" alt="Artur Borecki"/><h3>Python developer, AI</h3></div>
</div> -->

| Grzegorz Pisarczyk | Michał Borzuchowski | Artur Borecki |
|--------------------|---------------------|---------------|
| **Architekt rozwiązania, UI/UX Designer** | **Web/Mobile developer** | **Python developer, AI** |

## Użyte technologie

[Więcej informacji](https://stackshare.io/StudioCodeLab/city-coders-hackathon-plock-back-end)

- Programowanie:
  - JavaScript
  - Python
  - Node.js
  - MySQL
  - GraphQL
  - ES6
  - Flask
  - Apollo
- DevOps:
  - Git
  - GitHub
  - Visual Studio Code
  - npm
- Utilities:
  - Ollama

## Instalacja

1. Sklonuj repozytorium

2. Zainstaluj zależności

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```bash
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Uruchomienie

### Linux

```bash
source venv/bin/activate
flask --app rest run --host 0.0.0.0
```

### Windows

```bash
.\venv\Scripts\activate
flask --app rest run --host 0.0.0.0
```

## Użycie

### Ustawienie promptu pierwotnego (systemowego)

Plik `system_prompt.txt` zawiera prompt systemowy.

### Wygenerowanie nowego ID sesji

Zapytanie POST na `/new_session_id` z JSON-em w formacie:
```json
{
    "context": "KONTEKST (dane)"
}
```
`http://localhost:5000/new_session_id`

### Zapytanie do Ollamy

Zapytanie POST na `/chat` z JSON-em w formacie:
```json
{
    "session_id": "ID_SESJI",
    "message": "TREŚĆ_ZAPYTANIA"
}
```
ID_SESJI - ID sesji zwrócone przez `/new_session_id`

### Wrzucenie pliku do storage'u

Zapytanie POST na `/storage/push` z JSON-em w formacie:
```json
{
    "filename": "NAZWA_PLIKU",
    "data": "ZAWARTOŚĆ_PLIKU"
}
```

### Pobranie pliku z storage'u

Zapytanie POST na `/storage/pull` z JSON-em w formacie:
```json
{
    "filename": "NAZWA_PLIKU"
}
```

### Usunięcie pliku z storage'u

Zapytanie POST na `/storage/delete` z JSON-em w formacie:
```json
{
    "filename": "NAZWA_PLIKU"
}
```

### Pobranie listy plików w storage'u

Zapytanie GET na `/storage/list`

### Pobranie pliku z storage'u jako plik

Zapytanie GET na `/stored_files/NAZWA_PLIKU`
