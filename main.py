
  

print()
print("** Welcome to the Unit Converter **")
print()

while True:
 conversions_available = [(1, "km", "mi"),
                         (2, "mi", "km"),
                         (3, "kg", "lbs"),
                         (4, "lbs", "kg"),
                         (5, "C", "F"),
                         (6, "F", "C")]
    

 print("conversions_available:")
 print()

 for conversions_number, from_unit, to_unit in conversions_available:
  print(f"{conversions_number}: {from_unit} ({to_unit})")


 print()
 conversions = input(f"Enter the number of the conversion you would like to perform: ")
 conversions_index = int(conversions) - 1
 conversions_number, from_unit, to_unit =conversions_available[conversions_index]
 print()
  
 from_value = float(input(f"Enter the value in {from_unit}: "))
 print()

 if conversions_number == 1:
  to_value = from_value *0.62
  print(f"{from_value} {from_unit} is equal to {to_value} {to_unit}")

 elif conversions_number == 2:
  to_value = from_value * 1.61
  print(f"{from_value} {from_unit} is equal to {to_value} {to_unit}")

 elif conversions_number == 3:
  to_value = from_value * 0.45
  print(f"{from_value} {from_unit} is equal to {to_value} {to_unit}")

 elif conversions_number == 4:
  to_value = from_value *2.22
  print(f"{from_value} {from_unit} is equal to {to_value} {to_unit}")

 elif conversions_number == 5:
  to_value = (from_value - 32) / 1.8
  print(f"{from_value} {from_unit} is equal to {to_value} {to_unit}")

 elif conversions_number == 6:
  to_value = from_value * 1.8 + 32
  print(f"{from_value} {from_value} is equal to {to_value} {to_unit}")

 print("Would you like to enter another unit")

 print("1. Yes")
 print("2. No")
 choice = int(input("Enter your choice: "))
 if choice == 1:
    continue
   #to go back to the start of the loop
 elif choice == 2:
   print("Thank you for using the unit converter")
   break
    

  
