import math
# In this program, we will explore variables
# An equals sign '=' sets the value of a variable

Number_of_Guests = 50
# now the variable "Number_of_Guests" is equal to 50
# we'll keep assigning values to variables now!
Budget = 300
Cost_per_pizza = 20
Slices_per_pizza = 8
Number_of_re    quired_slices = Number_of_Guests * 2
Minimum_number_of_pizzas = math.ceil(Number_of_required_slices / Slices_per_pizza)
Total_cost = Minimum_number_of_pizzas * Cost_per_pizza


print("There will be",Number_of_Guests, "guests at the party!" )
print("We have a budget of:", Budget)
print("Each Pizza costs:", Cost_per_pizza)
print("That means we can afford a maximum of ",
        Budget / Cost_per_pizza,
        "Pizzas")
print("Which means we can have", (Budget / Cost_per_pizza) * Slices_per_pizza,
        "slices of pizza, maximum.")
print("Each person will probably eat 2 slices.")
print("There are going to be", Number_of_Guests, "people in attendance.")
print("Therefore, we will need", Number_of_required_slices, "slices of pizza.")
print("We will need a minimum of", Minimum_number_of_pizzas, "pizzas.")
print("We will have",
        (Minimum_number_of_pizzas * Slices_per_pizza) - Number_of_required_slices,
        "leftover slices")
print("The cost will be", Total_cost)
print("So we have", Budget - Total_cost, "left for ice cream!")
