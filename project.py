import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        print(f"Dane z pliku {file_path} wczytane pomyślnie.")
        return data
    except yaml.YAMLError:
        print(f"Błąd składni YAML w pliku {file_path}.")
        return None
    except Exception as e:
        print(f"Wystąpił problem podczas wczytywania pliku {file_path}: {str(e)}")
        return None

if __name__ == "__main__":
    # Zamień 'input.yml' na prawdziwą ścieżkę do pliku.
    data = load_yaml('input.yml')
