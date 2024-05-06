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
    print("Zmiany:")
    for change in changes:
        print(change)
        x, y, value = change.split(',')
        x = int(x)
        y = int(y)
        data[int(y)][int(x)] = value


def save_file(output_file, data):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    data = read_file(input_file)
    make_changes(data, changes)
    save_file(output_file, data)

    print(20 * '=')
    print(f"Do pliku {output_file}:")
    for line in data:
        print(','.join(line))
    print(20 * '=')


if main() == '__main__':
    main()

# python reader_func.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
