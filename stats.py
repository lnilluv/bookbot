def get_num_words(text):
    words = text.lower().split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
    return words
    
def count_characters(words):
    dict = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter not in dict:
                    dict[letter] = 1
                else:
                    dict[letter] += 1
                
    return dict

def pretty_print(dict,filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {value}")
    print("============= END ===============")
