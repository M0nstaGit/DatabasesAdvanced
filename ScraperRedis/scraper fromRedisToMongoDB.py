from time import time
import warnings
import pandas as pd
import pymongo as mongo
import redis
import pickle5 as pickle

# Because of something to do with df.append I ignored this warning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Connect with Redis
r = redis.StrictRedis('localhost')

# Make a connection with the MongoDB database
client = mongo.MongoClient("mongodb://127.0.0.1:27017")
transactions_db = client["transactions"]
col_transactions = transactions_db["transactions"]

# Create dataframe and set header for the 5 biggest transactions
header = ['hash', 'amountBitcoin', 'amountDollar', 'time']
biggest5 = pd.DataFrame(columns = header)

for i in range(0,5):
    # Set the current highest
    currentHighestDict = {'hash': 'none', 'amountBitcoin': "0 BTC", 'amountDollar': 0.00, "time":time}
    currentHighestAmount = float(0.00)

    # Loop through all of the Redis data
    for y in range(0,50):
        read_dict = r.get(f"transaction{y}")
        yourdict = pickle.loads(read_dict)

        # If the current dictionary is already in the dataframe, we will skip this one and go to the next one
        if biggest5['hash'].str.contains(yourdict['hash']).any():
            pass

        else:
            # Check if the current dictionary has a larger transaction then the current highest. If so set that one as the current largest
            if float(yourdict['amountDollar']) > currentHighestAmount:
                currentHighestAmount = yourdict['amountDollar']
                currentHighestDict = yourdict

    # Add the largest to the dataframe
    biggest5 = biggest5.append(currentHighestDict, ignore_index=True)

# Loop trough the 5 biggest transactions
for i in range(0,5):
    current_row = biggest5.iloc[i]

    current_hash = current_row["hash"]
    current_amountBTC = current_row["amountBitcoin"]
    current_amountDollar = current_row["amountDollar"]
    current_time = current_row["time"]

    # Combine data in a dictionary
    data = {"hash": current_hash, "amountBitcoin": current_amountBTC, "amountDollar": current_amountDollar, "time": current_time}

    # Send to MongoDB
    col_transactions.insert_one(data)

print("Data has been send to MongoDB")