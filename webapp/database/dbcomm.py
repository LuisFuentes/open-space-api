from configparser import SafeConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from webapp import Parser
import os



if 'DATABASE_URL' in os.environ:
    # Heroku Production DB URL
    connection_str = os.environ['DATABASE_URL']
else:
    # Otherwise, use the dev DB URL
    # Fetch the config settings for the DB
    database_user = str(Parser.get("DatabaseSettings", "User"))
    database_pw = str(Parser.get("DatabaseSettings", "Password"))
    database_name = str(Parser.get("DatabaseSettings", "DatabaseName"))
    database_server = str(Parser.get("DatabaseSettings", "ServerName"))

    # Send the connection string
    # FORMAT: //user:password@host/dbname[?key=value..]
    connection_str = "postgresql://{0}:{1}@{2}/{3}".format(database_user, database_pw, database_server, database_name) 



engine = create_engine(connection_str, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import webapp.database.models
    Base.metadata.create_all(bind=engine)