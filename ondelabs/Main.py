'''
Created on 3 Aug 2014

@author: ankur
'''
'''2) Load Data '''
'''3) Train '''
'''4) Save Model '''
'''5) Test Model Accuracy '''

import logging

from ondelabs.dao.DiskTrainingDAO import DiskTrainingDAO
from ondelabs.dao.DiskValidationDAO import DiskValidationDAO
from ondelabs.model.TrainingData import TrainingData


def main():
    trainingData = TrainingData.deserialize()
    
    if trainingData is None:
        trainingDAO = DiskTrainingDAO('resource/training.txt')
        trainingData = trainingDAO.loadData()
        trainingData.train()
        trainingData.serialize()
    
    logging.info('Training has completed')
    
    validationDAO = DiskValidationDAO('resource/validation.txt')
    validationData = validationDAO.loadData()
    validationResult = validationData.validate(trainingData.getClasses(), trainingData.getLexicon())
    
    logging.info('Validation has completed')
    

main()