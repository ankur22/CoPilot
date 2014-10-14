'''
Created on 14 Oct 2014

@author: ankur
'''


class TestLine:

    def __init__(self, originalLine, textClassType):
        self.__originalLine = originalLine
        self.__textClassType = textClassType

    def getOriginalLine(self):
        return self.__originalLine

    def getTextClassType(self):
        return self.__textClassType
