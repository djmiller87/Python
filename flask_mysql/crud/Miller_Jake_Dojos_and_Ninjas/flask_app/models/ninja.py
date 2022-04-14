from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        ninjas_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        