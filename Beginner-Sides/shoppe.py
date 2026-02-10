"""
Shopping cart type program:

1) show a list of items that are available and display their price

2) ask the user what they want, make a variable to store how many of each user wants

3) calculate the total - add sales tax (1.084)

"""
#printing the menu

print("Welcome to the shop, please pick from the following items: ")
print("-----------------------------------------------------------")
print("Potato Chips ...................................... 4.99")
print("Popcorn ........................................... 3.15")
print("Chicken Strips .................................... 5.16")
print("Cotton Candy ...................................... 4.12")
print("Pizza ............................................. 6.34")
print("French Fries ...................................... 1.15")
print("Lemonade .......................................... 2.15")
print("------------------------------------------------------------")
print("\n")

#getting the order ready

print("How many pizzas would you like: ")
pizza = int(input('>'))

print("How many bags of chips would you like: ")
chips = int(input('>'))

print("How many orders of chicken strips would you like: ")
chicken = int(input('>'))

print("How many boxes of fries would you like: ")
fries = int(input('>'))

print("How many bags of cotton candy would you like: ")
candy = int(input('>'))

print("How many bowls of popcorn would you like: ")
popcorn = int(input('>'))

print("How many cups of lemonade would you like: ")
drink = int(input('>'))

#calculating totals

pitotal = pizza * 6.34
chiptot = chips * 4.99
chkn = chicken * 5.16
friez = fries * 1.15
cotton = candy * 4.12
corn = popcorn * 3.15
drank = drink * 2.15

subtotal = pitotal + chiptot + chkn + friez + cotton + corn + drank

fintotal = subtotal * 1.084

print("Reciept ")
print("-----------------------------------------------------------")
print(f"Potato Chips ...................................... {chiptot:.6}")
print(f"Popcorn ........................................... {corn:.6}")
print(f"Chicken Strips .................................... {chkn:.6}")
print(f"Cotton Candy ...................................... {cotton:.6}")
print(f"Pizza ............................................. {pitotal:.6}")
print(f"French Fries ...................................... {friez:.6}")
print(f"Lemonade .......................................... {drank:.6}")
print(f"Subtotal ...................................... {subtotal:.6}")
print("Tax ............................................. 1.084")
print(f"Total............................................. {fintotal:.4}")
print("------------------------------------------------------------")

print("\n")
print("Insert card or select payment type: ")
print("\n")
