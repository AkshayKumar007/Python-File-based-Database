import os
import sys
import time
import json
import queue

from os import path
from threading import Thread

key_char_limit_error = TypeError('Key length shall not exceed 32 characters')
json_size_limit_error = MemoryError('JSON size exceeded 16KB')
db_size_limit_error = MemoryError('File size reached 1GB. Try creating a new Database instance')

class Database:
    def __init__(self, filepath) -> None:
        super().__init__()
        if filepath == None:
            pass
        else:
            pass
    
    def read(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)

def create_db(dir_path=None):
    file_path = None
    if dir_path == None:
        file_path = path.expanduser('~') + '/database.txt'
    else:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            if dir_path[-1] != '/':
                dir_path += '/'
            file_path = dir_path + 'database.txt'
            open(file_path, 'a').close()

    db = Database(filepath=file_path)
    return db

def open_db(file_path):
    if path.exists(file_path) and path.isfile(file_path):
        db = Database(filepath=file_path)
        return db
    else:
        return FileNotFoundError()
    
