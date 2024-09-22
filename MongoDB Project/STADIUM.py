# imports
from pymongo import MongoClient



# Reads the csv files and insert the data into mongodb
def import_data(stadium_path):

    # Making the connection to mongodb
    client = MongoClient('mongodb://localhost:27017/')
    db = client['SOCCER']
    stadium = db['STADIUM']

    # Reading csv files and inserting into document.
    with open(stadium_path, 'r') as csv_file:
        for rows in csv_file:
            rows = rows.split(",")
            document = {
                '_id': rows[7][1:-1],
                'city': rows[8][1:-1],
                'matches': []
            }
            if stadium.find_one({"_id": rows[7][1:-1]}) is None:
                stadium.insert_one(document)
            match = {
                '_id': int(rows[0]),
                'homeTeam': rows[3][1:-1],
                'awayTeam': rows[4][1:-1],
                'homeTeamScore': int(rows[5]),
                'awayTeamScore': int(rows[6]),
                'date': rows[1][1:-1]
            }
            stadium.update_one({"_id": rows[7][1:-1]}, {"$push" : {"matches": match}})

# file path location and calling our function to make connection to data and load data
if __name__ == "__main__":
    stadium = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Match_results.csv'
    match_results = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/'
    import_data(stadium)
