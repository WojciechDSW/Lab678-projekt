import yaml

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
        print(f"Dane zapisane pomyślnie do pliku {file_path}.")
    except Exception as e:
        print(f"Wystąpił problem podczas zapisywania do pliku {file_path}: {str(e)}")

if __name__ == "__main__":
    data = {"klucz": "wartość"}  # Zamień to na prawdziwe dane, które chcesz zapisać.
    # Zamień 'output.yml' na prawdziwą ścieżkę do pliku.
    save_yaml(data, 'output.yml')
