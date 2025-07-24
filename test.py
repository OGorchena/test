class User:
   def __init__(self, first_name, last_name, age):
      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      
   def describe_user(self):
      print(f"Имя: {self.first_name}")
      print(f"Фамилия: {self.last_name}")
      print(f"Возраст: {self.age} лет")
   
   def greet_user(self):
      print(f"Приветствую тебя на нашей платформе, {self.first_name} {self.last_name}")
      
First_user = User("Дмитрий", "Баринов", "17")
First_user.describe_user()
First_user.greet_user()

Second_user = User("Юлия", "Петрова", "19")
Second_user.describe_user()
Second_user.greet_user()
      
   
   
   