from datetime import datetime
# Module which has all the logic of the functions to use in the program
OPTION_LIST = [
    '[0] Show this message again',
    '[1] List all the primary types of crimes recorded (kidnapping, theft, robbery, etc.)',
    '[2] Find the most reported primary type of crime (regardless of if an arrest was made or not)',
    '[3] Determine total number of reported crimes for each year',
    '[4] Find all reported crimes in district 1',
    '[5] Find all reported crimes with the primary type of "NARCOTICS"',
    '[6] Find the top 10 locations where the most "THEFT" happens',
    '[7] Find the crime in which most arrests were made',
    '[8] Find the number of domestic crimes in Apartments or Residences',
    '[9] Find the type of crimes committed in School and Universities',
    '[10] Find the number of arrests made in "WEAPONS VIOLATION"',
    '[11] Get all reported crimes on street "E HURON ST" or "W HURON ST"',
    '[12] Find the ward(s) with the least number of crime reports',
    '[13] Find all the different kinds of description values for the "DECEPTIVE PRACTICE" primary type key',
    '[14] Find reports with an x-coordinate between (inclusive on both ends) 117700 and 117800',
    '[15] Find hourly breakdown of "THEFT" in 2016',
    '[16] Update a chosen "_id" key for a document to update to have its "Update On" key updated to the current time'
]  # List of all options in the program


# Function which prints n lines of given string and return string continuing after those b lines
def print_n_lines(print_str, n):
    i = 0
    split_lines = print_str.split('\n')
    while i < n and i < len(split_lines):
        print(split_lines[i])  # Print the line in split_lines at index i
        i += 1
    return '\n'.join(split_lines[i:])  # Join back remaining part of split lines with \n and return it


# Function to make specific kind of string for a list
def print_list(lst):
    print_out = ''
    for elem in lst:
        print_out += str(elem) + '\n'
    return print_out


# Function which returns list (as string) of all the queries which can be used
#   in the program (and their corresponding query number)
def get_query_list():
    return print_list(OPTION_LIST)


# Function which handles bad indexes given in run_query
def bad_index(index):
    return 'Error: index ' + str(index) + ' is not a valid option!'


# Get time string in a format that is used in the Chicago Crime collection data
def get_current_datetime():
    # Use datetime to get current time
    now = str(datetime.now())

    # Extract pieces of time from the datetime.now() call
    year = now[0:now.find('-')]
    month = now[now.find('-')+1:now.rfind('-')]
    day = now[now.rfind('-')+1:now.find(' ')]

    time = now[now.find(' ')+1:now.find('.')]
    hour = int(time[0:time.find(':')])

    # Depending on the hour, we must indicate AM / PM and adjust hour value accordingly
    time_period = 'PM'
    if hour < 12:
        hour += 12
        time_period = 'AM'
    hour -= 12  # Move hour back 12 hours so we get back in range of 1 to 12
    if hour == 0:  # Fix edge case with 0 as the hour by setting hour to 12 manually
        hour = 12

    # Create the 12-hour time matching the format in Chicago Crime data and return time in proper format
    time_12hour = str(hour) + ':' + time[time.find(':')+1:len(time)] + ' ' + time_period
    current_day = month + '/' + day + '/' + year
    return current_day + ' ' + time_12hour


# Query 1: List all the primary types of crimes recorded (kidnapping, theft, robbery, etc.)
def query_1(collection):
    return 'Query 1: List all the primary types of crimes recorded (kidnapping, theft, robbery, etc.)\n' + \
           print_list(collection.find().distinct('Primary Type'))


# Query 2:  Find the most reported primary type of crime (regardless of if an arrest was made or not)
def query_2(collection):
    pipeline = [
        {"$group": {"_id": {"Primary Type": "$Primary Type"}, "num_reports": {"$sum": 1}}},
        {"$sort":
            {"num_reports": -1}},
        {"$limit": 1}
    ]  # pipeline = pretty much exactly you would use in in normal "db.<collection>.aggregate()" call in mongo shell
    return 'Query 2:  Find the most reported primary type of crime (regardless of if an arrest was made or not)\n' + \
        print_list(collection.aggregate(pipeline))


