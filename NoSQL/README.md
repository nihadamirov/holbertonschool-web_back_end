# Project Badge

**NoSQL**  
**Level:** Amateur  
**By:** Emmanuel Turlay, Staff Software Engineer at Cruise and Guillaume, CTO at Holberton School  
**Weight:** 1  
**Migrated to checker v2:**  
Your score will be updated as you progress.

## Resources

Read or watch:

- [NoSQL Databases Explained](#)
- [What is NoSQL?](#)
- [MongoDB with Python Crash Course - Tutorial for Beginners](#)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](#)
- [Aggregation](#)
- [Introduction to MongoDB and Python](#)
- [mongo Shell Methods](#)
- [The mongo Shell](#)

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General

- What NoSQL means 
- What is the difference between SQL and NoSQL
- What is ACID
- What is document storage
- What are NoSQL types
- What are the benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: `// my comment`
- A `README.md` file, at the root of the project folder, is mandatory
- The length of your files will be tested using `wc`

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.\*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your code should not be executed when imported (use `if __name__ == "__main__":`)

## More Info

### Install MongoDB 4.2 in Ubuntu 18.04

Official installation guide:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$ sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

Potential issue if document creation doesn’t work or you encounter this error: `Data directory /data/db not found., terminating`


```$ sudo mkdir -p /data/db```

Or if /etc/init.d/mongod is missing, please find an example of the file here.

### Use “container-on-demand” to run MongoDB
- Ask for container Ubuntu 18.04 - MongoDB
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MongoDB before interacting with it:

```bash
$ service mongod start
* Starting database mongod [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
```

| Number | Name                          | Short Description                                                                 | Filename                  |
|--------|-------------------------------|-----------------------------------------------------------------------------------|---------------------------|
| 0      | List all databases            | Write a script that lists all databases in MongoDB.                                | 0-list_databases          |
| 1      | Create a database             | Write a script that creates or uses the database `my_db`.                          | 1-use_or_create_database   |
| 2      | Insert document               | Write a script that inserts a document with the attribute `name` = "Holberton school" in the collection `school`. | 2-insert                   |
| 3      | All documents                 | Write a script that lists all documents in the collection `school`.                | 3-all                     |
| 4      | All matches                   | Write a script that lists all documents with `name` = "Holberton school" in the collection `school`. | 4-match                   |
| 5      | Count                         | Write a script that displays the number of documents in the collection `school`.   | 5-count                   |
| 6      | Update                        | Write a script that updates a document with `name` = "Holberton school" by adding the attribute `address` = "972 Mission street". | 6-update    |
| 7      | Delete by match               | Write a script that deletes all documents with `name` = "Holberton school" in the collection `school`. | 7-delete       |
| 8      | List all documents in Python  | Write a Python function that lists all documents in a collection.                  | 8-all.py                  |
| 9      | Insert a document in Python   | Write a Python function that inserts a new document in a collection based on kwargs. | 9-insert_school.py       |
| 10     | Change school topics          | Write a Python function that changes all topics of a school document based on the name. | 10-update_topics.py      |
| 11     | Where can I learn Python?     | Write a Python function that returns the list of schools having a specific topic.  | 11-schools_by_topic.py    |
| 12     | Log stats                     | Write a Python script that provides some stats about Nginx logs stored in MongoDB. | 12-log_stats.py           |
