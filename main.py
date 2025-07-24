data_fruts = [ "banana", "cherry", "elderberry"]
data_vegetables = ["carrot", "broccoli", "spinach", "potato"]


if not "apple" in data_fruts:
   for fruit in data_fruts:
      input(f"Выбирете другой фрукт:{data_fruts}")
      if fruit == "banana":
         print("Вы выбрали банан")
      elif fruit == "cherry":
         print("Вы выбрали вишню")
         break
      elif fruit == "elderberry":
         print("Вы выбрали бузину")
         break
else: input("Фрукт уже выбран нажмите, чтобы продолжить")
      

