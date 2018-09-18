# -*- coding: utf-8 -*-
"""
This module act as layer to between services and DB 
    We can have different different components like inputdatacomponent, 
    outputdatacomponent etc etc
"""
import pymysql
from utils.dbconnection import DBConnection
from utils.petlogger import getLogger

logger = getLogger(__name__)

class DataComponent(object):
    
    def getAllPetsData(self):
        """
        Queries are hardcoded here but can be part of properties or queies.ini file
        and data from this file can be fetched using configparser lib
        """
        try:
            logger.info('getAllPetsData method called')
            finaldata = []
            query = "select id, name, species, gender, DATE_FORMAT(birthday,'%Y-%m-%d') from petdb.pets"
            logger.info(query)
            with DBConnection() as dbcursor:
                dbcursor.execute(query)
                result_set = dbcursor.fetchall()
                for row in result_set:
                    data = {}
                    data['id'] = row[0]
                    data['name'] = row[1]
                    data['species'] = row[2]
                    data['gender'] = row[3]
                    data['birthday'] = row[4]
                    finaldata.append(data)
        
        except pymysql.err.OperationalError as e:
            logger.error(e, exc_info=True)
            raise(Exception('MySQL DB connection error:'+str(e)))
        except Exception as e:
            logger.error(e, exc_info=True)
            raise(e)
            
        print(finaldata) 
        logger.info(finaldata)
        return finaldata
    
    def updateData(self, data):
        responseMsg = ""
        try:
            with DBConnection() as dbcursor:
                query = "update petdb.pets set name='{0}', species='{1}', gender='{2}', birthday=STR_TO_DATE('{3}','%Y-%m-%d') where id={4}".format(data.get('name'),data.get('species'),data.get('gender'),data.get('birthday'),data.get('id'))
                logger.info(query)
                out = dbcursor.execute(query)
                if out > 0:
                    responseMsg =  'Data Updated Successfully'
                else:
                    responseMsg =  'No records updated, please check input'
        except pymysql.err.OperationalError as e:
            logger.error(e, exc_info=True)
            raise(Exception('MySQL DB connection error:'+str(e)))
        except Exception as e:
            logger.error(e, exc_info=True)
            raise(e)
        return responseMsg
            

if __name__=='__main__':
    comp = DataComponent()
    comp.getAllPetsData()
    data = {"id": 1, "name": "Tiger2", "species": "dog", "gender": "m", "birthday": "2016-12-12"}
    comp.updateData(data)
        
        
    
    