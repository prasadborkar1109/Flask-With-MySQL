# -*- coding: utf-8 -*-
"""
Views can be created based on different modules. Here I have segregated based on
 user permissions example if any user is just having access to read data and don't 
 have permissions to upload or post data.
 So readservices will only hold GET calls
"""

import json
from flask import Blueprint, jsonify
from flasgger.utils import swag_from
from component.datacomponent import DataComponent
from utils.petlogger import getLogger

readService = Blueprint('readService',__name__)
logger = getLogger(__name__)


@readService.route('/getAllPetsData', methods=['GET'])
@swag_from('allpets.yml', methods=['GET'])
def getAllPetsData():
    """
    This GET service fetches all pets data
    """
    try:
        comp = DataComponent()
        resultData = comp.getAllPetsData()
    except Exception as e:
        logger.error(e, exc_info=True)
        return jsonify({'PetServiceException: '+str(e)})
    
    return json.dumps(resultData, indent=4, separators=(',',': '))