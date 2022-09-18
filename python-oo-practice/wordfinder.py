"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Opens the file at the specified path, and appends all lines into a list, prints the length of that list"""

    def __init__(self, path):
        self.file = open(path)
        self.text = []
        for line in self.file:
            self.text.append(line.strip())
        print(f"{len(self.text)} words read")

    def random(self):
        """Returns a random word from the list"""
        return choice(self.text)


class SpecialWordFinder(WordFinder):
    """Extends WordFinder and implements a different random function

        >>> swf = SpecialWordFinder("words2.txt")
        9 words read

        >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
        True

        >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
        True

        >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
        True

        >>> swf.random() in ["apple", "mango", "kale", "parsnips"]
        True
        """

    def __init__(self, path):
        super().__init__(path)

    def random(self):
        """Runs forever randomly picking elements until one satisfies the conditions"""
        while True:
            word = super().random()
            if word != "" and "#" not in word:
                return word
