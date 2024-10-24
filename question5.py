# Get the user's age
age = int(input("Enter your age: "))

# Determine the age category
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")
