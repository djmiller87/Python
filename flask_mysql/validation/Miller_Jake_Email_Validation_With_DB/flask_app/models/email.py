from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import emails
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        results = connectToMySQL('email_validation').query_db(query, data)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        results = connectToMySQL('email_validation').query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL('email_validation').query_db(query)
        return results

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is not valid!")
            is_valid = False
        return is_valid



