from main import Post, User, session



# Adding new user
new_user = User(
    username = "ram",
    email = "ram@gmail.com"
)
session.add(new_user)
session.commit()

user = session.query(User).filter(User.id == 1).first()



# posts list contains multiple post
posts = [
    {
        "title":"Learn Python",
        "content":"Basic to Advance Python"
    },
      {
        "title":"Learn Java",
        "content":"Basic to Advance Java"
    },
      {
        "title":"Learn Javascript",
        "content":"Basic to Advance Javascript"
    },
      {
        "title":"Learn HTML",
        "content":"Basic to Advance HTML"
    },
      {
        "title":"Learn CSS",
        "content":"Basic to Advance CSS"
    },

]


for post in posts:
    new_post = Post(
        title = post['title'],
        content = post['content'],
        author = user                       
    )
    session.add(new_post)
    session.commit()


post = session.query(Post).filter(Post.id == 1).first()
print(post.author)                         

print(user.posts)                           