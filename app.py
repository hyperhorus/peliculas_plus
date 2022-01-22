from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.pais import Pais, PaisList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app) #facilita la creación de resoruces

jwt = JWT(app, authenticate, identity) #Esto crea un endpoint nuevo, /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Pais, '/pais/<string:name>')
api.add_resource(PaisList, '/paises')
api.add_resource(UserRegister, '/register')
