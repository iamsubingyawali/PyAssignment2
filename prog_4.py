names = []
print("Empty List Id: ", id(names))
print(names)

names.append('Subin')
names.append('John')
names.append('Tina')
names.append('Brad')
names.append('Nolan')

print("\nFilled List Id: ", id(names))
print(names)

names.sort()

print("\nSorted List Id: ", id(names))
print(names)

# No, Id of the list didn't change while appending elements as well as after sorting the list
