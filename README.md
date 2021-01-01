# Python File Based key-Value Data Store

1. The database Module supports basic CRD(Create, Read, Delete) operations.

2. Usage:
   
   1. create_db('directory_path') : Creates a database file in specified directory. If no path is specified then file is created in home directory. <br>
   ```
    import database
    instance = database.create_db('posix_path') 
    ```
   2. open_db('file_path'):  opens the specified database file.<br>
    ``` instance = open_db('file_path') ```
   3. load_db(self): loads the database in program. <br>
   ``` instance.load_db() ```
   4. read_by_key(key): supply the key to get the value <br>
   ``` instance.read_by_key(key) ```
   5. read_db(): read entire database<br>
   ``` instance.read_db() ```
   6. write(key, value): write the key-value pair in database. It asks user whether they want to include time to live property interactively<br>
   ``` instance.write(key, value) ```
   7. bulk_write(liz): supply a list of objects to save in one go<br>
   ``` instance.bulk_write(liz) ```
   8. delete_by_key(key): supply the key to delete the JSON object stored<br>
   ``` instance.delete_by_key(self, key) ```
   9. delete_db():deletes the entire database <br>
   ``` instance.delete_db() ```
   10. commit(self): for all the changes to be reflected back and permanently stored in file database, user has to commit the changes<br>
   ``` instance.commit() ```

*Note* : The process lock functionality works only in UNIX(e.g. Linux and MacOS) operating systems. This is becuase of restrictions of this project to use 3rd party libraries. The **fcntl** library used in this project for ensuring only only process accesses the file is a standard library in python for UNIX operating systems.

# Refernces I used
1. https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python
2. https://stackoverflow.com/questions/10387501/python-get-size-of-an-object
3. https://www.programiz.com/python-programming/methods/built-in/hasattr#:~:text=Join-,Python%20hasattr(),false%20if%20it%20does%20not.&text=hasattr()%20is%20called%20by,to%20be%20raised%20or%20not.