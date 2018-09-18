# -*- coding: utf-8 -*-
"""

This service acts as a base service and services for different components 
can be segregated as views and register using Blueprint.
It also helps to easily authenticate or authorize based on permissions before 
redirecting to actual endpoint
"""

from flask import Flask
from flasgger import Swagger


app = Flask(__name__)

from services.views.readservice import readService
from services.views.loadservice import loadService

app.register_blueprint(readService, url_prefix='/petservice/readService')
app.register_blueprint(loadService, url_prefix='/petservice/loadService')

swag = Swagger(app=app)
