'''
Created on 3 Aug 2014

@author: ankur
'''

from ondelabs.dao.DiskDAO import DiskDAO
from ondelabs.model.ValidationData import ValidationData


class DiskValidationDAO(DiskDAO):
    
    def __init__(self, filename):
        super(DiskValidationDAO, self).__init__(filename)
    
    def loadData(self):
        lines = self._getLinesFromFile()
        return ValidationData(lines)
    