


from models import Restaurant, Customer, Review, Base, engine, session

def get_user_input(prompt):
    return input(prompt).strip()


def test_relationships():
    

    restaurant_name = get_user_input("Enter a restaurant name to retrieve: ")
    customer_first_name = get_user_input("Enter a customer's first name to retrieve: ")


    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    customer = session.query(Customer).filter_by(first_name=customer_first_name).first()


    print(f"\nRestaurant: {restaurant.name}")
    print(f"Customers who reviewed {restaurant.name}: {restaurant.get_customers()}")

    print(f"\nCustomer: {customer.full_name()}")
    print(f"Restaurants reviewed by {customer.full_name()}: {customer.get_restaurants()}")



def test_aggregate_methods():
    

    customer_first_name = get_user_input("Enter a customer's first name to retrieve: ")
    customer = session.query(Customer).filter_by(first_name=customer_first_name).first()


    print(f"\nFull name of {customer.first_name}: {customer.full_name()}")
    print(f"Favorite restaurant of {customer.first_name()}: {customer.favorite_restaurant().name}")

def test_review_full_review():
    

    review = session.query(Review).first()
    print(f"\nFull review details:\n{review.full_review()}")


if __name__ == "__main__":
    try:
        
        
        Base.metadata.create_all(engine)

        
        test_relationships()
        test_aggregate_methods()
        test_review_full_review()

        
        session.commit()

    except Exception as e:

        print(f"Exception occurred: {e}")
        session.rollback()

    finally:
        session.close()
