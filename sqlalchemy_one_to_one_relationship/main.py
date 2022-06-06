from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    ForeignKey
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker




# For mysql database connection
conn = "mysql://root:@localhost/one_to_one"       


# For sqlite database connection
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# conn = 'sqlite:///'+os.path.join(BASE_DIR,'one_to_one.db')


engine = create_engine(conn, echo=True)                    

Base = declarative_base()


class Parent(Base):
    __tablename__= 'parents'                                   
    id = Column(Integer(), primary_key = True)
    name = Column(String(25), nullable = False)
    child = relationship('Child', back_populates = 'parent', uselist = False, cascade = "all, delete")      # uselist = False, it only returns one child object or instance (i.t it indicates one to one relationship) # cascade = "all, delete" vannale Parent object lai nai delete garda, tes parent object sanga related child object automatically delete huncha vaneko

    def __repr__(self):                                       
        return f"<Parent {self.id}>"


class Child(Base):
    __tablename__= 'children'                                
    id = Column(Integer(), primary_key = True)
    name = Column(String(25), nullable = False)
    parent_id = Column(Integer(), ForeignKey('parents.id', ondelete = "CASCADE"))     
    parent = relationship('Parent', back_populates = 'child')

    def __repr__(self):
        return f"<Child {self.id}>"



Base.metadata.create_all(engine)               

session = sessionmaker()(bind=engine)         



