class Restaurant:
   def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
      self.number_served = 0
   def describe_restaurant(self):
      print(f"Название ресторана: {self.restaurant_name}")
      print(f"Тип кухни: {self.cuisine_type}")
      
   def set_number_served(self, number):
      if number >= 0:
        self.number_served = number
        print(f"Обслуженный посетителей за месяц: {number}")
      else:
        print("Количество не может быть отрицательным!")
         
   def served_write(self):
      print(f"Количество обслуженных посетителей За сегодня: {self.number_served}")
   
   def open_restaurant(self):
      print(f"Restaurant {self.restaurant_name} open")

my_restaurant = Restaurant("Vivaldi", "European kitchen")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.served_write()
my_restaurant.set_number_served(100)

your_restaurant = Restaurant("Clood Mone", "French kitchen")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
your_restaurant.served_write()
your_restaurant.set_number_served(200)

our_restautant = Restaurant("Fishka", "Russian kitchen")
our_restautant.describe_restaurant()
our_restautant.open_restaurant()
our_restautant.served_write()
our_restautant.set_number_served(110)
#20:47