'''
Created on 3 Aug 2014

@author: ankur
'''
import pickle
import os.path


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
    
    def serialize(self):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        resource_path = os.path.join(currentDir, "../../../resource/model.pik")
        pickleFile = file(resource_path, "w")
        pickle.dump(self, pickleFile, 1)
    
    @staticmethod
    def deserialize():
        currentDir = os.path.dirname(os.path.realpath(__file__))
        resource_path = os.path.join(currentDir, "../../../resource/model.pik")
        if os.path.isfile(resource_path):
            pickleFile = file(resource_path, "r")
            return pickle.load(pickleFile)
        return None
    