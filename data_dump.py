import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/default of credit card clients.csv"
DATABASE_NAME = "Credit_Card"
COLLECTION_NAME = "CC_Defaulter"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH, sep=',', header=None,engine="python")
    print(f"Number of rows and column : {df.shape}")

    #convert df to json which can be dumped in mongodb
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[1])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)