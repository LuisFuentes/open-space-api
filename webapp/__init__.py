'''
    Module initializes the Flask web application.
    The following variables are utlizied in the
    websevice module, these are imported and kept
    in memory for the duration of the application's
    lifecycle (or until the Flask app is restarted/stopped)
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from configparser import SafeConfigParser
import logging
import logging.handlers

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Set the log files to be created under current
# Max size of each log file is 100mb, back up 5 files
# handler = logging.handlers.RotatingFileHandler(
#     './logs/webapplogs.log',
#     maxBytes=5*1024*1024, backupCount=5)
# handler.setLevel(logging.INFO)

# formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
# handler.setFormatter(formatter)
#logger.addHandler(handler)

logger.info('Starting web space api')
# The following variables are constants (outside a func) and will
# be used in the webservice module

# Read from the app's config file
logger.info('Loading in the configurations...')
Parser = SafeConfigParser()
Parser.read('webappconfig.ini')

logger.info('Reading in the configurations...')
try:
    # Store in memory the following
    # NumberOfWindows = int(Parser.get("ApplicationSettings", "NumberOfWindows"))
    Test = str(Parser.get("ApplicationSettings", "Test"))
except Exception as e:
    logger.info("Caught an exception while loading config file %s", e)

logger.info('Finished reading all configurations!')

# Setup the flask app & Database
logger.info('Setting up flask app...')
application = Flask(__name__)

from .database import dbcomm
from .database import models

# Setup the database using the DB communcation's session
from .database.dbcomm import db_session

# Close the DB Session's when app exits or session ends
@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from webapp import webservice
