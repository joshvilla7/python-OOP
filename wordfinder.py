"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """ Takes a path to a file of words and returns random 
    words from that dictionary.
    
    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True


     """

    def __init__(self, path):
        """ Accepts a path to a file of words and turns it into a list of strings """
        file = open(path)
        self.words = self.listify(file)
        print(f"{len(self.words)} words read")

    def listify(self, file):
        """ Removes extra space/new line around each word in a file and creates a list """
        return [word.strip() for word in file] 

    def random(self):
        """ Returns a random word """
        return random.choice(self.words)

    def __repr__(self):
        """ Representation of what Class is about """
        return f"WordFinder(path={self.file})"


class SpecialWordFinder(WordFinder):
    """ Subclass of WordFinder, that has improved functionality to avoid returning comments or blank spaces """

    def listify(self, file):
        """ Improved listify method to create a list of only words, avoiding comments or blank spaces """
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]

    def __repr__(self):
        return f"SpecialWordFiner(path={self.file})"