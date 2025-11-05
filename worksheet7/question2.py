# (2) 2. Create a module, JSONProcessor. It should contain functions for loading JSON data
# from an external file and printing JSON data. The JSON file should contain following
# player details. Create a JSON file with this information.
# {
#     {
#         \player_name": \Shubham"
#         \player_email": \shubham@abc.org"
#         \player_score: 45
#         \man_of_the_match": false
#     },
#     {
#         \player_name": \Rohit"
#         \player_email": \rohit@abc.org"
#         \player_score: 75
#         \man_of_the_match": false
#     },
#     {
#         \player_name": \Virat"
#         \player_email": \virat@abc.org"
#         \player_score: 100
#         \man_of_the_match": false
#     }
#     ]
# }
# Load this file into a dictionary using the JSON module. Set the man_of_the_match
# field to True for a player who has scored the maximum score among all players. Write
# back this information into a new JSON file.

import JSONprocessor as js

data = js.read_json("playes_data.json")

print("Data before changes")
js.print_json(data)

updated = js.give_man_of_the_match(data)

print("Data after changes")
js.print_json(updated)

js.save_json("updated", "playes_data.json")


