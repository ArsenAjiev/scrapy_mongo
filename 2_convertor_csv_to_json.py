import csv
import json
import time


def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    # read csv file
    with open(csv_file_path, encoding='utf-8') as csv_file:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csv_file)

        # convert each csv row into python dict
        for row in csv_reader:
            # add this python dict to json array
            json_array.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_array, indent=4, ensure_ascii=False)
        json_file.write(json_string)


csv_file_path = r'data.csv'
json_file_path = r'data.json'

start = time.perf_counter()
csv_to_json(csv_file_path, json_file_path)
finish = time.perf_counter()

print(f"Conversion completed successfully in {finish - start:0.4f} seconds")