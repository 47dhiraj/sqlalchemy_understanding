from user import User, Session, engine



local_session = Session(bind=engine)            # establishing local session for retrieving query or transaction


# # For retrieving all users or objects or instances
users = local_session.query(User).all()
for user in users:
    print(user.username)


# # # For retrieving users with in some range or limit
# users = local_session.query(User).all()[:3]     # limitting to first 3 users only
# for user in users:
#     print(user.username)


# # For fitering the object or instance  (or getting specific user only)
# single_user = local_session.query(User).filter(User.username=="sita").first()
# print(single_user)



