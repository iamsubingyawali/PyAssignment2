def cut_extension(filename):
    length = len(filename)
    dot_index = filename.index('.')
    sliced_name = filename[slice(dot_index - length)]
    return sliced_name


print(cut_extension("dksfhksdh.xlxs"))

# This code works for extensions with any length
