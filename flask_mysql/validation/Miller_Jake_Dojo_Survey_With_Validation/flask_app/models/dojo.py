from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import dojos
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.location = data['location'],
        self.language = data['language']
        self.comment = data['comment'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],

    @classmethod
    def save_survey(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());'
        results = connectToMySQL('dojo_survey').query_db(query, data)
        return results

    @classmethod
    def get_info(cls):
        query = 'SELECT * FROM dojos WHERE id = (SELECT MAX(ID) FROM dojos);'
        results = connectToMySQL('dojo_survey').query_db(query)
        all_info = results[0]
        print(all_info)
        return all_info

    @staticmethod 
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("Must choose a location.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Must choose a language.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Must leave a comment.")
            is_valid = False
        return is_valid
