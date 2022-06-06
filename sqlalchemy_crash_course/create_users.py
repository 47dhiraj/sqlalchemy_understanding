from user import User, Session, engine


users = [                                   
    {
        "username":"ram",
        "email":"ram@gmail.com"
    },
     {
        "username":"shyam",
        "email":"shyam@gmail.com"
    }, 
    {
        "username":"hari",
        "email":"hari@gmail.com"
    }, 
    {
        "username":"sita",
        "email":"sita@gmail.com"
    }, 
    {
        "username":"rita",
        "email":"rita@gmail.com"
    },
]


local_session = Session(bind=engine)                                    


for u in users:                                                         
    new_user = User(username=u["username"],email=u["email"])            
    local_session.add(new_user)                                        
    local_session.commit()                                              

    print(f"Added {u['username']} to the users table in database.")    


# for inserting single record or object to the table in database
# new_user = User(username="dhiraj",email="dhiraj@gmail.com")
# local_session.add(new_user)
# local_session.commit()


