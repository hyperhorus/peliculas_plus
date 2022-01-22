import sqlite3

class PaisModel:
    """docstring for ."""

    def __init__(self, name, idioma):
        self.name = name
        self.idioma = idioma

    def json(self):
        return {'name': self.name, 'idioma': self.idioma}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM paises WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO paises VALUES (?, ?)"
        cursor.execute(query, (self.name, self.idioma))
        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE paises SET idioma=? WHERE name=? "
        cursor.execute(query, (self.idioma, self.name))
        connection.commit()
        connection.close()
