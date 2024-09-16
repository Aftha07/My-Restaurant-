menu = {
  'Pizza': 149,
  'Burger': 99,
  'Noodles': 40,
  'Biriyani': 80,
}

print("=" * 40)
print("\nWELCOME TO OUR RESTAURENT\n")
print("=" * 40)
print("-" * 40)
print("     M    E   N   U")
print("-" * 40)
print("FOOD\t\t\t PRICE")
print("-" * 10,"-" * 15)
print("Pizza  \t\t\t\t149 \nBurger  \t\t\t99 \nNoodles  \t\t\t40 \nBiriyani  \t\t\t80")

order = 0

order_1 = input("\nPlease enter your dish you want to order = ")

if order_1 in menu:
order += menu[order_1]
print(f"{order_1} has been added to your order")
else:
print(f"Sorry your item {order_1} is not available in our restaurent")

next_order = input("Do you want to order anything else (Yes/No) : ")

if next_order == "Yes":
order_2 = input("Please enter your another order = ")
if order_2 in menu:
  order += menu[order_2]
  print(f"{order_2} has been added to your order")

else:
  print(f"{order_2} is  not available in our restaurent")

print(f"The total amount to pay is {order}")
print("-" * 40)
print("\nThank you for visiting our restaurent....Have a good day")
