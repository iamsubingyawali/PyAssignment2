def match_brackets(input_string):
    open_bracs = ['[', '{', '(']
    close_bracs = [']', '}', ')']

    brac_list = []
    for i in input_string:
        if i in open_bracs:
            brac_list.append(i)
        elif i in close_bracs:
            pos = close_bracs.index(i)
            if ((len(brac_list) > 0) and
                    (open_bracs[pos] == brac_list[len(brac_list) - 1])):
                brac_list.pop()
            else:
                return False

    if len(brac_list) == 0:
        return True
    else:
        return False


print(match_brackets("({[)]"))
print(match_brackets("()[]{}"))
