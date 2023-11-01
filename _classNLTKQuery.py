import os
import sys
import logging
import nltk
from nltk.corpus import PlaintextCorpusReader

class classNLTKQuery:
    def textCorpusInit(self, thePath):
        if not os.path.isdir(thePath):
            return "Path is not a Directory"

        if not os.access(thePath, os.R_OK):
            return "Directory is not Readable"

        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print("Processing Files:")
            print(self.Corpus.fileids())
            print("Please wait...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
        except:
            return "Corpus Creation Failed"
        self.ActivateTextCorpus = True
        return "Success"
    def printCorpusLength(self):
        print("Corpus Text Length: ")
        print(len(self.rawText))

    def printTokensFound(self):
        print("Tokens Found: ")
        print(len(self.tokens))

    def printVocabSize(self):
        print("Calculating...")
        print("Vocabulary Size: ")
        vocabularyUsed = set(self.TextCorpus)
        vocabularySize = len(vocabularyUsed)
        print(vocabularySize)

    def printSortedVocab(self):
        print("Compiling...")
        print("Sorted Vocabulary")
        print(sorted(set(self.TextCorpus)))

    def printCollocation(self):
        print("Compiling Collocations...")
        #Ask Dr. Perry about this, whether it should be in a print statement or not.
        print(self.TextCorpus.collocations())

