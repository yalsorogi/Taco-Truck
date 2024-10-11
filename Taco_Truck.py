# Taco Truck Ordering System

import random

veggies = ["spicy tempeh", "refried beans"]
meats = ["ground beef", "pork carnitas", "spicy chicken","fried chicken","turkey","tuna"]
toppings = ["onions", "pickles", "basil","no toppings"]

items_ordered = []
counted_items = {'spicy tempeh':0,
                 'refried beans':0,
                 'ground beef':0,
                 'pork carnitas':0,
                 'spicy chicken':0,
                 'fried chicken':0,
                 'turkey':0,
                 'tuna':0,
                 'onions':0,
                 'pickles':0,
                 'basil':0,
                 'Corn tortilla':0,
                 'Flour tortilla':0,
                 'guacamole':0,
                 'spicy salsa':0}


print("\nWelcome! To I210 Taco Truck! Let's get your order placed.")
name = input("May I have a name for your order: ")



# choose a tortilla
while True:
    tortilla = input("Would you like a corn or flour tortilla? ")
    items_ordered.append(tortilla + " tortilla")

# vegetarian?
    is_veg = input("\nAre you vegetarian? (Y / N): ")

# choose a protein
    if is_veg == "Y":
        proteins = veggies
    else:
        proteins = meats
#refactor/adjust the code so the "Choose #" is user friendly (start at 1)
    for i in range(len(proteins)):
        print(f"\tChoose {i+1} for", proteins[i])
    
    choice = input("\nWhich protein would you like? ")

    protein = proteins[int(choice) - 1]
    items_ordered.append(protein)

# choose a topping
    print("\n Now choose a topping:")
    for i in range(len(toppings)):
        print(f"\tChoose {i+1} for", toppings[i])


    top_choice = input("\nWhich topping would you like? ")

    topping = toppings[int(top_choice)-1] 
    items_ordered.append(topping)

# guac?
    guac_choice = input("\nWould you like guacamole on that? (Y / N): ")
    if guac_choice == "Y":
        guac = "and guacamole"
        items_ordered.append("guacamole")
    else:
        guac = "hold the guac"
# salsa?
    salsa_choice = input("\nWould you like spicy salsa on that? (Y / N): ")
    if salsa_choice == "Y":
        salsa = "and our spicy salsa"
        items_ordered.append("spicy salsa")
    else:
        salsa = "hold the salsa"



# display taco order
    taco_order = "\nOk, that's one {} taco on a {} tortilla with {} {}, {}."
    print(taco_order.format(protein, tortilla, topping,guac, salsa))

#Ask if the customer is done ordering. if they aren't, loop

    again = input('Would you like anything else? (Y or N):')
    if again == 'N':
        break


#thank you message and a help/survey message
#create random generated #100,000 and 999,999 for each order for a survey code
print("Thank you for your order.")
print("Help the Taco Truck be the best it can be!")
survey_code = random.randint(100000,1000000)
print(f'Text Survey Code {survey_code} to 210-210 to participate')

tip = input("\nWould you like to leave a Tip? (Y / N): ")
if tip == "Y":
    tip_amount = input("How much would you like to tip? ")
    print("Thank you for your generosity!")
else:
    print("Thank you. Have a nice day!")

#dicitonary and store the what is ordered and how many
# Totaling Items Orders
for item in items_ordered:
    if item in counted_items:
        counted_items[item] += 1

#dictionary of only the items that were ordered
order = {item: count for item, count in counted_items.items() if count > 0}

# Print the ordered items dictionary
print("\nItems ordered:")
print(order)

