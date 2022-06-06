from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime
import os



# Database Configuration Code

connection_string = "mysql://root:@localhost/crash_course"                  # for mysql database connection

# BASE_DIR = os.path.dirname(os.path.realpath(__file__))                    # __file__ vannale yei current file (i.e main.py file) vako directory vanne bujaucha
# connection_string="sqlite:///"+os.path.join(BASE_DIR,'crash_course.db')   # for sqlite database connection

Base = declarative_base() 

engine = create_engine(connection_string, echo=True)                        # echo=True le SQL query haru lai terminal ma display garne kaam garcha

Session = sessionmaker()                                                    # To perform for every database transaction or query, you need to create session, so, sessionmaker() is used to create session 



class User(Base):                                                           # User class vannu ra User model vannu same ho
    __tablename__='users'                                                   # table ko name ==> users
    id= Column(Integer(), primary_key= True)
    username= Column(String(25), nullable= False,unique= True)
    email= Column(String(80), unique= True, nullable= False)
    date_created= Column(DateTime(), default= datetime.utcnow)

    def __repr__(self):                                                     # __repr__() method gives string representation to our User class
        return f"<User username={self.username} email={self.email}>"



