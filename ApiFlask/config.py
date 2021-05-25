from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#iniciar app
app = Flask(__name__)

#conf de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/apidb'
db = SQLAlchemy(app)