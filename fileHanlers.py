import random
from datetime import datetime

class FileHandlers:
    @classmethod
    def fileContent(cls, path):
        """read file"""
        file = None
        with open(path, 'r') as f:
            file = f.read()
        return file
    
    @classmethod
    def appendNew(cls, path):
        """append new data to file"""
        with open(path, 'a') as f:
            value = "// this is my conmment"  + str(random.random())
            f.write(f'\n{value}')
    
    @classmethod
    def updateAndRead(cls, path):
        """First append new files and then read it"""
        cls.appendNew(path)
        file = cls.fileContent(path)
        return file
    
    def log_error(self, content):
        with open('log.txt', 'a') as f:
            curr_date = str(datetime.now())
            f.write(f'\n{content} ----  {curr_date}') 

        print("Failed, exiting...")