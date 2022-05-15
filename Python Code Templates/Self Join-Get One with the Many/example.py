
# -------------------------------------------------------------------------------------
# Example: One to many
# -------------------------------------------------------------------------------------

# *****************************
# SIMPLE WITHOUT JOINING TABLE
# *****************************

#     @classmethod
#     def get_one_dojo_and_ninjas(cls, data):
#         query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
#         results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
#         one_dojo = cls(results[0])        
#         for row in results:
#             ninja_info = {
#                 'id' : row['ninjas.id'],
#                 'first_name' : row['first_name'],
#                 'last_name' : row['last_name'],
#                 'age' : row['age'],
#                 'created_at' : row['ninjas.created_at'],
#                 'updated_at' : row['ninjas.updated_at']
#             }
#             one_dojo.ninjas.append(ninja_info)
#         return one_dojo

# # ***************************
# # WITH JOINING TABLE
# # ***************************

# class User:
#     db_name = 'paintings'
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.password = data['password']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         self.paintings = []

#         @classmethod
#     def get_user_paintings(cls, data):
#         query = "SELECT * FROM users LEFT JOIN owners ON owners.user_id = users.id LEFT JOIN paintings on paintings.id = owners.painting_id WHERE users.id = %(id)s;"
#         results = connectToMySQL(cls.db_name).query_db(query, data)
#         user_paintings = cls(results[0])
#         for row in results:
#             if row['paintings.id'] == None:
#                 break
#             painting_data = {
#                 'id' : row['paintings.id'],
#                 'title' : row['title'],
#                 'description' : row['description'],
#                 'price' : row['price'],
#                 'quantity' : row['quantity'],
#                 'artist_id' : row['artist_id'],
#                 'created_at' : row['created_at'],
#                 'updated_at' : row['updated_at']
#             }
#             user_paintings.paintings.append( painting.Painting(painting_data))
#         return user_paintings



# ----------------------------------------------------------------------------------
# Example: Self Join Many to Many (Users - Messages - Users)
# ----------------------------------------------------------------------------------

    # @classmethod
    # def get_user_messages(cls, data):
    #     query = "SELECT users.first_name as sender, users2.first_name as recipient, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.recipient_id WHERE users2.id = %(id)s;"
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     print(results)
    #     messages = []
    #     for message in results:
    #         messages.append(cls(message))
    #     print(messages)
    #     return messages