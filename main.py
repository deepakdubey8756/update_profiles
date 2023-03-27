import credentials
from codeforces.codeforcesHandler import CodeForcesHandler
from fileHanlers import FileHandlers
import time
import os

def updateCodeforces(problems):
    print("Codeforces: Updating profile")
    codeforces = CodeForcesHandler(credentials.codeforces_handle, credentials.codeforces_password)
    print("Codeforces: Logging....")

    if codeforces.login() == None:
        FileHandlers.log_error(codeforces.error)
        return
    
    print("Codeforces: Submitting problemsets")
    for index, problem in enumerate(3 * problems):
        print(f"Submitting {index+1}")
        if codeforces.submitproblem(problem) == None:
            FileHandlers.log_error(codeforces.error)
        time.sleep(10)

    print("Codeforces Updated....")

def updateGithub():
    FileHandlers.appendNew('dummy.txt')
    os.system("git add .")
    os.system("git commit -am 'another update'")
    os.system("git push -u origin main")



if __name__ == "__main__":
    problems = [
        {"contest_id": '1807', "problem_id": 'A', 'code_file': 'cf1.cpp'},
        {"contest_id": '1809', "problem_id": 'B', 'code_file': 'cf2.cpp'},
        {"contest_id": '1809', "problem_id": 'A', 'code_file': 'cf3.cpp'}
        ]
    updateCodeforces(problems)
    updateGithub()
