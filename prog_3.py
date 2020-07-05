def find_anagrams(sentence):
    sorted_dict = {}
    anagram_list = []
    added_keys = []
    input_words = sentence.split()
    for words in input_words:
        new_word = ''.join(sorted(words.lower()))
        sorted_dict[words] = new_word

    for key in input_words:
        word_set = set()
        for key2 in input_words:
            if key == key2:
                continue
            elif key in added_keys:
                continue
            else:
                if sorted_dict[key] == sorted_dict[key2]:
                    added_keys.append(key2)
                    word_set.add(key)
                    word_set.add(key2)
        if len(word_set) > 0:
            anagram_list.append(word_set)
    return anagram_list


input_sent = input("Enter Sentence: ")
print(find_anagrams(input_sent))
