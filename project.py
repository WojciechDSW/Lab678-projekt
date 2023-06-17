import json
import yaml
import xmltodict
import tkinter as tk
from tkinter import filedialog, messagebox

def load_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def save_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def convert_yaml_to_json(yaml_content):
    data = yaml.safe_load(yaml_content)
    return json.dumps(data, indent=4)

def convert_yaml_to_xml(yaml_content):
    data = yaml.safe_load(yaml_content)
    return xmltodict.unparse(data, pretty=True)

def convert_json_to_yaml(json_content):
    data = json.loads(json_content)
    return yaml.dump(data)

def convert_json_to_xml(json_content):
    data = json.loads(json_content)
    return xmltodict.unparse(data, pretty=True)

def convert_xml_to_yaml(xml_content):
    data = xmltodict.parse(xml_content)
    return yaml.dump(data)

def convert_xml_to_json(xml_content):
    data = xmltodict.parse(xml_content)
    return json.dumps(data, indent=4)

def convert_files():
    input_file = filedialog.askopenfilename(title="Wybierz plik wejściowy")
    output_file = filedialog.asksaveasfilename(title="Zapisz plik wyjściowy", defaultextension=".txt")

    input_format = input_format_var.get()
    output_format = output_format_var.get()

    if not input_file or not output_file:
        messagebox.showerror("Błąd", "Należy wybrać plik wejściowy i plik wyjściowy.")
        return

    input_content = load_file(input_file)

    if input_format == "YAML":
        if output_format == "JSON":
            output_content = convert_yaml_to_json(input_content)
        elif output_format == "XML":
            output_content = convert_yaml_to_xml(input_content)
    elif input_format == "JSON":
        if output_format == "YAML":
            output_content = convert_json_to_yaml(input_content)
        elif output_format == "XML":
            output_content = convert_json_to_xml(input_content)
    elif input_format == "XML":
        if output_format == "YAML":
            output_content = convert_xml_to_yaml(input_content)
        elif output_format == "JSON":
            output_content = convert_xml_to_json(input_content)

    save_file(output_file, output_content)
    messagebox.showinfo("Konwersja zakończona", "Plik zapisany jako " + output_file)

# Tworzenie głównego okna
window = tk.Tk()
window.title("Konwerter plików YAML, JSON, XML")

# Tworzenie etykiet
input_label = tk.Label(window, text="Format pliku wejściowego:")
input_label.grid(row=0, column=0, padx=10, pady=10)

output_label = tk.Label(window, text="Format pliku wyjściowego:")
output_label.grid(row=1, column=0, padx=10, pady=10)

# Tworzenie list rozwijanych dla formatu wejściowego
input_format_var = tk.StringVar()
input_format_var.set("YAML")

input_format_menu = tk.OptionMenu(window, input_format_var, "YAML", "JSON", "XML")
input_format_menu.grid(row=0, column=1, padx=10, pady=10)

# Tworzenie listy rozwijanej dla formatu wyjściowego
output_format_var = tk.StringVar()
output_format_var.set("JSON")

output_format_menu = tk.OptionMenu(window, output_format_var, "YAML", "JSON", "XML")
output_format_menu.grid(row=1, column=1, padx=10, pady=10)

# Tworzenie przycisku konwersji
convert_button = tk.Button(window, text="Konwertuj", command=convert_files)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Uruchamianie pętli głównej aplikacji
window.mainloop()

