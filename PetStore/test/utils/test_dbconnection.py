# -*- coding: utf-8 -*-

import unittest
import pymysql
from utils.dbconnection import DBConnection

class Test_DBConnection(unittest.TestCase):
    
    def setUp(self):
        print('setup called')
    
    def test_connection(self):
        """
        Test if Database is getting connected successfully with correct credentials
        """
        with DBConnection() as cursor:
            cursor.execute("SELECT VERSION()")
            result = cursor.fetchone()
            self.assertIsNotNone(result)
        
    def test_connection2(self):
        """
        Test DB connection with incorrect credentials
        """
        with self.assertRaises(pymysql.err.OperationalError):
            DBConnection(password='xyz')


if __name__=='__main__':
    unittest.main()