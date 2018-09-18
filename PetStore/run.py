# -*- coding: utf-8 -*-
"""
This module is use to run the flask app locally

"""

from services.petservice import app
app.run(host='0.0.0.0', debug=True)