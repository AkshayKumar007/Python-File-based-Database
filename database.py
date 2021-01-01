import os
import json
import fcntl  # for UNIX only
import atexit

from os import path
from threading import Thread


key_char_limit_error = TypeError('Key length shall not exceed 32 characters')
json_size_limit_error = MemoryError('JSON size exceeded 16KB')
db_size_limit_error = MemoryError('File size reached 1GB. Try creating a new Database instance')

class Database:
    # data members = db, filename, dthread, auto_dump, loco
    def __init__(self, filepath) -> None:
        super().__init__()
        self.filename = filepath
        self.file_obj = open(filepath, 'wt')
        self.file_no = self.file_obj.fileno()
        try:
            fcntl.lockf(self.file_no, fcntl.LOCK_EX)
            atexit.register(self.close_db)
        except OSError as e:
            raise PermissionError('File is being used by other process(es)')

    def open_db(self): # opens file containg db
        try:
            self.f_obj = open(self.filename, 'w+')
            self.db = json.load(self.f_obj)   
        except ValueError as e:
            if path.getsize(self.filename) == 0:
                self.db = {}
            else:
                raise ValueError('File is corrupted or not in JSON format.')
    
    def close_db(self): # for closing file and removing lock on file by process
        del self.db
        fcntl.lockf(self.file_no, fcntl.LOCK_UN)
        self.f_obj.close()
    
    def commit(self):
        json.dump(self.db, self.file_obj)
        return True

    def read_db(self): # read  data
        return self.db
    
    def read_by_key(self, key):
        return self.db[key]

    def bulk_write(self, liz):
        for index in range(len(liz)):
            for key in liz[index]:
                self.db[key] = liz[index][key]
    
    def write(self, key, value):
        self.db[key] = value

    def delete_by_key(self, key):
        del self.db[key]
        
    def delete_db(self):
        del self.db

def create_db(dir_path=None):
    
    if dir_path == None:
        print('Inside None')
        file_path = path.expanduser('~') + '/database.txt'
        open(file_path, 'wt').close()
        obj = Database(filepath=file_path)
        return obj
    else:
        print('Inside else')
        if dir_path[-1] != '/':
             dir_path += '/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        file_path = dir_path + 'database.txt'
        print('here'+file_path)
        open(file_path, 'wt').close()
        obj = Database(filepath=file_path)
        return obj
            

def open_db(file_path):
    if path.exists(file_path) and path.isfile(file_path):
        obj = Database(filepath=file_path)
        return obj
    else:
        raise FileNotFoundError()
    
# refernces
# https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python