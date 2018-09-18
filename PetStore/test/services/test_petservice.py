# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:39:54 2018

@author: Prasad
"""

import unittest
from services.petservice import app
import json
from unittest.mock import patch, MagicMock, Mock

class Test_PetService(unittest.TestCase):
    
    def setUp(self):
        print('setup called')
        self.test_app = app.test_client()
    
    def tearDown(self):
        print('delete/close any resources')
    
    def getMockPetsData(self):
        return ((1, 'Tommy', 'dog', 'm', '2017-10-12'), (2, 'Sweetu', 'cat', 'w', '2015-01-31'))
        
    
    @patch('utils.dbconnection.pymysql')
    def test_getAllPetsData(self, mock_pymysql):
        """
        Here we are trying to test the service, so mocking up the DB calls or
        any other IO calls
        DB connection can be tested as part of itegration tests
        """
        conn = Mock()
        mock_pymysql.connect.return_value = conn
    
        cursor = MagicMock()
        mockResult = MagicMock()
        cursor.__enter__.return_value = mockResult
        cursor.__exit___ = MagicMock()
    
        # Below commands set the return values for commands executed 
        # in datacomponent
        conn.cursor.return_value = cursor
        cursor.execute.return_value = True
        cursor.fetchall.return_value = self.getMockPetsData()
        
        resp = self.test_app.get('/petservice/readService/getAllPetsData')
        self.assertEqual(resp.status_code,200)
    
    def test_loadPetsData(self):
        inputJson = {"id": 1,"name": "Tiger", "species": "dog","gender": "m","birthday": "2016-12-12"}
        resp = self.test_app.post('/petservice/loadService/updatePetsData', data=json.dumps(inputJson))
        self.assertEqual(resp.status_code,200)

if __name__=='__main__':
    unittest.main()
        
