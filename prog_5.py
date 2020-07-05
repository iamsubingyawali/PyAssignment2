my_tuple = ('Subin', 'Gyawali', 20)
people = [my_tuple]

tuple_1 = ('A', 'B', 12)
people.append(tuple_1)
tuple_2 = ('C', 'D', 56)
people.append(tuple_2)
tuple_3 = ('E', 'F', 45)
people.append(tuple_3)
tuple_4 = ('G', 'H', 90)
people.append(tuple_4)

people.sort(key=lambda i: i[2])
print(people)
