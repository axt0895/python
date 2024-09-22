# imports
from pymongo import MongoClient


# Method to read csv files and insert data into the collection
def import_data(country, players, player_cards, player_assists_goals, worldcup_history):

    # making connection to mongodb
    client = MongoClient('mongodb://localhost:27017/')
    db = client['SOCCER']
    countrys = db['COUNTRY']

    # Reading country csv files and inserting values into document
    with open(country, 'r') as csv_file:
        for rows in csv_file:
            values = rows.split(",")
            document = {
                '_id': values[0][1:-1],
                'population': float(values[1]),
                'numOfWorldCupWon': int(values[2]),
                'manager': values[3][1:-1],
                'capital': values[4][1: -1],
                'players': [],
                'worldcup_history': []
            }
            countrys.insert_one(document)

    # Insert players into player arrays inside country document
    with open(players, 'r') as csv_file:
        for rows in csv_file:
            values = rows.split(',')
            document = {
                '_id': int(values[0]),
                'lastName': values[2][1:-1],
                'firstName': values[3][1:-1],
                'height': float(values[6]),
                'DOB': values[4][1:-1],
                'isCaptain': values[10][:-1].lower(),
                'position': values[8][1:-1],
            }
            player_country = values[5][1:-1]
            countrys.update_one({"_id": player_country}, {"$push": {"players": document}})

    # Now, we update each player in player arrays and add fields to each player, such as red cards & yellow cards
    with open(player_cards, 'r') as csv_file:
        for rows in csv_file:
            values = rows.split(",")
            countrys.update_one({"players": {"$elemMatch": {"_id": int(values[0])}}},
                               {"$set": {"players.$.yellowCards": int(values[1]),
                                         "players.$.redCards": int(values[2])}})

    # Now, we again update each player in player arrays and add fields, such as number of goals & number of assists
    with open(player_assists_goals, 'r') as csv_file:
        for rows in csv_file:
            values = rows.split(",")
            countrys.update_one({"players": {"$elemMatch": {"_id": int(values[0])}}},
                               {"$set": {"players.$.numGoals": int(values[2]),
                                         "players.$.numAssists": int(values[3])}})

    # Now, we add the worldcup history as an object to the worldcup_history array
    with open(worldcup_history, 'r') as csv_file:
        for rows in csv_file:
            values = rows.split(",")
            history = {
                'year': values[0],
                'hostCountry': values[1][1:-1]
            }
            countrys.update_one({"_id": values[2][1:-2]}, {"$push": {"worldcup_history":  history}}, upsert=True)


# file path location of each csv file and calling function that makes connection to mongo db and insert data
if __name__ == '__main__':
    country = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Country.csv'
    players = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Players.csv'
    player_card = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Player_Cards.csv'
    players_assists_goals = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Player_Assists_Goals.csv'
    worldcup_history = '/Users/anilthapa/Downloads/OneDrive_1_10-8-2024/Worldcup_History.csv'

    import_data(country, players, player_card, players_assists_goals, worldcup_history)
