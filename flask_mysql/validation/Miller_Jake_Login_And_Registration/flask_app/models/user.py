from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL('user_login').query_db(query, data)
        return results

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('user_login').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        fname = str(user['first_name'])
        lname = str(user['last_name'])
        user_in_db = User.get_by_email({'email': user['email']})
        if len(user['first_name']) < 2:
            flash("*First name must contain at least 2 characters!", 'register')
            is_valid = False
        if not fname.isalpha():
            flash("*First name must be letters only!", 'register')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("*Last name must contain at least 2 characters!", 'register')
            is_valid = False
        if not lname.isalpha():
            flash("*Last name must be letters only!", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("*Invalid email address!", 'register')
            is_valid = False
        if user_in_db:
            flash("*Email already taken!", 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash("*Password must contain at least 8 characters!", 'register')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("*Passwords do not match!", 'register')
            is_valid = False
        if re.search('[0-9]', user['password']) is None:
            flash("*Passwords must contain a number!", 'register')
            is_valid = False
        if re.search('[A-Z]', user['password']) is None:
            flash("*Passwords must contain a capital letter!", 'register')
            is_valid = False
        if re.search('[$#@]', user['password']) is None:
            flash("*Passwords must contain a symbol!", 'register')
            is_valid = False
        return is_valid
        


