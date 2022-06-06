from user import Session , engine, User
from sqlalchemy import desc



local_session=Session(bind=engine)


# # order ascending wise
# users_asc = local_session.query(User).order_by(User.username).all()
# for user in users_asc:
#     print(f"User {user.username}")

# order descending wise
users_desc = local_session.query(User).order_by(desc(User.username)).all()
for user in users_desc:
    print(f"User {user.username}")
