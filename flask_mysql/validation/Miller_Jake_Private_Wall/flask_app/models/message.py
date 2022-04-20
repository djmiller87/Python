from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.controllers import messages, users
from datetime import datetime
import math

class Message:
    db_name = 'user_wall'
    def __init__(self, db_data):
        self.id = db_data['id']
        self.message = db_data['message']
        self.sender_id = db_data['sender_id']
        self.sender = db_data['sender']
        self.recipient_id = db_data['recipient_id']
        self.recipient = db_data['recipient']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds)
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds()/60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds()/60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds()/60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"


    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages (message, sender_id, recipient_id) VALUES (%(message)s, %(sender_id)s, %(recipient_id)s);"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_user_messages(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as recipient, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.recipient_id WHERE users2.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        messages = []
        for message in results:
            messages.append(cls(message))
        print(messages)
        return messages

    @classmethod
    def number_sent_messages(cls, data):
        query = "SELECT users.first_name as sender, users2.first_name as recipient, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.recipient_id WHERE messages.sender_id = 1;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        messages = []
        for message in results:
            messages.append(cls(message))
        print(messages)
        return messages

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(str(message)) < 2:
            flash("Message must contain 2 characters!")
            is_valid = False
        return is_valid
