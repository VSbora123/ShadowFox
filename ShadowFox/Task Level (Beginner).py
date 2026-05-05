# 1. Variables:~
# Q1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.

pi = 22/7
print(type(pi))

# Q2. Create a variable called for and assign it a value 4. See what happensand find out the reason behind the behavior that you see.

# for = 4

# Q3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. 
# Formula: Simple Interest = P X R X T/100

principal = 100    # example amount
rate = 5           # example interest
time = 3           # time in 3 years
SI = (principal * rate * time)/100
print(f"The Simple Interest is: {SI}")

# ---------------------------------------------------------------------------------------------------------------------------------


# 2. Numbers:~
# Q1. Write a function that takes two arguments, 145 and 'o', and uses the 'format' function to return a formatted string.
# Print the result. Try to identify the representation used.

def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print(f"Formatted string: {result}")


# Q2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = pi * r**2.
# (Use the value 3.14 for pi). Bonus question: If there is exactly 1.4 litres of water in a square meter, what is the total amount of water in the pond?
# Print the answer without any decimal point in it. Hint: Circle Area = pi*r**2, Water in the pond = Pond Area Water per square meter.

radius = 84
pi = 3.14
water_per_sq_meter = 1.4

# Area of the circular pond
Pond_Area = pi * (radius ** 2)
print(f"Area of the circular pond is: {Pond_Area}")

# Total Water
total_water = Pond_Area * water_per_sq_meter
print(f"Total amount of water: {int(total_water)}")


# Q3. If you cross a 490 meter long street in 7 mins, calculate your speed in meters per second. Print the answer without any decimal point in it.
# Hint: Speed = Distance/Time

distance = 490
time_min = 7
time_sec = time_min * 60
speed =  distance/time_sec

print(f"Speed in meter per seconds: {int(speed)}")

# -------------------------------------------------------------------------------------------------------------------------------


# 4. If Condition:~
# Q1. Write a program to determine the BMI Category based on the user input. Ask the user to:
#     Enter height in meters 
#     Enter weight weight in kilograms
#     Calculate BMI using the formula: BMI = weight/(height)**2
#     Use the following categories:
#        If BMI is 30 or greater, print "Obesity"
#        If BMI is between 25 and 29, print "Overweight"
#        If BMI is between 18.5 and 25, print "Normal"
#        If BMI is less than 18.5, print "Underweight"

#     Example:
#     Enter height in meters: 1.75
#     Enter weight in kilograms: 70
#     Output: "Normal"

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight/(height)**2

if bmi >= 30:
    print("Obesity")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
else:
    print("Underweight")

# Q2. Write a program to determine which country a city belongs to. Given list of cities per country:
# Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
# UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# Ask the user to enter a city name and print the corresponding country.
# Example:
#   Enter a city name: "Abu Dhabi"
#   Output: "Abu Dhabi is in UAE"

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city: ")

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"Sorry, I don't know which country {city} belongs to.")

# Q3. Write a program to check if two cities belong to the same country.
# Ask the user to enter two cities and print whether they belong to the same country or not.

# Example:
# Enter the first city: "Mumbai"
# Enter the second city: "Chennai"
# Output: "Both cities are in India"

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

# Determine country for city1
if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
elif city1 in India:
    country1 = "India"
else:
    country1 = None

# Determine country for city2
if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
elif city2 in India:
    country2 = "India"
else:
    country2 = None

if country1 == country2 and country1 is not None:
    print(f"Both cities are in {country1}.")
else:
    print("They don't belong to the same country.")

# ---------------------------------------------------------------------------------------------------------------------------------

# 5. For Loop:~
# Q1. Using a loop, simulate rolling a sixsided die multiple times(at least 20 times)
#   Count and print the following statistics:
#   How many times you rolled a 6.
#   How many times you rolled a 1.
#   How many times you rollod two 6s in a row.

import random
rolls = 20
count_6 = 0
count_1 = 0
two_6s_in_row = 0
last_roll = 0

print("Rolling the die 20 times.....")

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i + 1}: {roll}")

    # Check for a 6
    if roll == 6:
        count_6 += 1

        if last_roll == 6:
            two_6s_in_row += 1

    # Check for 1
    if roll == 1:
        count_1 += 1

    last_roll = roll

print(f"Times rolled a 6: {count_6}")
print(f"Times rolled a 1: {count_1}")
print(f"Times rolled two 6s in a row: {two_6s_in_row}")


# Q2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
# Write a program that: Asks you to perform 10 jumping jacks at a time. After each set, it asks, "Are you tired?"
# If you reply "yes" or "y", it should ask if you want to skip the remaining sets.
# If you reply "yes" or "y", it should break and print, "You completed a total of jumping jacks."

total_goal = 100
completed = 0

for i in range(10, total_goal + 1, 10):
    print(f"Perform 10 jumping jacks. (Total: {i})")
    completed = i

    if completed == total_goal:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired?").strip().lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets?").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break

    else:
        remaining = total_goal - completed
        print(f"{remaining} jumping jacks are remaining.")

# --------------------------------------------------------------------------------------------------------------------------------------

# 6. Dictionary:~
# Q1. Create a list of you friend's names. The list should have at least 5 names. Create a list of tuples.
# Each tuple should contain a friend's naem and the length of the name.
# For example, if someone's name is Aditya, the tuple would be: ('Aditya', 6)

friends = ["Taehyung", "Namjoon", "Jin", "Jimin", "Yoongi", "Jungkook", "Hoseok"]
friends_length = [(name, len(name)) for name in friends]

print("List of tuples (Name, Length):")
print(friends_length)

# Q2. You and your partner are planning a trip, and you want to track expenses. Create two dictionaries,
# one for your expenses and one for your partner's expenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts.
# For example:
# Your expenses--
# your_expenses = {
#  "Hotel": 1200,
#  "Food": 800,
#  "Transportation": 500,
#  "Attractions": 300,
#  "Miscellaneous": 200
# }

## Your partner's expenses--
# partner_expenses = {
#  "Hotel": 1000,
#  "Food": 900,
#  "Transportation": 600,
#  "Attractions": 400,
#  "Miscellaneous": 150
# }
# Calculate the total expenses for each of you and print the results.
# Determine who spent more money overall and print the result.
# Find out the expense category where there is a significant difference in spending between you and your partner. Print the category and the difference.

your_expenses = {
 "Hotel": 1200,
 "Food": 800,
 "Transportation": 500,
 "Attractions": 300,
 "Miscellaneous": 200
}

partner_expenses = {
 "Hotel": 1000,
 "Food": 900,
 "Transportation": 600,
 "Attractions": 400,
 "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: {your_total}")
print(f"Partner's total expenses: {partner_total}")

# Determines who spent more money
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent money overall.")
else:
    print("Both of you spent the same amount.")

# Find out the expense category and significate difference
max_diff = 0
significant_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        significant_category = category

print(f"Significant difference in spending: {significant_category} (Difference: {max_diff})")

# --------------------------------------------------------------------------------------------------------------------------------------