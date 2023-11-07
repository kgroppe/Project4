import os
import sys
import logging
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class classNLTKQuery:
    def textCorpusInit(self, thePath):
        engStop = stopwords.words("english")
        pnctAndEng = engStop + [',','.','?',"'",';',':',"//", "/", "*", '(',')','--',"''","``",'-', '_']
        if not os.path.isdir(thePath):
            return "Path is not a Directory"

        if not os.access(thePath, os.R_OK):
            return "Directory is not Readable"

        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*', encoding='latin-1')
            print("Processing Files:")
            print(self.Corpus.fileids())
            print("Please wait...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
            stopword = [t for t in self.tokens if t not in pnctAndEng]
            stemmer = PorterStemmer()
            self.stemmed = [stemmer.stem(w).lower() for w in stopword]
            self.pos = nltk.pos_tag(self.tokens)
            self.pos_tags = ['CC', 'CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN',
                             'NNS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS',
                             'RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT',
                             'WP','WP$','WRB']

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

    def searchWordOccurence(self):
        myWord = input("Enter Search Word:")
        if myWord:
            wordCount = self.TextCorpus.count(myWord)
            #Ask if this works as well for the code
            print(myWord+" occured: " + str(wordCount) + " times")
        else:
            print("Word Entry is Invalid")

    def generateConcordance(self):
        myWord = input("Enter word to Concord: ")
        if myWord:
            self.TextCorpus.concordance(myWord)
        else:
            print("Word Entry is Invalid")

    def generateSimilarities(self):
        myWord = input("Enter seed word: ")
        if myWord:
            self.TextCorpus.similar(myWord)
        else:
            print("Word Entry is Invalid")

    def printWordIndex(self):
        myWord = input("Find first occurrence of what Word?: ")
        if myWord:
            wordIndex = self.TextCorpus.index(myWord)
            print("First Occurence of " + myWord + " is at offset: ")
            print(wordIndex)
        else:
            print("Word Entry is Invalid")

    def printVocabulary(self):
        print("Compiling Vocabulary Frequencies")
        vocabFreqList = self.TextCorpus.vocab()
        print(vocabFreqList.items())

    def stemOccurrence(self):
        stem = input("Please enter a stem to look for: ").lower()
        if stem:
            wordCount = self.stemmed.count(stem)
            print(stem+" occured: " + str(wordCount) + " times")
        else:
            print("Word Entry is Invalid")

    def wordsWithPOS(self):
        print("Here are the 36 different POS tags:")
        print(self.pos_tags)
        found = []
        myPos = input("Enter a POS to look for: ").upper()
        if myPos:
            for word, tag in self.pos:
                if tag == myPos:
                    if word not in found:
                        found.append(word)
            if len(found) > 0:
                print(found)
            else:
                print("That POS is not in the document")
        else:
            print("POS Entry is Invalid")

    def showAllPOS(self):
        tags = []
        find = input("Enter a word to find all given POS: ").lower()
        if find:
            for word, tag in self.pos:
                if word.lower() == find:
                    if tag not in tags:
                        tags.append(tag)
            print(tags)
        else:
            print("Word Entry is Invalid")

    def showMostCommon(self):
        print("Here are the 36 different POS tags:")
        print(self.pos_tags)
        common = input("Enter a POS to find the most common word: ").upper()
        comDict = {}
        comList = []
        count = 1
        if common:
            for word, tag in self.pos:
                if tag == common:
                    if word in comDict.keys():
                        comDict[word] += 1
                    else:
                        comDict[word] = 1
            if len(comDict) > 0:
                for key, item in comDict.items():
                    comList.append((item, key))
                comList.sort(reverse=True)
                print("For the POS tag of",common, "the most common twenty words are: ")
                for item in comList[:20]:
                    print("%d. " %(count), end="")
                    print(item)
                    count += 1
            else:
                print("POS Entry is Invalid")
        else:
            print("POS Entry is Invalid")
            