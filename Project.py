import xml.etree.ElementTree as ET
import xmljson
import xmltodict

def save_xml(root, file_path):
    try:
        tree = ET.ElementTree(root)
        tree.write(file_path)
        print(f"Dane zapisane pomyślnie do pliku {file_path}.")
    except Exception as e:
        print(f"Wystąpił problem podczas zapisywania do pliku {file_path}: {str(e)}")

if __name__ == "__main__":
    # Stwórz korzeń drzewa.
    root = ET.Element("root")

    # Dodaj elementy do drzewa.
    child1 = ET.SubElement(root, "child1")
    child1.text = "tekst dziecka 1"
    child2 = ET.SubElement(root, "child2")
    child2.text = "tekst dziecka 2"

    # Zamień 'output.xml' na prawdziwą ścieżkę do pliku.
    save_xml(root, 'output.xml')
