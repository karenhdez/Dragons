from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


#This creates the application instance.
#This App instance is the web server andpasses all requests it receives
#from clients to this object for handling,
#using the Web Server Gateway Interface(WSGI) protocol
app = Flask(__name__)



app.config.from_pyfile('config.py')

Bootstrap(app)

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    #app.run(debug=True,)
    app.run(debug=True, host='127.0.0.1', port=8000)
