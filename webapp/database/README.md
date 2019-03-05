Setting up the Open Space Database
-----------------------------------
PostgreSQL is used for database. To install PostgreSQL:
```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Creating a PostgreSQL user account:
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
The database in my case was 'openspaceapidb'.

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
Now the database will contain the contents of the wikipedia page that was scraped!

To verify the data is on the database, simply open the PostgreSQL database and query for the tables.
Open up terminal and open postgres. Perform a query on the shuttle missions table. Taping 'q' will quit the view.
```
sudo -u postgres psql openspaceapi
SELECT * FROM "ShuttleMission";
```
