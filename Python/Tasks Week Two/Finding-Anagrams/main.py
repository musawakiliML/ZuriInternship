# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
def find_anagram(word, anagram):
    word_list = list(word.lower())
    anagram_list = list(anagram.lower())

    word_list = sorted(word_list)
    anagram_list = sorted(anagram_list)

    if word_list == anagram_list:
        return True
    else:
        return False


find_anagram("hello", "check")
find_anagram("below", "elbow")
