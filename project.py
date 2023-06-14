import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f"Dane z pliku {file_path} wczytane pomyślnie.")
        return data
    except json.JSONDecodeError:
        print(f"Błąd składni JSON w pliku {file_path}.")
        return None
    except Exception as e:
        print(f"Wystąpił problem podczas wczytywania pliku {file_path}: {str(e)}")
        return None

if __name__ == "__main__":
    # Zamień 'input.json' na prawdziwą ścieżkę do pliku.
    data = load_json('input.json')
