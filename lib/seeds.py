


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review


engine = create_engine('sqlite:///db/restaurants.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=4)
restaurant3 = Restaurant(name='Restaurant C', price=5)


session.add_all([restaurant1, restaurant2, restaurant3])
session.commit()


customer1 = Customer(first_name='Peter', last_name='Pan')
customer2 = Customer(first_name='John', last_name='Wick')
customer3 = Customer(first_name='Jackie', last_name='Chan')

session.add_all([customer1, customer2, customer3])
session.commit()


review1 = Review(star_rating=3, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)
review3 = Review(star_rating=5, restaurant=restaurant3, customer=customer3)

session.add_all([review1, review2, review3])
session.commit()


session.close()
