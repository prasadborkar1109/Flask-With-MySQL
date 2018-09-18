# -*- coding: utf-8 -*-

import pymysql

class DBConnection(object):
    """
    Below server, port and credentials are hardcoded as default values in init but this info
    can be part of config.ini file (holds key value pair environment specific config file)
    and can be extracted using configparser lib
    """
    
    def __init__(self, host='localhost', port=3306,user='root',password='admin',db='petdb'):
        
        self.conn = pymysql.connect(host=host, port=port,
                             user=user,
                             password=password,
                             db=db)
        self.cursor = self.conn.cursor()
    
    
    def __enter__(self):
        return self.cursor
    
    def __exit__(self, type, value, traceback):
        self.cursor.close()
        if isinstance(value, Exception):
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close() 
            
