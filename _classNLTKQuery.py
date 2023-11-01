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