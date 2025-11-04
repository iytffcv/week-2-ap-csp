# open up the vscode from previous day
# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Marvin"
age = 30
favorite_color = "Blue"
favorite_number = 7

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper())

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print(f"My (first_name) and my favorite color is {favorite_color}")

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
print(f"My favorite number times 2 is {favorite_number * 2}.")
print(f"My favorite number plus 10 is {favorite_number + 10}.")
print(f"My favorite number squared is {favorite_number ** 2}.")


#  Step 4: User Input Practice
# Ask the user two questions and combine answers
ser_food = input("What is your favorite food? ")
user_place = input("Where do you want to travel? ")
print(f"You love {user_food} and want to visit {user_place}!")




# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together

print(f"{first_name.upper()} loves {favorite_color}, enjoys eating {ser_food}, ")
print f"and dreams of visiting {user_place}. "
print( f"If you double their favorite number ({favorite_number}), you get {favorite_number * 2}!")