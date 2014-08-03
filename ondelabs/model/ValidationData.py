'''
Created on 3 Aug 2014

@author: ankur
'''
import logging
import math

from ondelabs.model.TextClassType import TextClassType


class ValidationData:
    
    def __init__(self, lines):
        self.__lines = lines
        self.__words = {}
        self.__separateWordsInLines()
    
    def __separateWordsInLines(self):
        for line in self.__lines:
            self.__words[line] = TextClassType(line, -1)
    
    def validate(self, classes, lexicon):
        results = {}
        
        allClassTypes = classes.getAllClassTypes()
        
        for key in self.__words.keys():
            validationText = self.__words[key]
            classResult = {}
            for classTypeKey in allClassTypes:
                classType = classes.getClass(classTypeKey)
                words = validationText.getWords()
                prob = math.log(classes.getPrior(classTypeKey))
                for word in words:
                    conProb = lexicon.getConditionalProbability(word, classTypeKey)
                    if conProb != 0:
                        prob = prob + math.log(conProb)
                classResult[classTypeKey] = prob
            results[key] = self.__findClassTypeWithHighestProb(classResult)
        return results
    
    def __findClassTypeWithHighestProb(self, probs):
        bestClassType = -1
        highestProb = -9999999
        
        for key in probs.keys():
            if probs[key] > highestProb:
                highestProb = probs[key]
                bestClassType = key
        
        return bestClassType
        
        