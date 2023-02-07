import pandas as pd
import json
from pathlib import Path

#input the file path
file_path = Path(input('File path: '))

def json_to_csv():
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
    df_tp.to_csv(f"{file_path.parent}/output.csv")

json_to_csv()