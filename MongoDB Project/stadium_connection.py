# imports
import csv
import sys
from datetime import date, datetime

from pymongo import MongoClient


# function to make connection to mongodb and insert the document
def import_data(file_path):
    # making the connection
    client = MongoClient('mongodb://localhost:27017/')
    db = client['SOCCER']
    stadium = db['STADIUM']
    stadium_field_names = ['match_id', 'matchDate', 'matchTime', 'homeCountry', 'awayCountry', 'homeTeamScore',
                           'awayTeamScore', 'stadium', 'city']
    matches = []

    with open(file_path, 'r') as csv_file:
        csv_dict = csv.DictReader(csv_file, fieldnames=stadium_field_names)
        for row in csv_dict:
            document = {
                '_id': row['stadium'],
                'city': row['city'],
                'matches':[]
            }
            stadium.insert_one(document)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Match_results.csv'

    import_data(file_path)
