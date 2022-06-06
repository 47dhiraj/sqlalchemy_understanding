from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    ForeignKey,
    Table
)


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# import os


# For mysql database connection
connection_str = "mysql://root:@localhost/many_to_many"       

# for sqlite database connection
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# connection_str = 'sqlite:///'+os.path.join(BASE_DIR,'blog.db')

engine = create_engine(connection_str)

Base = declarative_base()



assosciation_table = Table(
    'assosciation',                                 
    Base.metadata,
    Column('customer_id', ForeignKey('customers.id')), 
    Column('product_id', ForeignKey('products.id'))    
)



class Customer(Base):
    __tablename__= 'customers'                                            
    id = Column(Integer(), primary_key = True)
    name = Column(String(100), nullable = False)

    products = relationship('Product', secondary= assosciation_table, back_populates= 'customers')
         

    def __repr__(self):                                                
        return f"<Customer {self.name}>"
    

class Product(Base):
    __tablename__= 'products'                                            
    id = Column(Integer(), primary_key = True)
    name = Column(String(100), nullable = False)
    price = Column(Integer(), nullable = False)
    
    customers = relationship('Customer', secondary = assosciation_table, back_populates = 'products')


    def __repr__(self):                                                
        return f"<Product {self.name}>"



Base.metadata.create_all(engine)                                        
session = sessionmaker()(bind=engine)


