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


def main():
    trainingDAO = DiskTrainingDAO('resource/training.txt')
    trainingData = trainingDAO.loadData()
    trainingData.train()
    
    logging.info('Training has completed')
    
    validationDAO = DiskValidationDAO('resource/validation.txt')
    validationData = validationDAO.loadData()
    result = validationData.validate(trainingData.getClasses(), trainingData.getLexicon())
    
    logging.info('Validation has completed')
    

main()