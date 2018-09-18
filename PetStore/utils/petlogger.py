# -*- coding: utf-8 -*-
"""
We can have different log format and diferent log file for each log level.

"""

import logging
import datetime
from root import ROOT_PATH

def getLogger(moduleName):
    logger = logging.getLogger(moduleName)
    formatter = logging.Formatter('%(asctime)s | %(name)-12s | %(levelname)-8s  %(message)s')
    logFilePath = ROOT_PATH + '\\pet_' + datetime.date.today().isoformat() + '.log'
    fileHandler = logging.FileHandler(logFilePath)
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    
    logger.setLevel(logging.INFO)
    return logger
    