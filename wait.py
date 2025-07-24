import time
class Human():
   def __init__(self, race, nation, height, weight, first_name, last_name, age):
      self.race = race
      self.nation = nation
      self.height = height
      self.weight = weight
      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      
   def describe_human_1(self):
      print(f"Раса: {self.race}")
      print(f"Нация: {self.nation}")
      print(f"Рост: {self.height}")
      print(f"Вес {self.weight}")
      
   def describe_human_2(self):
      print(f"Имя: {self.first_name}")
      print(f"Фамилия: {self.last_name}")
      print(f"Возраст: {self.age}")
      
human_1 = Human("Nigga", "Sosal", "189 cm", "85 kg", "Faneli", "Ofesal", "18 лет")
human_1.describe_human_1()
time.sleep(2)
human_1.describe_human_2()
input("Press Enter to continue")
