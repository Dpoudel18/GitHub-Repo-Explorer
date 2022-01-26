import json 
import pandas as pd

with open("commits.json") as f:
    data = json.load(f) # load json data

df = pd.DataFrame(data) # load pandas dataframe

def get_author_id(dict_object):
    try:
        return dict_object['id']
    except:
        return None

def get_committer_id(dict_object):
    try:
        return dict_object['id']
    except:
        return None

def get_parents_sha(list_object):
    try:
        return list_object[0]['sha']
    except:
        return None

def get_commit_message_label(dict_object):
    try:
        return dict_object['message'].split(" ")[0].split(":")[0]
    except:
        return None

def get_commit_date(dict_object):
    try:
        return dict_object['committer']['date']
    except:
        return None

def get_date_format(timestamp):
    try:
        return timestamp[0:10]
    except:
        return None


def commits_json_to_csv(): # generates commits.csv file

    commits_col_for_csv = ['sha', 'author_id', 'committer_id', 'message_label','parents_sha', 'commit_date']

    df['author_id'] = df['author'].apply(get_author_id)
    df['committer_id'] = df['committer'].apply(get_committer_id)
    df['message_label'] = df['commit'].apply(get_commit_message_label)
    df['parents_sha'] = df['parents'].apply(get_parents_sha)
    df['author_id'] = df['author_id'].astype('Int64')
    df['committer_id'] = df['committer_id'].astype('Int64')
    df['commit_date'] = df['commit'].apply(get_commit_date).apply(get_date_format)

    pd_commits = df[commits_col_for_csv]
    print(pd_commits)

    pd_commits.to_csv (r'csv_files/commits.csv', index = None, header=True)


if __name__ == "__main__":
    commits_json_to_csv()