from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'friendships'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return results 

    @classmethod
    def create_friendship(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def all_friendships(cls):
        query = "SELECT users.id, users.first_name, users.last_name, friends.first_name AS friend_first, friends.last_name AS friend_last FROM users LEFT JOIN friendships ON friendships.user_id = users.id JOIN users AS friends ON friends.id = friendships.friend_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return results
