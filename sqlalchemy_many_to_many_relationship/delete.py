from main import session, Customer, Product


customer1 = session.query(Customer).filter(Customer.id==1).first()

product1 = session.query(Product).filter(Product.id==1).first()
product2 = session.query(Product).filter(Product.id==2).first()


customer1.products.remove(product2)
session.commit()


