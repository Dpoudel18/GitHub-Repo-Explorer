from bs4 import BeautifulSoup
import requests
import sys
import re
import datetime
class Repo_rt:

    def __init__(self, github_username, repo_name):
        self.github_username = github_username
        self.repo_name = repo_name
        self.url = f'https://api.github.com/repos/{self.github_username}/{self.repo_name}' 
        self.check_valid_request()
        self.json_response  = requests.get(self.url).json()
        

    def check_valid_request(self):
        if str(requests.get(self.url)) == '<Response [403]>':
            print('API request limit exceeded')
            sys.exit(0)
        elif str(requests.get(self.url)) != '<Response [404]>': 
            self.json_response  = requests.get(self.url).json() 
        else:
            print('Invalid username or repository name')
            sys.exit(0)

    def get_repo_url(self):
        """
        Returns the url of the specified repository.
        """
        return f"The url of the {self.repo_name} repository is: {self.url}"

    def get_num_of_open_issues(self):
        """
        Returns the number of open issues in the specified repository
        """
        open_issues_count = self.json_response['open_issues_count']
        return f"Number of open issues: {open_issues_count}"

    def count_scraper(self, component, open): 
        """
        A helper function that web scrapes the repo url and returns the count of issues and pull requests 
        """
        html_response = requests.get(f"https://github.com/{self.github_username}/{self.repo_name}/{component}").content
        soup = BeautifulSoup(html_response, 'html.parser')
        if open == True:  # open = True scrapes the open {component} count
            count_str = soup.find_all(class_="table-list-header-toggle states flex-auto pl-0")[1].findAll(class_= "btn-link")[0].text
        else:   # open = False scrapes the closed {component} count
            count_str = soup.find_all(class_="table-list-header-toggle states flex-auto pl-0")[1].findAll(class_= "btn-link")[-1].text

        count_int = re.sub('[^0-9]','', count_str)
        return int(count_int)


    def get_num_of_open_issues(self):
        """
        Returns the number of open issues in the specified repository
        """
        open_issues_count = self.count_scraper('issues', open = True)
        return f"Number of open issues: {open_issues_count}"


    def get_num_of_closed_issues(self):
        """
        Returns the number of closed issues in the specified repository
        """
        closed_issues_count = self.count_scraper('issues', open = False)
        return f"Number of closed issues: {closed_issues_count}"

    def get_num_of_total_issues(self):
        """
        Returns the number of total issues in the specified repository
        """
        total_issues_count = self.count_scraper('issues', open = False) + self.count_scraper('issues', open = True)
        return f"Number of total issues: {total_issues_count}"        
    
    def get_num_of_open_pull_requests(self):
        """
        Returns the number of open pull requests in the specified repository
        """        
        open_pull_request_count = self.count_scraper('pulls', open = True)
        return f"Number of open pull requests: {open_pull_request_count}"    

    def get_num_of_closed_pull_requests(self):
        """
        Returns the number of closed pull requests in the specified repository
        """
        closed_pull_request_count = self.count_scraper('pulls',open = False)
        return f"Number of closed pull requests: {closed_pull_request_count}"    

    def get_num_of_total_pull_requests(self):
        """
        Returns the number of total pull requests in the specified repository
        """
        total_pull_requests_count = self.count_scraper('pulls', open = False) + self.count_scraper('pulls', open = True)
        return f"Number of total pull requests: {total_pull_requests_count}"  

    def get_num_of_forks(self):
        """
        Returns the number of forks of the specified repository
        """
        forks_count = self.json_response['forks_count']
        return f"Number of forks: {forks_count}"

    def get_num_of_watch(self):
        """
        Returns the number of 'watch' in the specified repository
        """
        watch_count = self.json_response['subscribers_count']
        return f"Number of 'watch': {watch_count}"
    
    def get_num_of_stars(self):
        """
        Returns the number of stars in the specified repository
        """
        star_count = self.json_response['stargazers_count']
        return f"Number of stars: {star_count}"

    def get_num_of_releases(self):
        pass


    def get_age_of_repo(self):
        """
        Returns the age of the specified repository
        """
        creation_date_str = self.json_response['created_at'][:10]
        creation_date = datetime.datetime.strptime(creation_date_str, '%Y-%m-%d').date()
        def calculate_age(date):
            today = datetime.date.today()
            return today.year - date.year - ((today.month, today.day) < (date.month, date.day))
        return f"Age of the repository: {calculate_age(creation_date)} years"

    def get_repo_overview(self):
        """
        prints the general overview of the specified repository
        """
        repo_components = [
            self.get_repo_url(),
            self.get_num_of_open_issues(),
            self.get_num_of_closed_issues(),
            self.get_num_of_total_issues(),
            self.get_num_of_open_pull_requests(),
            self.get_num_of_closed_pull_requests(),
            self.get_num_of_total_pull_requests(),
            self.get_num_of_watch(),
            self.get_num_of_forks(),
            self.get_num_of_stars(),
            self.get_age_of_repo()
        ]
        print()
        print(f'General overview of the {self.repo_name.capitalize()} repository')
        print('-------------------------------------------')
        for component in repo_components:
            print(component)
        print('-------------------------------------------')
        

if __name__ == "__main__":

    repo = Repo_rt('pandas-dev', 'pandas')
    repo.get_repo_overview()
    repo2 = Repo_rt('numpy', 'numpy')
    repo2.get_repo_overview()
        
