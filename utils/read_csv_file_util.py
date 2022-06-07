import csv


def read_csv_file(file_path):
    test_data = []
    with open(file_path, newline='') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        # skip header row
        next(data)
        for row in data:
            test_data.append(tuple(row))

    return test_data
