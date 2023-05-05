#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    address = Column(String(120))
    phone = Column(String(120))
    image_link = Column(String(500))
    facebook_link = Column(String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = Column(String, nullable=False)
    website = Column(String)
    seeking_talent = Column(Boolean, default=False)
    seeking_description = Column(Text,default='')
    num_upcoming_shows = Column(Integer, default=0)
    num_past_shows = Column(Integer, default=0)
    shows = relationship('Show',
                         backref='venue',
                         lazy=True)
    
class Artist(db.Model):
    __tablename__ = 'Artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    phone = Column(String(120))
    genres = Column(String(120))
    image_link = Column(String(500))
    facebook_link = Column(String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website = Column(String)
    seeking_venue = Column(Boolean,default=False)
    seeking_description = Column(Text)
    num_upcoming_shows = Column(Integer, default=0)
    num_past_shows = Column(Integer, default=0)
    shows = relationship('Show',
                         backref='artist',
                         lazy=True)

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    start_time = Column(String(), nullable=False)
    artist_id = Column(Integer,db.ForeignKey('Artist.id') ,nullable=False)
    venue_id = Column(Integer,db.ForeignKey('Venue.id') ,nullable=False)
