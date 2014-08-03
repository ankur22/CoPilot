'''
Created on 3 Aug 2014

@author: ankur
'''

class TrainingData:
    
    def __init__(self, lexicon, classes, numberOfLines):
        self.__lexicon = lexicon
        self.__classes = classes
        self.__numberOfLines = numberOfLines
    
    def train(self):
        self.__classes.calculatePrior()
        self.__lexicon.calculateConditionalProbability(self.__classes)
    
    def getClasses(self):
        return self.__classes
    
    def getLexicon(self):
        return self.__lexicon
        