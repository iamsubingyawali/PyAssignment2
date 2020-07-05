import csv


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        csv_list = list(reader)

        data_dict = {}
        data_list = list()

        for i in range(1, len(csv_list)):
            for j in range(len(csv_list[i])):
                data_dict[csv_list[0][j]] = csv_list[i][j]
            data_list.append(data_dict)
        return data_list


print(read_csv('test.csv'))
