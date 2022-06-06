from main import session, Customer, Product


# Creating customer objects
customer1 = Customer(name = "Customer 1")
customer2 = Customer(name = "Customer 2")
customer3 = Customer(name = "Customer 3")

# session.add_all(
#     [customer1, customer2, customer3]
# )   
# session.commit()                      


fetched_customer1 = session.query(Customer).filter(Customer.id==1).first()
fetched_customer2 = session.query(Customer).filter(Customer.id==2).first() 



# Creating product objects
product1 = Product(name = "Milk", price = 90)
product2 = Product(name = "Chicken", price = 400)
product3 = Product(name = "Mutton", price = 1300)


# fetched_customer1.products.append(
#     product1                                          
# )

# fetched_customer1.products.append(
#     product2
# )


# fetched_customer2.products.append(
#     product1
# )

# fetched_customer2.products.append(
#     product3
# )


# session.commit()    

fetched_product1 = session.query(Product).filter(Product.id==1).first()

print("Customers buying Product1", fetched_product1.customers)

print("Products of Customer 1", fetched_customer1.products)
print("Products of Customer 2", fetched_customer2.products)
