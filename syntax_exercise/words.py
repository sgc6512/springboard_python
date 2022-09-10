# Print out each word on a separate line, in all uppercase
def print_upper_words(words):
    for word in words:
        print(word.upper())
    return


# Previous function but only prints words that start with 'e'
def print_upper_words_v2(words):
    for word in words:
        if word.startswith("e"):
            print(word.upper())
    return


# Print only words that start with the passed letters
def print_upper_words_v3(words, letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
    return


print_upper_words(["hello", "test", "testing", "hi"])
print_upper_words_v2(["hello", "egg", "testing", "enervate"])
print_upper_words_v3(["apple", "boy", "cost", "dog"], ["a", "b"])
