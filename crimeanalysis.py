from pymongo import MongoClient, errors
from crimeanalysisconfig import *


def main():
    print('Chicago Crime Data Analysis\n')

    # Open connection to configured collection in MongoDB database which contains the Chicago crime data
    print('Attempting to connect to MongoDB host ' + MONGODB_HOST_NAME + ' on port ' + str(MONGODB_PORT_NUMBER))
    try:
        client = MongoClient(MONGODB_HOST_NAME, MONGODB_PORT_NUMBER,
                             serverSelectionTimeoutMS=MONGODB_CONNECTION_ATTEMPT_LENGTH_MS)
        client.server_info()  # Establish working connection with MongoDB server by issuing a command on the client
    except errors.ServerSelectionTimeoutError:
        print('Connection timed out (current configuration times out connection after ' +
              str(MONGODB_CONNECTION_ATTEMPT_LENGTH_MS) + ' milliseconds). Make sure the waiting time is' +
              ' long enough and the correct hostname and port are being used in crimeanalysisconfig.py')
        return

    print('Connection successful!')
    db = client[MONGODB_CHICAGO_CRIME_DATABASE_NAME]
    chicago_crime_collection = db[MONGODB_CHICAGO_CRIME_COLLECTION_NAME]
    print(type(chicago_crime_collection))
    # print(chicago_crime_collection.find_one())  # One example on a find of a single document

    # Main program loop: prompt user to pick which query to perform on Chicago crime data
    option = 0
    while option != -1:
        print('What option would you like to use? (enter -1 to exit)')
        option_text = input('--> ')

        try:
            option = int(option_text)
        except ValueError:
            option = -2

        if option < -1 or option > 15:
            print('Please enter a valid number!')
        elif option == -1:
            break
        else:
            print('TODO')

    # Close connection to MongoDB database
    client.close()
    print('Goodbye!')

main()
