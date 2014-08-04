'''
Created on 3 Aug 2014

@author: ankur
'''

import logging

from ondelabs.dao.DiskDAO import DiskDAO
from ondelabs.model.TextClassType import TextClassType
from ondelabs.model.ValidationData import ValidationData


class DiskValidationDAO(DiskDAO):
    
    def __init__(self, filename):
        super(DiskValidationDAO, self).__init__(filename)
    
    def loadData(self):
        result = {}
        lines = self._getLinesFromFile()

        for line in lines:
            textClassType = self.__separateTextAndClassType(line)
            if textClassType is not None:
                result[line] = textClassType
        
        return ValidationData(result)
    
    def __separateTextAndClassType(self, line):
        index = line.rfind(' ')
        if index is -1:
            logging.warn('Could not find valid class type in ' + line)
            return None
        else:
            if self.__isInt(line[index:]) is False:
                logging.warn('classType is not an int')
                return None
            else:
                return TextClassType(line[:index], int(line[index:]))

    def __isInt(self, text):
        try:
            int(text)
            return True
        except ValueError:
            return False
