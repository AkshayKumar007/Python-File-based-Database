from genericpath import exists
import os
import datetime
import json
import fcntl  # for UNIX only
import atexit

from os import path
from threading import Thread

key_type_error = TypeError('Key Should be a string')
key_exists_error = IndexError('Key already exists')
key_char_limit_error = TypeError('Key length shall not exceed 32 characters')
json_size_limit_error = MemoryError('JSON size exceeded 16KB')
db_size_limit_error = MemoryError('File size reached 1GB. Try creating a new Database instance')

class Database:
    # data members = db, filename, dthread, auto_dump, loco
    def __init__(self, filepath) -> None:
        super().__init__()
        self.filename = filepath
        
        self.file_obj = open(filepath, 'r+')
        self.file_no = self.file_obj.fileno()
        
        try:
            fcntl.lockf(self.file_no, fcntl.LOCK_EX)
            atexit.register(self.close_db)
        except OSError as e:
            raise PermissionError('File is being used by other process(es)')

    def load_db(self):  # opens file containg db
        try:
            self.db = json.load(self.file_obj)   
        except ValueError as e:
            if path.getsize(self.filename) == 0:
                self.db = {}
            else:
                raise ValueError('File is corrupted or not in JSON format.')
    
    def close_db(self):  # for closing file and removing lock on file by process
        if hasattr(self, 'db'):
            del self.db
        fcntl.lockf(self.file_no, fcntl.LOCK_UN)
        print('Free resources')
    
    def commit(self):
        if path.getsize(self.filename) >= 1073741824:
            raise db_size_limit_error
        json.dump(self.db, open(self.filename, 'w+'))
        return True

    def read_db(self): # read  data
        return self.db
    
    def read_by_key(self, key):

        return self.db[key]

    def bulk_write(self, liz, time_to_live=None):
        for index in range(len(liz)):
            for key in liz[index]:
                self.write(key, liz[index][key], time_to_live)
    
    def write(self, key, value):
        choice = input('Include Time to Live(Y/n)?')
        if choice == 'Y' or 'y':
            date_entry = input('Enter a date in YYYY-MM-DD-HH-MM format:\t')
            time_to_live = datetime.datetime.strptime(date_entry, '%Y-%m-%d-%H-%M')
            epoch = datetime.datetime.utcfromtimestamp(0)
            time_to_live = (time_to_live - epoch).total_seconds()
        else:
            time_to_live = None
        try:
            if type(key) != str:
                raise key_type_error
            elif len(key) > 32:
                raise key_char_limit_error
            elif self.db.get(key, None) != None:
                raise key_exists_error
            else:
                if time_to_live != None:
                    value = {'time-to-live' : time_to_live, 'value' : value}
                else:
                    value = {'value' : value}
                json_obj = json.dumps(value)
                json_size = len(json_obj.encode('utf-8'))
                if json_size > 16384:
                    raise json_size_limit_error
                else:
                    self.db[key] = json_obj

        except:
            raise TypeError('Object not serializable')

    def delete_by_key(self, key):
        del self.db[key]
        
    def delete_db(self):
        self.db = {}

def create_db(dir_path=None):
    
    if dir_path == None:
        file_path = path.expanduser('~') + '/database.txt'
        open(file_path, 'w+').close()
        obj = Database(filepath=file_path)
        return obj
    else:
        if dir_path[-1] != '/':
             dir_path += '/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        file_path = dir_path + 'database.txt'
        
        open(file_path, 'w+').close()
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
# https://stackoverflow.com/questions/10387501/python-get-size-of-an-object
# https://www.programiz.com/python-programming/methods/built-in/hasattr#:~:text=Join-,Python%20hasattr(),false%20if%20it%20does%20not.&text=hasattr()%20is%20called%20by,to%20be%20raised%20or%20not.