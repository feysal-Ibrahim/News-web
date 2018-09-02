from flask import Flask
# from flask_bootstrap import Bootstrap

'''
initialize app with the flask module
'''
'''
'''
from .config import DevConfig
'''

'''

app = Flask(__name__, instance_relative_config=True)
'''
1.create an instance of the class Flask and called it app and pass the __name__variable.This name variable is used by flask module to determine the root path of the application.
.Flask locates resources for the app relative to that path.
2.add news api key to the config file in the instance folder in root app and then connects it to
the app by passing it in the __name__ variable when the app is instantiated.this allows us to connect
to the instance folder where the config file is located so that it can access the api key. 

'''
app.config.from_object(DevConfig)

app.config.from_pyfile('config.py')

'''
The app.config.from_pyfile('config.py) connects to the config.py file and all its content are appended to the app.config
'''

# Initializing Flask Extensions
# bootstrap = Bootstrap(app)


from app import views
'''

'''