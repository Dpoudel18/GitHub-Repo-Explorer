import json 
import pandas as pd

with open("contributors.json") as f:
    data = json.load(f) # load json data

df = pd.DataFrame(data) # load pandas dataframe

def contributors_json_to_csv(): # generates issues.csv file

    contributors_col_for_csv = ['id', 'login', 'contributions']
    
    final_df = df[contributors_col_for_csv]
    final_df.to_csv (r'csv_files/contributors.csv', index = None, header=True)

if __name__ == "__main__":
    contributors_json_to_csv()




