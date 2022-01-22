import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.pais import PaisModel


class Pais(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idioma',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )

    @jwt_required()
    def get(self, name):
        pais = PaisModel.find_by_name(name)
        if pais:
            return pais.json()
        return {'message':'Pais not found'}, 404

    def post(self, name):
        if PaisModel.find_by_name(name):
            return {'message': f"an pais with name {name} already exists"}, 400

        data = Pais.parser.parse_args()

        pais = PaisModel(name, data['idioma'])
        try:
            pais.insert()
        except:
            return {"message": "An error ocurred inserting the pais."}, 500 #internal server error

        return pais.json(), 201   #indica que el item fue creado

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM paises WHERE name =?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message": f"{name} deleted"}


    def put(self, name):
        data = Pais.parser.parse_args()
        pais = PaisModel.find_by_name(name)
        updated_pais = PaisModel(name, data['idioma'])
        if pais == None:
            try:
                updated_pais.insert()
            except:
                return {"message": "An error ocurred inserting the pais."}, 500  #internal server error
        else:
            try:
                updated_pais.update()
            except:
                return {"message": "An error ocurred updating the pais."}, 500  # internal server error
        return updated_pais.json()

class PaisList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        paises = []

        query = "SELECT * FROM paises"
        result = cursor.execute(query)
        for row in result:
            paises.append({'name': row[0], 'idioma':row[1]})
        connection.close()
        return {'paises': paises}

        #return {'items': 'No items found'}
