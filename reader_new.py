import sys
import csv
import json
import os
import pickle


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        raise NotImplementedError

    def save_file(self, data):
        raise NotImplementedError

    def print_data(self, data):
        for line in data:
            print(','.join(map(str, line)))


class CSVHandler(FileHandler):
    def read_file(self):
        data = []
        with open(self.file_path, newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                data.append(line)
        return data

    def save_file(self, data):
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)


class JSONHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data

    def save_file(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)


class TXTHandler(FileHandler):
    def read_file(self):
        data = []
        with open(self.file_path, 'r') as f:
            for line in f:
                data.append(line.strip().split(','))
        return data

    def save_file(self, data):
        with open(self.file_path, 'w') as f:
            for line in data:
                f.write(','.join(map(str, line)) + '\n')


class PickleHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, 'rb') as f:
            data = pickle.load(f)
        return data

    def save_file(self, data):
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)


def get_file_handler(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext == '.csv':
        return CSVHandler(file_path)
    elif ext == '.json':
        return JSONHandler(file_path)
    elif ext == '.txt':
        return TXTHandler(file_path)
    elif ext == '.pickle':
        return PickleHandler(file_path)
    else:
        raise ValueError(f'Nieprawidlowy format pliku wyjsciowego: {ext}')


def apply_changes(data, changes):
    print('=' * 20)
    print('Zmiany:')
    all_changes_invalid = True
    for change in changes:
        print(change)
        x, y, value = change.split(',')
        x_valid = y_valid = False
        try:
            x = int(x)
            if 0 <= x < len(data[0]):
                x_valid = True
            else:
                print(f'Nieprawidlowa wartosc x: {x}.')
        except ValueError:
            print(f'Nieprawidlowa wartosc x: {x}.')

        try:
            y = int(y)
            if 0 <= y < len(data):
                y_valid = True
            else:
                print(f'Nieprawidlowa wartosc y: {y}.')
        except ValueError:
            print(f'Nieprawidlowa wartosc y: {y}.')

        if x_valid and y_valid:
            all_changes_invalid = False
            data[y][x] = value

    if all_changes_invalid:
        print('Brak poprawnych argumentow, zmiany nie zostana wprowadzone.')
        sys.exit()

    return data


def main():
    if len(sys.argv) < 4:
        print('Za malo argumentow.')
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    try:
        input_handler = get_file_handler(input_file)
        data = input_handler.read_file()
    except FileNotFoundError:
        print('Nieprawidlowy plik wejsciowy.')
        return
    except ValueError as e:
        print(e)
        return

    try:
        output_handler = get_file_handler(output_file)
    except ValueError as e:
        print(e)
        return

    print('=' * 20)
    print(f'Z pliku {input_file}:')
    input_handler.print_data(data)

    data = apply_changes(data, changes)

    output_handler.save_file(data)

    print('=' * 20)
    print(f'Do pliku {output_file}:')
    output_handler.print_data(data)
    print('=' * 20)


if __name__ == '__main__':
    main()
