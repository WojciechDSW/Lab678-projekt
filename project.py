import threading
def convert(self):
    threading.Thread(target=self.convert_file).start()

def convert_file(self):
    # Tutaj powinien znaleźć się Twój kod konwertujący pliki.
    print("Konwertuję plik...")
