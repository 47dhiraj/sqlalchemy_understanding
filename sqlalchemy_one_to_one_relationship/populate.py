from main import Parent, Child, session


parent1 = Parent(name = "Parent 1")
parent2 = Parent(name = "Parent 2")

session.add_all([parent1,parent2])
session.commit()

# parents = session.query(Parent).all()
# print(parents)

# parent1 = session.query(Parent).filter(Parent.id==1).first()
# print(parent1)



# One to One Relationship ma, yesari, multiple child, autai parent haru sanga link garayera rakhna painna OR mildaina

child1 = Child(name = "Child 1", parent = parent1)
session.add(child1)
session.commit()

child2 = Child(name = "Child 2", parent = parent1)
session.add(child2)
session.commit()


print(parent1.child)                            # latest link gareko child chai parent sanga bascha, suru ma link vako child ko aba parent sanga kunai relation rahadaina (so, jasari pani one to one relationship nai huncha)

