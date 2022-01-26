import json 
import pandas as pd

with open("json_response/issues_and_pulls.json") as f:
    data = json.load(f) # load json data

df = pd.DataFrame(data) # load pandas dataframe

def get_user_id(dict_object):
    return dict_object['id']

def get_milestone_number(dict_object):
    if dict_object == None:
        return None
    else:
        return dict_object['number']

def get_merged_date(dict_object):
    return dict_object['merged_at'] 

def get_date_format(timestamp):
    try:
        return timestamp[0:10]
    except:
        return None
    
def issues_json_to_csv(): # generates issues.csv file

    datetime_columns = ['created_at', 'updated_at', 'closed_at']
    imp_columns = ['number', 'user_id', 'created_at','updated_at', 'closed_at', 'milestone_number', 'state']

    df_issues = df[df['pull_request'].apply(lambda x: not isinstance(x, dict))].reset_index() # only select issues
    df_issues['user_id'] = df_issues['user'].apply(get_user_id)
    df_issues['milestone_number'] = df_issues['milestone'].apply(get_milestone_number)
    df_issues['milestone_number'] = df_issues['milestone_number'].astype('Int64')
    for column in datetime_columns:
        df_issues[column] = df_issues[column].apply(get_date_format)

    issues_pd = df_issues[imp_columns]

    issues_pd = issues_pd.drop_duplicates() # api sometimes seem to fetch duplicate data

    issues_pd.to_csv (r'csv_files/issues.csv', index = None, header=True) # creates a .csv file

def pulls_json_to_csv(): # generates pulls.csv file

    datetime_columns = ['created_at', 'updated_at', 'closed_at', 'merged_at']
    imp_columns = ['number', 'user_id', 'created_at', 'updated_at', 'closed_at', 'state', 'merged_at']
    df_pulls = df[df['pull_request'].apply(lambda x: isinstance(x, dict))].reset_index() # only select pulls
    df_pulls['user_id'] = df_pulls['user'].apply(get_user_id)
    df_pulls['merged_at'] = df_pulls['pull_request'].apply(get_merged_date)

    for column in datetime_columns:
        df_pulls[column] = df_pulls[column].apply(get_date_format)

    pulls_pd = df_pulls[imp_columns]

    pulls_pd = pulls_pd.drop_duplicates() # api sometimes seem to fetch duplicate data

    pulls_pd.to_csv (r'csv_files/pulls.csv', index = None, header=True) # creates a .csv file

if __name__ == "__main__":
    issues_json_to_csv()
    pulls_json_to_csv()




