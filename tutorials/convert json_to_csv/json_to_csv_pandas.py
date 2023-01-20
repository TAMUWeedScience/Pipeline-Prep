#import pandas and json
import pandas as pd
import json

#specify the file path
file_path = "/Users/navjotsingh/Documents/first_gui/species_info.json"

#open the file and use json to read, load data into variabel 'obj'
myjsonfile = open(file_path, 'r')
jsondata = myjsonfile.read()
obj = json.loads(jsondata)

#for our json file, we need only 'species' object. So, extract it.
#this will be a dictionary
species_data = (obj['species']) 

#use 'pd.DataFrame.from_dict' to convert a dictionary to dataframe
df = pd.DataFrame.from_dict(species_data)

#for our file, we needed to transpose rows and columns for a better csv file
df_tp = df.transpose()

#use .to_csv to convert pandas dataframe to csv file
#write it to a csv file
df_tp.to_csv("output.csv")