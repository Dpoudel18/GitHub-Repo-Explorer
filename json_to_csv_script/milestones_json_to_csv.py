import json 
import pandas as pd

with open("json_response/milestones.json") as f:
    data = json.load(f) # load json data

df = pd.DataFrame(data) # load pandas dataframe

def get_date_format(timestamp):
    try:
        return timestamp[0:10]
    except:
        return None

def get_user_id(dict_object):
    return dict_object['id'] 

def milestones_json_to_csv(): # generates issues.csv file

    datetime_columns = ['created_at', 'updated_at', 'due_on', 'closed_at']

    for column in datetime_columns:
        df[column] = df[column].apply(get_date_format)
    
    df['creator_id'] = df['creator'].apply(get_user_id)
    
    milestones_col_for_csv = ['number', 'title', 'creator_id', 'created_at', 'updated_at', 'due_on', 'closed_at', 'open_issues', 'closed_issues', 'state']
    
    final_df = df[milestones_col_for_csv]
    final_df.to_csv (r'csv_files/milestones.csv', index = None, header=True)

if __name__ == "__main__":
    milestones_json_to_csv()