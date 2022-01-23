from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.pais import Pais, PaisList
from db import db
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app) #facilita la creación de resoruces
#db = SQLAlchemy(app)

jwt = JWT(app, authenticate, identity) #Esto crea un endpoint nuevo, /auth
db.init_app(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Pais, '/pais/<string:name>')
api.add_resource(PaisList, '/paises')
api.add_resource(UserRegister, '/register')
