import csv


def create_csv(filename, value_list):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Age'])

        for tup in value_list:
            writer.writerow(tup)


create_csv('test.csv', [('Subin', 'Kathmandu', 20), ('Subin', 'Kathmandu', 20)])
