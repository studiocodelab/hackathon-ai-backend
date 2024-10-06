# ollama_python_api
API dla Ollama ze wsparciem (pseudo)sesji

## Wymagania

- Python 3
- Flask
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

Zapytanie POST na `/new_session_id`
`http://localhost:5000/new_session_id`

### Zapytanie do Ollamy

Zapytanie POST na `/ollama` z JSON-em w formacie:
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
