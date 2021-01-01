# Python File Based key-Value Data Store

1. The database Module supports basic CRD(Create, Read, Delete) operations.

2. Usage:
   
   1. create_db('directory_path') : Creates a database file in specified directory. If no path is specified then file is created in home directory. <br>
   ``` instance = database.create_db('posix_path') ```
   2. open_db('file_path'):  opens the specified database file.<br>
    ``` instance = open_db('file_path') ```
   3. load_db(self): loads the database in program. <br>
   ``` instance.load_db() ```
   4. read_by_key(key): supply the key to get the value <br>
   ``` instance.read_by_key(key) ```
   1. read_db(): read entire database<br>
   ``` instance.read_db() ```
   1. write(key, value): write the key-value pair in database. It asks user whether they want to include time to live property interactively<br>
   ``` instance.write(key, value) ```
   1. bulk_write(liz): supply a list of objects to save in one go<br>
   ``` instance.bulk_write(liz) ```
   1. delete_by_key(key): supply the key to delete the JSON object stored<br>
   ``` instance.delete_by_key(self, key) ```
   1. delete_db():deletes the entire database <br>
   ``` instance.delete_db() ```
   1.  commit(self): for all the changes to be reflected back and permanently stored in file database, user has to commit the changes<br>
   ``` instance.commit() ```

*Note* : The process lock functionality works only in UNIX(e.g. Linux and MacOS) operating systems. This is becuase of restrictions of this project to use 3rd party libraries. The **fcntl** library used in this project for ensuring only only process accesses the file is a standard library in python for UNIX operating systems.