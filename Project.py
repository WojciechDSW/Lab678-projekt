import xml.etree.ElementTree as ET
import xmljson
import xmltodict

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print(f"Dane z pliku {file_path} wczytane pomyślnie.")
        return root
    except ET.ParseError:
        print(f"Błąd składni XML w pliku {file_path}.")
        return None
    except Exception as e:
        print(f"Wystąpił problem podczas wczytywania pliku {file_path}: {str(e)}")
        return None

if __name__ == "__main__":
    # Zamień 'input.xml' na prawdziwą ścieżkę do pliku.
    root = load_xml('input.xml')
