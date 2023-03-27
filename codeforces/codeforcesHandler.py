import requests
from bs4 import BeautifulSoup
from fileHanlers import FileHandlers

class CodeForcesHandler:

    def __init__(self, handle, password):
        self.handle = handle
        self.password = password
        self.session = requests.session()
        self.error = None

    def get_csrf(self, url):
        """Scrape page from url, parse it and capture csrf token from it."""
        page = self.session.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        element = soup.find('input', attrs={'name': 'csrf_token'})
        if element == None:
            self.error = "Faild to find csrf"
            return None
        return element['value']

    def login(self):
        """Loging user to codeforces"""

        # login url
        url = 'https://codeforces.com/enter'

        # csrf token
        csrf_token = self.get_csrf(url)

        if csrf_token == None:
            self.error = "Failed to capture csrf token during loging... "
            return None

        login_data = {
        'csrf_token': csrf_token,
        'action': 'enter',
        'handleOrEmail': self.handle,
        'password': self.password,
        '_tta': '602',
        'remember': 'on'
        }

        status = self.session.post(url, data=login_data)

        if status.status_code != 200:
            self.error = "Failed to login"
            return None
        return 1


    def submitproblem(self, problem):
        """Submitting problems"""
        contest_id = problem['contest_id']
        problem_id = problem['problem_id']
        code_file = "codeforces/"+problem['code_file']
        
        submit_url = f'https://codeforces.com/contest/{contest_id}/submit'

        csrf_token = self.get_csrf(submit_url)

        if csrf_token == None:
            self.error = "Failed to caputre url during problem submission"
            return None
        
        submit_data = {
            'csrf_token': csrf_token,
            'action': 'submitSolutionFormSubmitted',
            'submittedProblemIndex': problem_id,
            'programTypeId': '54',
            'sourceFile': FileHandlers.updateAndRead(code_file),
            '_tta': '602'
        }

        status = self.session.post(submit_url, data=submit_data)

        if status == None:
            self.error = "Failed to submit problems"
            return None
        
        return 101
    



