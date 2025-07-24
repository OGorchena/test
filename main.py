class Restaurant:
   def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
   def describe_restaurant(self):
      print(f"Название ресторана: {self.restaurant_name}")
      print(f"Тип кухни: {self.cuisine_type}")
   
   def open_restaurant(self):
      print(f"Restaurant {self.restaurant_name} open")

my_restaurant = Restaurant("Vivaldi", "European kitchen")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("Clood Mone", "French kitchen")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

our_restautant = Restaurant("Fishka", "Russian kitchen")
our_restautant.describe_restaurant()
our_restautant.open_restaurant()

#dd