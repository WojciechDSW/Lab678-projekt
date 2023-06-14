import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Konwersja danych między formatami: .xml, .json i .yml (.yaml)")

    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")

    args = parser.parse_args()
    return args.input_file, args.output_file

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    print(f"Plik wejściowy: {input_file}, Plik wyjściowy: {output_file}")
