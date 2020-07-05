def search(sorted_seq, item):
    if type(sorted_seq) == dict:
        seq_list = list(sorted_seq.values())
        if item in seq_list:
            return seq_list.index(item)
        else:
            return -1
    else:
        if item in sorted_seq:
            seq_list = list(sorted_seq)
            return seq_list.index(item)
        else:
            return -1


seq = ['a', 'b', 'c', 1, 2, 3]

print(search(seq, 'c'))
