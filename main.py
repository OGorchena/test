class Restaurant:
   def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      self.number_served = 1000
   def describe_restaurant(self):
      print(f"Название ресторана: {self.restaurant_name}")
      print(f"Тип кухни: {self.cuisine_type}")
      
      
   def served_write(self):
      print(f"Количество обслуженных посетителей: {self.number_served}")
   
   def open_restaurant(self):
      print(f"Restaurant {self.restaurant_name} open")

my_restaurant = Restaurant("Vivaldi", "European kitchen")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.served_write()

your_restaurant = Restaurant("Clood Mone", "French kitchen")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
your_restaurant.served_write()

our_restautant = Restaurant("Fishka", "Russian kitchen")
our_restautant.describe_restaurant()
our_restautant.open_restaurant()
our_restautant.served_write()

#dd