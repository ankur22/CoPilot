'''
Created on 3 Aug 2014

@author: ankur
'''
from ondelabs.dao.BaseDAO import BaseDAO


class DiskDAO(BaseDAO):
    
    def __init__(self, filename):
        self.__filename = filename
    
    def loadData(self):
        raise NotImplementedError( "Should implemented this" )
    
    def _getLinesFromFile(self):
        f = open(self.__filename)
        lines = f.readlines()
        f.close()
        return lines
    