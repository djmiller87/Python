#1. Update Values in Dictionaries and Lists

#   1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#    2.Change the last_name of the first student from 'Jordan' to 'Bryant'
#    3.In the sports_directory, change 'Messi' to 'Andres'
#    4.Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 

def update_values(list):
    list[1][0] = 15
    return list
print(update_values(x))


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def update_list_dictionary_students(dict):
    dict[0]['last_name'] = 'Bryant'
    return dict
print(update_list_dictionary_students(students))


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def update_dictionary(diction):
    diction['soccer'][0] = 'Andres'
    return diction
print(update_dictionary(sports_directory))


z = [ {'x': 10, 'y': 20} ]

def update_the_value(a_list):
    a_list[0]['y'] = 30
    return a_list
print(update_the_value(z))


# 2. Iterate Through a List of Dictionaries

#    Create a function iterateDictionary(some_list) that, given a list of dictionaries,
#    the function loops through each dictionary in the list and prints each key and the associated value. 
#    For example, given the following list:

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

studentsinfo = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(a_list):
    for x in range(len(a_list)):
        for key,val in a_list[x].items():
            print(f'{key} - {val}')

iterate_dictionary(studentsinfo)



# 3 Get Values From a List

# Create a function iterateDictionary2(key_name, some_list) that, given 
# a list of dictionaries and a key name, the function prints the value 
# stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) 
# should output:

def iteratedictionary2(key_name, some_list):
    for x in range(len(some_list)):
        for key, value in some_list[x].items():
            if key == key_name:
                print(f'{value}')
iteratedictionary2('first_name', studentsinfo)
iteratedictionary2('last_name', studentsinfo)


# 4. Iterate Through a Dictionary with List Values
        # (This one sucked)

# Create a function printInfo(some_dict) that given
#  a dictionary whose values are all lists, prints the
#  name of each key along with the size of its list, and
#  then prints the associated values within each key's list. For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(a_list):
    for key,value in a_list.items(): 
        print(f'{len(value)} {key.upper()}')
        for x in range(0,len(value)):
            print(value[x])
printinfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

