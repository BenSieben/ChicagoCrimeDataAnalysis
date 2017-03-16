from pymongo import MongoClient, errors
from crimeanalysisconfig import *
from crimeanalysisfunctions import *


# Main module which handles running the entire program
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
    db = client[MONGODB_CHICAGO_CRIME_DATABASE_NAME]  # Get reference to database with crime data
    chicago_crime_collection = db[MONGODB_CHICAGO_CRIME_COLLECTION_NAME]  # Get reference to collection with crime data

    # Main program loop: prompt user to pick which query to perform on Chicago crime data
    print('\nHere are the current query options in the program:')
    option = 0
    while option != EXIT_SHELL_VALUE:
        # Check for valid options being used
        if option < -1 or option > 15:
            print('Please enter a valid number!')

        # Exit
        elif option == -EXIT_SHELL_VALUE:
            break

        else:
            # Here, if we get a very large number of documents back, we will slowly iterate results
            #   and let user choose to continue viewing more documents or get back to main options
            #   unless the option is 0, in which case we will print out everything
            if option != SHOW_OPTIONS_VALUE:
                result = print_n_lines(run_query(option, chicago_crime_collection), NUM_LINES_TO_PRINT)
                option = 'it'
                while result.find('\n') != -1 and option == 'it':
                    print('Enter "it" to view more results (or anything else to choose another option)')
                    option = input('--> ')
                    if option != 'it':
                        break
                    result = print_n_lines(result, NUM_LINES_TO_PRINT)

            else:
                print(run_query(option, chicago_crime_collection))

            print('\nWhat option would you like to use? (enter -1 to exit; enter 0 to show query options)')
            option_text = input('--> ')

            # Try to read in int value from user.
            # If it is not an integer, set option to -2 to trigger error print in next loop
            try:
                option = int(option_text)
            except ValueError:
                option = -2

    # Close connection to MongoDB database
    client.close()
    print('Goodbye!')

main()
