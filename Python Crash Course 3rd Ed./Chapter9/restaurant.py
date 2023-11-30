class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nName: {self.restaurant_name.title()}")
        print(f"Cuisine: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is now open!")

    def read_served(self):
        print(f"\nCustormers Served: {self.number_served}")

    def set_number_served(self, new_served):
        self.number_served = new_served

    def increment_number_served(self):
        self.number_served += 1


# 9-4 Number Served
restaurant = Restaurant('yellow cab', 'fast food')

restaurant.read_served()
restaurant.set_number_served(5)
restaurant.read_served()
restaurant.increment_number_served()
restaurant.read_served()

# Creating an instance of our Restaurant class
# restaurant = Restaurant('yellow cab', 'fast food')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# Creating 3 instances of restaurants
# restaurant_one = Restaurant('mang inasal', 'fast food')
# restaurant_two = Restaurant('golden mami house', 'chinese food')
# restaurant_three = Restaurant('wingyard', 'unli wings')

# restaurant_one.describe_restaurant()
# restaurant_two.describe_restaurant()
# restaurant_three.describe_restaurant()
