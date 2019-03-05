from configparser import SafeConfigParser

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from webapp.database.dbcomm import Base

class ShuttleMission(Base):
    __tablename__ = 'ShuttleMission'
    id = Column('Id', Integer, primary_key=True)
    order = Column('Order', Integer, nullable=False)
    number_of_crew = Column('NumberOfCrew', Integer, nullable=False)
    duration_in_minutes = Column('DurationInMinutes', Integer, nullable=False)
    launch_date = Column('LaunchDate', DateTime, nullable=False)
    mission_name = Column('MissionName', String(1024), nullable=False)
    notes = Column('Notes', String(1024))
    
    # One-to-Many relationships
    # A shuttle can be used for multiple missions
    shuttle_id = Column('ListShuttleId',  \
        Integer, ForeignKey('ListShuttle.ShuttleId'),
        nullable=False)
    shuttle = relationship('ListShuttle',
        backref=backref('shuttleMission', lazy=True))
    # A landing site can be used for multiple missions
    landing_site_id = Column('LandingSiteId', \
        Integer, ForeignKey('ListLandingSite.LandingSiteId'),
        nullable=False)
    landing_site = relationship('ListLandingSite',
        backref=backref('shuttleMission', lazy=True))

    def __init__(self, order, number_of_crew, duration_in_minutes,
        launch_date, mission_name, notes, shuttle, landing_site):
        self.order = order
        self.number_of_crew = number_of_crew
        self.duration_in_minutes = duration_in_minutes
        self.launch_date = launch_date
        self.mission_name = mission_name
        self.notes = notes
        self.shuttle = shuttle
        self.landing_site = landing_site

    def as_dict(self):
        '''Returns shuttle data as a dictionary'''
        shuttle = {}
        shuttle['Order'] = self.order
        shuttle['NumberOfCrew'] = self.number_of_crew
        shuttle['DurationInMinutes'] = self.duration_in_minutes
        shuttle['LaunchDate'] = self.launch_date.strftime("%B %d, %Y")
        shuttle['MissionName'] = self.mission_name
        shuttle['Shuttle'] = self.shuttle
        shuttle['LandingSite'] = self.landing_site
        return shuttle

    def as_dict_str(self):
        '''Returns the shuttle object in a dictionary in string format'''
        return "{0}".format(self.as_dict())

    def __str__(self):
        '''Returns a string format for the shuttle'''
        return "{0}".format(self.as_dict())

    def __repr__(self):
        '''Returns string representing Shuttle object'''
        return '<ShuttleMission (%s>' % (self.id)
        
class ListLandingSite(Base):
    __tablename__ = 'ListLandingSite'
    landing_site_id = Column('LandingSiteId', Integer, primary_key=True)
    landing_name = Column('LandingSiteName', String(1024), nullable=False)

    def __init__(self, landing_name=None):
        self.landing_name = landing_name
        
    def __repr__(self):
        return '{0}'.format(self.landing_name)

class ListShuttle(Base):
    __tablename__ = 'ListShuttle'
    shuttle_id = Column('ShuttleId', Integer, primary_key=True)
    shuttle_name = Column('ShuttleName', String(1024), nullable=False)

    def __init__(self, shuttle_name):
        self.shuttle_name = shuttle_name

    def __repr__(self):
        return '{0}'.format(self.shuttle_name)