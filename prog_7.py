people = [('A', 'B', 12), ('C', 'D', 56), ('E', 'F', None), ('G', 'H', 90), ('I', 'J', 67)]
avg = 0
for tup in people:
    if tup[2] is not None:
        avg += tup[2]
avg = avg / len(people)


for person in people:
    if person[2] is not None:
        if person[2] > avg:
            print(person[0], " is old.")
        else:
            print(person[0], " is young.")
