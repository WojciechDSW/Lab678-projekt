import sys
import json
import yaml
import xml.etree.ElementTree as ET
from xmljson import badgerfish as bf
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLabel, QLineEdit
import threading


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def load_xml(file_path):
    tree = ET.parse(file_path)
    return bf.data(tree.getroot())

def save_xml(data, file_path):
    root = bf.etree(data)
    tree = ET.ElementTree(root)
    tree.write(file_path)

def convert_file(input_file, output_file, output_format):
    data = None
    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)

    if data is not None:
        if output_format == 'json':
            save_json(data, output_file)
        elif output_format == 'yaml':
            save_yaml(data, output_file)
        elif output_format == 'xml':
            save_xml(data, output_file)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.inputFileLineEdit = QLineEdit()
        self.inputFileButton = QPushButton('Wybierz plik wejściowy')
        self.inputFileButton.clicked.connect(self.choose_input_file)

        self.outputFormatComboBox = QComboBox()
        self.outputFormatComboBox.addItems(['json', 'yaml', 'xml'])

        self.outputFileLineEdit = QLineEdit()
        self.outputFileButton = QPushButton('Wybierz ścieżkę docelową pliku')
        self.outputFileButton.clicked.connect(self.choose_output_file)

        self.convertButton = QPushButton('Konwertuj')
        self.convertButton.clicked.connect(self.convert)

        layout.addWidget(QLabel('Plik wejściowy:'))
        layout.addWidget(self.inputFileLineEdit)
        layout.addWidget(self.inputFileButton)
        layout.addWidget(QLabel('Format wyjściowy:'))
        layout.addWidget(self.outputFormatComboBox)
        layout.addWidget(QLabel('Plik wyjściowy:'))
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
        fileName, _ = QFileDialog.getSaveFileName(self, "Wybierz ścieżkę docelową", "", "All Files (*)", options=options)
        if fileName:
            self.outputFileLineEdit.setText(fileName)

    def convert(self):
        threading.Thread(target=self.thread_convert).start()

    def thread_convert(self):
        input_file = self.inputFileLineEdit.text()
        output_file = self.outputFileLineEdit.text()
        output_format = self.outputFormatComboBox.currentText()

        if not input_file or not output_file:
            print("Wybierz plik wejściowy i plik wyjściowy.")
            return

        convert_file(input_file, output_file, output_format)

        print("Konwersja zakończona.")


def main():
    app = QApplication(sys.argv)
    ex = ConverterApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
