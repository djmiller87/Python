from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo_and_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        one_dojo = cls(results[0])        
        for row in results:
            ninja_info = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            }
            one_dojo.ninjas.append(ninja_info)
        return one_dojo