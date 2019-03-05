Open Space API
===============
A REST API that allows users to search for information on solar objects.

Setting up the project
-----------------------
Open Space runs on python3, please make sure you are using the latest.
You will need these dependencies:
```bash
sudo apt-get install python3 python3-dev
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

Setup Virtual Environment (venv)
----------------------------------
Create the project directiory:
```bach
mkdir openspaceapi
cd openspaceapi
```

Setup the virtual environment. We use Python3:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install Required PIP packages
------------------------------
Install all the required Python packages. Simply save the requirements.txt file from
this project on your local machine and install.
```bash
cd openspaceapi
pip install -r requirements.txt
```

Using the Scrapy Tool
-----------------------
To read the contents of the Wikipedia page, use the scrapy crawl function:
```bash
cd wikiscraper
scrapy crawl SpaceShuttleMissions -o shuttlemissions.json
```
This will execute the web scrapper and write the contents to a JSON file.

Setting up the PostgresSQL Database
====================================
To setup the database, please follow the following steps to setup the PostgreSQL database.

Setting up the Open Space API Database
---------------------------------------
PostgreSQL is used for database. To install PostgreSQL, ensure you have the latest and install postgres:
```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Creating a PostgreSQL user account
-----------------------------------
To utilize the PostgreSQL database, a user account is needed.
On the system, first add a new user account:
```
sudo adduser openspaceapi-db-user
```
Next, create a new user on PostgreSQL database and set up the password:
```
sudo -u postgres createuser --interactive
```
The user in my case was 'openspaceapi-db-user' with a superuser role

Update the user's password on PostgresSQL
------------------------------------------
Open up PostgresSQL and update the password:
```
ALTER USER "<USERNAME>" PASSWORD '<PASSWORD';
```

Create the Open Space Database
-------------------------------
To create the database, use this action
```
createdb <DATABASENAME>
```
The database in my case was 'openspacedpidb'.

Create the database tables
---------------------------
To create the tables, DBComm's init_db() function is used.
First, make sure you are in the 'webapp' directory.
Create an instance of python and run the init_db() command.
```
cd openspaceapi
python3
```

Once the Python shell opens, import init_db and run it:
```
from webapp.database.dbcomm import init_db
init_db()
```

Populate the database
----------------------
To populate the database with the data that was scraped by the wikiscraper, we'll use the populdate DB python file.
First, make sure ou are in the 'webapp' directory. Then run the file
```
cd webapp
python3 -m database.populateDB
```

