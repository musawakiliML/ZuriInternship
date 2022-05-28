def anagrams(word_1, word_2):
    word_1_list = list(word_1.lower())
    word_2_list = list(word_2.lower())

    for i in word_1_list:
        if i == " ":
            word_1_list.remove(i)
    for v in word_2_list:
        if v == " ":
            word_2_list.remove(v)

    word_1_list = sorted(word_1_list)
    word_2_list = sorted(word_2_list)

    if word_2_list == word_1_list:
        print("Anagrams")
    else:
        print("Not Anagrams")
    return [word_1_list, word_2_list]


# test_1 = anagrams("Heavy rain", "Hire a navy") => Anagram
# test_2 = anagrams("Eleven plus two", "Twelve plus one") => Anagram
test_words = anagrams("secure", "rescue")
# print(test_1)
# print(test_2)
print(test_words)
