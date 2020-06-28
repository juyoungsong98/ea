import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))    # create a 'scoped session' that ensures different users' interactions with the
                                                    # database are kept separate


# same import and setup statements as above

f = open("resources.csv")
reader = csv.reader(f)
for title,type,length,image,link in reader: # loop gives each column a name
    db.execute("INSERT INTO resources (title,type,length,image,link) VALUES (:title, :type, :length,:image, :link)",
                  {"title": title, "type": type, "length": length,"image":image, "link":link}) # substitute values from CSV line into SQL command, as per this dict
db.commit() # transactions are assumed, so close the transaction finished