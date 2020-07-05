friends = ['Subin', 'Brad', 'Nolan', 'Tina', 'Ram']


def search(name):
    found = False
    for names in friends:
        if names == name:
            found = True
            break
        else:
            found = False

    if found:
        return name + ' is in the list'
    else:
        return 'Not found'


input_name = input("Enter the name to search: ")
print(search(input_name))
