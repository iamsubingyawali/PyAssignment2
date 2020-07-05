import json

my_dict = {
    'name': 'Subin',
    'age': 20
}

print(my_dict)
print(type(my_dict))

my_json = json.dumps(my_dict)

print(my_json)
print(type(my_json))

my_converted_dict = json.loads(my_json)
print(my_converted_dict)
print(type(my_converted_dict))
