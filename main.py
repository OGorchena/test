data_fruits = ["banana", "cherry", "elderberry"]
data_vegetables = ["carrot", "broccoli", "spinach", "potato"]

def choose_1():
   index = int(input(f"Выберите один фрукт (используя цифры): {', '.join([f'{i}: {fruit}' for i, fruit in enumerate(data_fruits)])}: "))
   if 0 <= index < len(data_fruits):
       print(f"Вы выбрали: {data_fruits[index]}")
   else:
       print("Неверный индекс. Пожалуйста, попробуйте снова.")
def choose_2():
   index = int(input(f"Выберите один овощь (используя цифры): {', '.join([f'{i}: {fruit}' for i, fruit in enumerate(data_vegetables)])}: "))
   if 0 <= index < len(data_vegetables):
       print(f"Вы выбрали: {data_vegetables[index]}")
       print(f"Спасибо за покупки! \n Ваша корзина: {data_fruits[index]}, {data_vegetables[index]}")
   else:
       print("Неверный индекс. Пожалуйста, попробуйте снова.")
   


choose_1()
choose_2()
