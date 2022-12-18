# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        self_map_word = self.map_word(self.word)
        matching_words = []
        print("This is the map word", self_map_word)
        for word in list:
            if Anagram.map_word(self, word) == self_map_word:
                matching_words.append(word)

        return matching_words
                

    def map_word(self, word):
        map = {}
        for letter in word: 
            if letter in map.keys():
                map[letter] += 1
            else:
                map[letter] = 1
        return map


                





                

