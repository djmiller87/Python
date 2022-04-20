from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re


class Recipe:
    db_name = 'recipes'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.time = data['time']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, time, instructions, date_made, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(time)s, %(instructions)s, %(date_made)s, %(user_id)s, NOW(), NOW());"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_one_info(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        recipe_info = cls(results[0])
        return recipe_info

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes 

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s,time = %(time)s, instructions = %(instructions)s, date_made = %(date_made)s, updated_at = NOW() WHERE recipes.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("*Name must contain at least 3 characters!")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("*Description must contain at least 3 characters!")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("*Instructions must contain at least 3 characters!")
            is_valid = False
        if recipe['date_made'] == "":
            flash("*Invalid date!")
            is_valid = False
        if not 'time' in request.form:
            flash("*Must choose time to make!")
            is_valid = False
        return is_valid