# Query 3: Determine total number of reported crimes for each year
def query_3(collection):
    pipeline = [
        {"$group": {"_id": {"Year": "$Year"}, "num_reports": {"$sum": 1}}},
        {"$sort":
            {"Year": 1}}
    ]
    return 'Query 3: Determine total number of reported crimes for each year\n' + \
           print_list(collection.aggregate(pipeline))


# Query 4: Find all reported crimes in district 1
def query_4(collection):
    return 'Query 4: Find all reported crimes in district 1\n' + \
           print_list(collection.find({"District": 1}))


# Query 5: Find all reported crimes with the primary type of "NARCOTICS"
def query_5(collection):
    return 'Query 5: Find all reported crimes with the primary type of "NARCOTICS"\n' + \
           print_list(collection.find({"Primary Type": "NARCOTICS"}))


# Query 6: Find the top 10 locations where the most "THEFT" happens
def query_6(collection):
    pipeline = [
        { "$match":{"Primary Type": "THEFT"}},
        {"$group": {"_id": "$Location Description", "num_theft": {"$sum": 1}}},
        {"$sort": {"num_theft": -1}},
        {"$limit":10}
    ]
    return 'Query 6: Find the top 10 locations where the most "THEFT" happens\n' + \
           print_list(collection.aggregate(pipeline))


# Query 7: Find the crime in which most arrests were made
def query_7(collection):
    pipeline = [
        {"$match": {"Arrest":"true"}},
        {"$group": {"_id":"$Primary Type", "num_arrests": {"$sum" : 1}}},
        {"$sort": { "num_arrests":-1}},
        {"$limit": 1}
    ]
    return 'Query 7: Find the crime in which most arrests were made\n' + \
           print_list(collection.aggregate(pipeline))


# Query 8: Find the number of domestic crimes in Apartments or Residences
def query_8(collection):
    pipeline = [
        { "$match": { "$and": [{"Primary Type": "DOMESTIC VIOLENCE"}],"$or": [{"Location Description": "APARTMENT"},
                                                                          {"Location Description": "RESIDENCE"}]}},
        {"$group": {"_id": "$Primary Type", "num_crimes": {"$sum": 1}}}
    ]
    return 'Query 8: Find the number of domestic crimes in Apartments or Residences\n' + \
           print_list(collection.aggregate(pipeline))


# Query 9: Find the type of crimes committed in School and Universities
def query_9(collection):
    return 'Query 9: Find the type of crimes committed in School and Universities\n' + \
           print_list(collection.distinct("Primary Type",{"$or": [ {"Location Description":"SCHOOL, PRIVATE, BUILDING"},{"Location Description": "SCHOOL, PUBLIC, GROUNDS" },{"Location Description": "SCHOOL, PRIVATE, GROUNDS"}]}))


# Query 10:  Find the number of arrests made in "WEAPONS VIOLATION"
def query_10(collection):
    pipeline = [
        {"$match":{"Arrest": "true", "Primary Type": "WEAPONS VIOLATION"}},
        {"$group": {"_id": "$Primary Type", "num_arrests": {"$sum": 1}}}
    ]
    return 'Query 10:  Find the number of arrests made in "WEAPONS VIOLATION"\n' + \
           print_list(collection.aggregate(pipeline))


# Query 11: Get all reported crimes on street "E HURON ST" or "W HURON ST"
def query_11(collection):
    return 'Query 11: Get all reported crimes on street "E HURON ST" or "W HURON ST"\n' + \
           print_list(collection.find({"$or": [{"Block": {'$regex': "W HURON ST"}}, {"Block": {'$regex': "E HURON ST"}}]}))


# Query 12: Find the ward(s) with the least number of crime reports
def query_12(collection):
    pipeline = [
        {"$group": {"_id": {"ward": "$Ward"}, "totalAmount": {"$sum": 1}}},
        {"$sort": {"totalAmount": 1}}
    ]
    return 'Query 12: Find the ward(s) with the least number of crime reports\n' + \
           print_list(collection.aggregate(pipeline))


