import sys
import csv


def read_file(input_file):
    data = []
    print(20 * '=')
    print(f'Z pliku {input_file}:')
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
            print(','.join(line))
    return data


def make_changes(data, changes):
    print(20 * '=')
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


def save_file(output_file, data):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main():
    if len(sys.argv) < 4:
        print('Za malo argumentow.')
        return

    input_file = sys.argv[1]
    if input_file != 'in.csv':
        print('Nieprawidlowy plik wejsciowy.')
        return

    output_file = sys.argv[2]
    if not output_file.endswith('.csv'):
        print('Nieprawidlowy plik wyjsciowy.')
        return

    changes = sys.argv[3:]

    data = read_file(input_file)
    make_changes(data, changes)
    save_file(output_file, data)

    print(20 * '=')
    print(f'Do pliku {output_file}:')
    for line in data:
        print(','.join(line))
    print(20 * '=')


if main() == '__main__':
    main()

# python reader_corrected-2.py in.csv out-2.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
