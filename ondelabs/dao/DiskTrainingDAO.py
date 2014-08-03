'''
Created on 3 Aug 2014

@author: ankur
'''
import logging

from ondelabs.dao.DiskDAO import DiskDAO
from ondelabs.model.Classes import Classes
from ondelabs.model.Lexicon import Lexicon
from ondelabs.model.TextClassType import TextClassType
from ondelabs.model.TrainingData import TrainingData


class DiskTrainingDAO(DiskDAO):
    
    def __init__(self, filename):
        super(DiskTrainingDAO, self).__init__(filename)
    
    def loadData(self):
        lexicon = Lexicon()
        classes = Classes()
        numberOfLines = 0
        
        lines = self._getLinesFromFile()

        for line in lines:
            textClassType = self.__separateTextAndClassType(line)
            if textClassType is not None:
                classType = textClassType.getClassType()
                if self.__isInt(classType) is False:
                    logging.warn('classType is not an int')
                    continue
                classType = int(classType)
                lexicon.addWords(textClassType.getWords(), classType)
                classes.addClass(classType, len(textClassType.getWords()))
                numberOfLines = numberOfLines + 1
        
        return TrainingData(lexicon, classes, numberOfLines)
    
    def __separateTextAndClassType(self, line):
        index = line.rfind(' ')
        if index is -1:
            logging.warn('Could not find valid class type in ' + line)
            return None
        else:
            return TextClassType(line[:index], line[index:])

    def __isInt(self, text):
        try:
            int(text)
            return True
        except ValueError:
            return False
    