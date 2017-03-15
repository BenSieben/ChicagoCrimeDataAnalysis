from pymongo import MongoClient
# Module which has all the logic of the functions to use in the program
OPTION_LIST = [
    '[0] Show this message again'
    '[1] List all the primary types of crimes recorded (kidnapping, theft, robbery, etc.)',
    '[2] Find the most reported primary type of crime (regardless of if an arrest was made or not)',
    '[3] Determine total number of reported crimes for each year',
    '[4] Find all reported crimes in district 1',
    '[5] Find all reported crimes with the primary type of “NARCOTICS”',
    '[6] Find the top 10 locations where the most “THEFT” happens',
    '[7] Find the crime in which most arrests were made',
    '[8] Find the number of domestic crimes in Apartments or Residences',
    '[9] Find the type of crimes committed in School and Universities',
    '[10] Find the number of arrests made in “WEAPONS VIOLATION”',
    '[11] Get all reported crimes on street “E HURON ST” or “W HURON ST”',
    '[12] Find the ward(s) with the least number of crime reports',
    '[13] Find all the different kinds of description values for the “DECEPTIVE PRACTICE” primary type key',
    '[14] Find reports with an x-coordinate between (inclusive on both ends) 117700 and 117800',
    '[15] Find hourly breakdown of “THEFT” in 2016',
]  # List of all options in the program


# Function to make specific kind of string for a list
def print_list(lst):
    print_out = ''
    for elem in lst:
        print_out += elem + '\n'
    return print_out


# Function which returns list (as string) of all the queries which can be used
#   in the program (and their corresponding query number)
def get_query_list():
    return print_list(OPTION_LIST)


# Function which handles bad indexes given in run_query
def bad_index(index):
    return 'Error: index ' + str(index) + ' is not a valid option!'


# Query 1: List all the primary types of crimes recorded (kidnapping, theft, robbery, etc.)
def query_1(collection):
    return 'Query 1 is still in progress...'


# Query 2:  Find the most reported primary type of crime (regardless of if an arrest was made or not)
def query_2(collection):
    return 'Query 2 is still in progress...'


# Query 3: Determine total number of reported crimes for each year
def query_3(collection):
    return 'Query 3 is still in progress...'


# Query 4: Find all reported crimes in district 1
def query_4(collection):
    return 'Query 4 is still in progress...'


# Query 5: Find all reported crimes with the primary type of “NARCOTICS”
def query_5(collection):
    return 'Query 5 is still in progress...'


# Query 6: Find the top 10 locations where the most “THEFT” happens
def query_6(collection):
    return 'Query 6 is still in progress...'


# Query 7: Find the crime in which most arrests were made
def query_7(collection):
    return 'Query 7 is still in progress...'


# Query 8: Find the number of domestic crimes in Apartments or Residences
def query_8(collection):
    return 'Query 8 is still in progress...'


# Query 9: Find the type of crimes committed in School and Universities
def query_9(collection):
    return 'Query 9 is still in progress...'


# Query 10:  Find the number of arrests made in “WEAPONS VIOLATION”
def query_10(collection):
    return 'Query 10 is still in progress...'


# Query 11: Get all reported crimes on street “E HURON ST” or “W HURON ST”
def query_11(collection):
    return 'Query 11 is still in progress...'


# Query 12: Find the ward(s) with the least number of crime reports
def query_12(collection):
    return 'Query 12 is still in progress...'


# Query 13: Find all the different kinds of description values for the “DECEPTIVE PRACTICE” primary type key
def query_13(collection):
    return 'Query 13 is still in progress...'


# Query 14: Find reports with an x-coordinate between (inclusive on both ends) 117700 and 117800
def query_14(collection):
    return 'Query 14 is still in progress...'


# Query 15: Find hourly breakdown of “THEFT” in 2016
def query_15(collection):
    return 'Query 15 is still in progress...'


# Main function which routes the given option to the proper query to run
#   (needs to have the pymongo.collection.Collection passed in as "collection" to run the queries on)
def run_query(index, collection):
    if type(index) is int:
        return {
            0: get_query_list(),
            1: query_1(collection),
            2: query_2(collection),
            3: query_3(collection),
            4: query_4(collection),
            5: query_5(collection),
            6: query_6(collection),
            7: query_7(collection),
            8: query_8(collection),
            9: query_9(collection),
            10: query_10(collection),
            11: query_11(collection),
            12: query_12(collection),
            13: query_13(collection),
            14: query_14(collection),
            15: query_15(collection)
        }.get(index, bad_index(index))
    return 'Type of index must be int, not ' + str(type(index)) + ' for run_query'
