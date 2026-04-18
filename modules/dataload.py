import csv

def load_data(filename, key, value):
    data_map = {}

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_map[row[key].lower()] = float(row[value])

    return data_map
