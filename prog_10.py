def change_case(camel_case_string, separator):
    letter_list = list(camel_case_string)
    new_string = letter_list[0]
    for i in range(1, len(letter_list)):
        if letter_list[i].isupper():
            new_string += (separator + letter_list[i])
        else:
            new_string += letter_list[i]
    return new_string.lower()


print(change_case("ThisIsCamelCased", '_'))