# Query 13: Find all the different kinds of description values for the "DECEPTIVE PRACTICE" primary type key
def query_13(collection):
    return 'Query 13: Find all the different kinds of description values for the ' \
           '"DECEPTIVE PRACTICE" primary type key\n' + \
           print_list(collection.find({"Primary Type": "DECEPTIVE PRACTICE"}, {"Description": 1, "_id":0}))


# Query 14: Find reports with an x-coordinate between (inclusive on both ends) 117700 and 117800
def query_14(collection):
    return 'Query 14: Find reports with an x-coordinate between (inclusive on both ends) 117700 and 117800\n' + \
           print_list(collection.find({"X Coordinate": {"$gte": 1173000, "$lte": 1175000}}))


# Query 15: Find Arrests from Domestic disputes that happen on Christmas Day
def query_15(collection):

    return 'Query 15: Find Arrests from Domestic disputes that happen on Christmas Day\n' + \
           print_list(collection.find({"$and": [{"Date": {"$regex": ".*12/25.*"}}, {"Arrest": "true"}, {"Domestic": "true"}]}, {"_id": 0, "Primary Type": 1, "Description": 1}))


# Update 1: Update a chosen "_id" key for a document to update to have its "Updated On"
#   key updated to the current time, and show this change by querying for given "_id" before and after
#   the attempted update
# 02/04/2016 06:33:39 AM is an example entry in the "Updated On" key
def update_1(collection):
    # Print out prompt to user to pick _id to change "Updated On" key for
    print('Update 1: Update a chosen "_id" key for a document to update to have '
          'its "Updated On" key updated to the current time')
    print('What is the _id of the report you would like to update?')
    option = input('--> ')
    try:
        option = int(option)
    except ValueError:
        return '_id must be a number! Going back to main prompt...'

    # Attempt to look up collection for a document with matching _id, and return if nothing is found
    doc_before_update = collection.find_one({"_id": option},
                                            {"_id": 1, "Case Number": 1, "Date": 1, "Primary Type": 1,
                                             "Description": 1, "Updated On": 1})
    if doc_before_update is None:  # This means the find_one() call found nothing
        return 'Could not find any document with _id ' + str(option) + '!'
    else:
        print('Found the following matching document (picking a few keys only):\n' + str(doc_before_update))

    # Get current time and update the document with the chosen _id to the current time
    dt = get_current_datetime()
    print('Updating the "Updated On" key value to "' + str(dt) + '"')
    collection.update_one({'_id': option}, {"$set": {"Updated On": dt}}, upsert=False)

    # Return a find_one() call on the same document again
    return 'Here is the updated version of the document (picking a few keys only):\n' + \
           str(collection.find_one({"_id": option},
                                   {"_id": 1, "Case Number": 1, "Date": 1, "Primary Type": 1, "Description": 1,
                                    "Updated On": 1}))


# Main function which routes the given option to the proper query to run
#   (needs to have the pymongo.collection.Collection passed in as "collection" to run the queries on)
def run_query(index, collection):
    if type(index) is int:  # Make sure that index is an integer
        if index == 0:
            return get_query_list()
        elif index == 1:
            return query_1(collection)
        elif index == 2:
            return query_2(collection)
        elif index == 3:
            return query_3(collection)
        elif index == 4:
            return query_4(collection)
        elif index == 5:
            return query_5(collection)
        elif index == 6:
            return query_6(collection)
        elif index == 7:
            return query_7(collection)
        elif index == 8:
            return query_8(collection)
        elif index == 9:
            return query_9(collection)
        elif index == 10:
            return query_10(collection)
        elif index == 11:
            return query_11(collection)
        elif index == 12:
            return query_12(collection)
        elif index == 13:
            return query_13(collection)
        elif index == 14:
            return query_14(collection)
        elif index == 15:
            return query_15(collection)
        elif index == 16:
            return update_1(collection)
        else:
            bad_index(index)  # If given index is not valid, give back bad_index() response
    return 'Type of index must be int, not ' + str(type(index)) + ' for run_query'
