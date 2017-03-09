from pymongo import MongoClient
from crimeanalysisconfig import *


def main():
    # Open connection to configured collection in MongoDB database which contains the Chicago crime data
    client = MongoClient(MONGODB_HOST_NAME, MONGODB_PORT_NUMBER)
    db = client[MONGODB_CHICAGO_CRIME_DATABASE_NAME]
    chicago_crime_collection = db[MONGODB_CHICAGO_CRIME_COLLECTION_NAME]

    # Main program loop: prompt user to pick which query to perform on Chicago crime data
    print 'Chicago Crime Data Analysis'
    option = 1
    while option != 0:
        print 'What option would you like to use? (enter 0 to exit)'
        option_text = raw_input('--> ')
        try:
            option = int(option_text)
        except ValueError:
            option = -1
        if option < 0 or option > 15:
            print 'Please enter a valid number!'
        elif option == 0:
            break
        else:
            print 'TODO'

    # Close connection to MongoDB database
    client.close()
    print 'Goodbye!'

main()
