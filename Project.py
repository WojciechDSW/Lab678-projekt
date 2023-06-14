import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QComboBox, QLabel, QLineEdit

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
        # Tutaj powinien znaleźć się Twój kod konwertujący pliki.
        print("Konwertuję plik...")

def main():
    app = QApplication(sys.argv)
    ex = ConverterApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
