import json
from webapp.database.dbcomm import db_session
from webapp.database.models import ShuttleMission, ListLandingSite, ListShuttle

def convert_to_minutes(time_str):
    '''
    Function converts the time string ##d ##h ##m
    into minutes
    '''
    mins = 0
    times = time_str.split(' ')
    for time in times:
        if 'd' in time:
            mins = mins + int(time[:2]) * 1440
        elif 'h' in time:
            mins = mins + int(time[:2]) * 60
        elif 'm' in time:
            mins = mins + (int(time[:2]))
    return mins

def read_missions_json():
    '''
    Function reads the JSON file where all the shuttle
    missions data is located.
    '''
    # Open up the JSON File that contains the wiki scraped info
    with open('missions.json') as f:
        missions = json.load(f)
        missions = missions[0]['shuttle_missions']
        return missions

def seed_database(missions):
    '''
    Function take the missions Dictionary and stores
    all the data onto the database.
    '''

    for mission in missions:
        # Check if the shuttle already exists on the Shuttle list table
        # If new, add the shuttle to the datatable first.
        shuttle = ListShuttle.query.filter(ListShuttle.shuttle_name == mission['Shuttle']).first()
        if shuttle == None:
            shuttle = ListShuttle(mission['Shuttle'])
            session.add(shuttle)
            session.commit()

        # Check if the landing site already exists on the Landing Site list table
        # If new, add the site to the datatable first.
        landing_site = ListLandingSite.query.filter(
            ListLandingSite.landing_name == mission['Landing site']).first()
        if landing_site == None:
            landing_site = ListLandingSite(mission['Landing site'])
            session.add(landing_site)
            session.commit()

        # Lastly add the mission to the Shuttle Mission table 
        shuttle_mission = ShuttleMission(
            mission['Order'], mission['Crew'],
            convert_to_minutes(mission['Duration']),
            mission['Launch date'], mission['Mission'],
            mission['Notes'],
            shuttle=shuttle, landing_site=landing_site)

        session.add(shuttle_mission)
        session.commit()

        # mission = ShuttleMission()
        # print("{0} - {1}".format(mission['Order'], mission['Mission']))
    print("Finished seeding database!")

if __name__ == "__main__":
    # execute only if run as a script
    
    # Create a new database session & seed the database
    # with the data from the missions JSON 
    session = db_session()
    missions = read_missions_json()
    seed_database(missions)