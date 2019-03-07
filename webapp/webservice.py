from webapp import application, logger
from webapp.database.models import ShuttleMission, ListLandingSite, ListShuttle
import json
import datetime

@application.route('/')
@application.route('/index')
def index():
    ''' Default page '''
    # TODO: Add a Fancy landing page
    logger.debug("Hit the default page!")
    return ("Hello, World! This is a confirmation page to show the app is up")

@application.route('/api/shuttle/mission/<mission_name>')
def get_shuttle_by_mission_name(mission_name):
    '''
    Fetch a single shuttle's info by name.
    Returns a single shuttle's info by the mission name it was on
    '''
    
    shuttle = ShuttleMission.query.filter(ShuttleMission.mission_name == mission_name).first()
    return shuttle.as_dict_str()

@application.route('/api/shuttle/launchyear/<int:launch_year>')
def get_shuttles_by_year(launch_year):
    '''
    Fetch all shuttles's info with the same launch year given.
    Returns a list of shuttle's info in JSON string format.
    '''
    launch_year_min = datetime.datetime(launch_year, 1, 1)
    launch_year_max = datetime.datetime(launch_year + 1, 1, 1)

    shuttles = ShuttleMission.query.filter(
        (ShuttleMission.launch_date >= launch_year_min)
        & (ShuttleMission.launch_date <= launch_year_max)).all()

    shuttlesList = []
    for shuttle in shuttles:
        shuttlesList.append(shuttle.as_dict_str())

    return "{0}".format(shuttlesList)