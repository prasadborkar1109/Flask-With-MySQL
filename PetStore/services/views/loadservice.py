# -*- coding: utf-8 -*-

import json
from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from component.datacomponent import DataComponent
from utils.petlogger import getLogger

logger = getLogger(__name__)

loadService = Blueprint('loadService',__name__)

    
@loadService.route('/updatePetsData', methods=['POST'])
@swag_from('updatepet.yml', methods=['POST'])
def updatePetsData():
    """
    This POST service updates Pet data based on id
    Input data json: {
        "id": 1,
        "name": "Tiger2",
        "species": "dog",
        "gender": "m",
        "birthday": "2016-12-12"
    }
    """
    logger.info('updatePetsData service called')
    resultData = None
    try:
        data = request.get_json()
        logger.info(data)
        if data:
            comp = DataComponent()
            resultData = comp.updateData(data)
    except Exception as e:
        logger.error(e, exc_info=True)
        return jsonify({'PetServiceException: '+str(e)})
    
    return json.dumps(resultData, indent=4, separators=(',',': '))