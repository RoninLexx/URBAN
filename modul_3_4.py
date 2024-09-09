def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for item in other_words:
        i_l = item.lower()
        if root_word in i_l:
            same_words.append(item)
        if i_l in root_word:
            same_words.append(item)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
