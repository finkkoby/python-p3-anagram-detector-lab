# your code goes here!
import ipdb
class Anagram():
    def __init__(self, word):
        self.word = word
    def match(self, anagrams_list):
        target_char_list = sorted(list(self.word))
        answer_list = []
        for str in anagrams_list:
            anagram_char_list = sorted(list(str))
            if anagram_char_list == target_char_list:
                answer_list.append(str)
        return answer_list