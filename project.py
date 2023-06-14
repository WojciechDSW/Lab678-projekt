import sys
import threading
import json
import xml.etree.ElementTree as ET
import yaml
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLabel, QLineEdit

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)

def read_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def write_yaml(data, file_path):
    with open(file_path, 'w') as f:
        yaml.safe_dump(data, f)

def read_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def write_xml(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path)

import json
import xmltodict
import yaml

def convert_file(input_file, output_file, output_format):
    # Wczytywanie pliku wejściowego
    with open(input_file, 'r') as file:
        if input_file.endswith('.json'):
            data = json.load(file)
        elif input_file.endswith('.xml'):
            data = xmltodict.parse(file.read())
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            data = yaml.safe_load(file)
        else:
            print('Niewspierany format pliku wejściowego.')
            return

    # Konwersja i zapis do pliku wyjściowego
    with open(output_file, 'w') as file:
        if output_format == 'json':
            json.dump(data, file, indent=4)
        elif output_format == 'xml':
            xmltodict.unparse(data, output=file)
        elif output_format == 'yml':
            yaml.dump(data, file)
        else:
            print('Niewspierany format pliku wyjściowego.')


class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.inputFileLabel = QLabel('Plik wejściowy:')
        self.inputFileLineEdit = QLineEdit()
        self.inputFileButton = QPushButton('Wybierz plik wejściowy')
        self.inputFileButton.clicked.connect(self.choose_input_file)

        self.outputFormatLabel = QLabel('Format wyjściowy:')
        self.outputFormatComboBox = QComboBox()
        self.outputFormatComboBox.addItems(['json', 'yaml', 'xml'])

        self.outputFileLabel = QLabel('Plik wyjściowy:')
        self.outputFileLineEdit = QLineEdit()
        self.outputFileButton = QPushButton('Wybierz plik wyjściowy')
        self.outputFileButton.clicked.connect(self.choose_output_file)

        self.convertButton = QPushButton('Konwertuj')
        self.convertButton.clicked.connect(self.convert)

        layout.addWidget(self.inputFileLabel)
        layout.addWidget(self.inputFileLineEdit)
        layout.addWidget(self.inputFileButton)
        layout.addWidget(self.outputFormatLabel)
        layout.addWidget(self.outputFormatComboBox)
        layout.addWidget(self.outputFileLabel)
        layout.addWidget(self.outputFileLineEdit)
        layout.addWidget(self.outputFileButton)
        layout.addWidget(self.convertButton)

        self.setLayout(layout)

    def choose_input_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy", "", "All Files (*)", options=options)
        if fileName:
            self.inputFileLineEdit.setText(fileName)

    def choose_output_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Wybierz plik wyjściowy", "", "All Files (*)", options=options)
        if fileName:
            self.outputFileLineEdit.setText(fileName)

    def convert(self):
        input_file = self.inputFileLineEdit.text()
        output_file = self.outputFileLineEdit.text()
        output_format = self.outputFormatComboBox.currentText()
        threading.Thread(target=convert_file, args=(input_file, output_file, output_format)).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConverterApp()
    converter.show()
    sys.exit(app.exec_())
