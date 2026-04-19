import csv

def load_data(filename, key, value):
    data_map = {} #empty dictionary
    with open(f'data/{filename}', encoding="utf-8") as file: #used + adjusted from degrees32_lib.py
        reader = csv.DictReader(file)
        for row in reader:
            type= row[key].lower() #type of activity (lowercased so cap doesnt impact)
            data_map[type] = float(row[value]) #grabs the value as the value pair to the key
    return data_map
