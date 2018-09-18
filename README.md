# Flask PetStore Application:


Instructions:

1. Installation:
This application requires below libs apart from core python:

command:    pip install -r requirements.txt


    1. PyMySQL - to hold pets data
    2. flasgger - used flasgger for swagger api documentation instead of (http://swagger.io/specification/)
    3. Also flask version 0.12.2 as latest version is having some issues


2. Execute run.py file which runs the flask app locally, once it is started then run below swagger url in browser to
   open the api documentation

    Swagger url : http://localhost:5000/apidocs/
    

3. Endpoint details:

    A) An endpoint to list all stored pets
    URL - http://localhost:5000/petservice/readService/getAllPetsData
    Method - GET
    Input - NA
    Response json - 
        [{"id": 1,"name": "Tommy","species": "dog","gender": "m","birthday": "2017-10-12"},
        {"id": 2,"name": "Sweety","species": "cat","gender": "f","birthday": "2015-01-25"}]
    
    B) An endpoint to update one pet by its id
    URL - http://localhost:5000/petservice/loadService/updatePetsData
    Method - POST
    Input json - {"id": 1,"name": "Tommy","species": "dog","gender": "m","birthday": "2017-10-12"}
    Response json - 
        Data Updated Successfully

    If there are any exceptions then the api response will hold error details
    


Summary:

Few pointers:
1. We can use configparser to store/retrieve the environment specific config(key value pair) which can 
   hold Database details and also SQL queries
2. In order to discover and run all test cases present within project, we can use TestSuite/PyTest 
  and coverge.py/pytest-cov to identify the test coverage.
