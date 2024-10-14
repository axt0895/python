# imports
import csv
from pymongo import MongoClient

# making connection to mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client['SOCCER']
country = db['COUNTRY']
players = db['PLAYERS']

# file path & header names

# read the players
player_file_path = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Players.csv'
player_field_names =['_id', 'fullName', 'firstName', 'lastName', 'dateOfBirth', 'country', 'height', 'club', 'position', 'capsForCountry', 'captaincy']

# opening & reading csv file then inserting into mongodb
with open(player_file_path, 'r') as csv_file:
    csv_dict = csv.DictReader(csv_file, fieldnames=player_field_names)
    for row in csv_dict:
        document = {}
        for field in player_field_names:
            document[field] = row[field]



        country.insert_one(document)




with open(player_file_path, 'r') as csv_file:
    csv_dict = csv.DictReader(csv_file, fieldnames=player_field_names)
    for row in csv_dict:
        document = {}
        for field in player_field_names:
            document[field] =row[field]
        players.insert_one(document)