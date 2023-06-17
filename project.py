import sys
import threading
import json
import xml.etree.ElementTree as ET
import yaml
import xmljson
import xmltodict
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
    with open(file_path, 'r') as f:
        return xmltodict.parse(f.read())

def write_xml(data, file_path):
    with open(file_path, 'w') as f:
        f.write(xmltodict.unparse(data))

def convert_file(input_file, output_file, output_format):
    # Określenie formatu pliku wejściowego
    if input_file.endswith('.json'):
        data = read_json(input_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        data = read_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = read_xml(input_file)
    else:
        print('Nieobsługiwany format pliku wejściowego.')
        return

    # Określenie formatu pliku wyjściowego
    if output_format == 'json':
        write_json(data, output_file)
    elif output_format == 'yaml':
        write_yaml(data, output_file)
    elif output_format == 'xml':
        write_xml(data, output_file)
    else:
        print('Nieobsługiwany format pliku wyjściowego.')
        return



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
        self.outputFileButton = QPushButton('Wybierz ścieżkę docelową pliku')
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
        fileName, _ = QFileDialog.getSaveFileName(self, "Wybierz lokalizacje pliku", "", "All Files (*)", options=options)
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

