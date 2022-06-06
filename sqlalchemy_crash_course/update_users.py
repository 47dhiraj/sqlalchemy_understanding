from user import Session, engine, User


local_session=Session(bind=engine)                      # establishing local session for updating query or transaction


# For updating/editing the object or instance
user_to_update = local_session.query(User).filter(User.username == 'ram').first()
user_to_update.username = "ramesh"
user_to_update.email = "ramesh@gmail.com"
local_session.commit()                                  # pahilai database ma vakoinstance vayera add nagari direct commit gareko
