# Marksheet 7 Subjects
print("Marksheet: 7 Subjects")
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))
sub5 = int(input("Enter marks for Subject 5: "))
sub6 = int(input("Enter marks for Subject 6: "))
sub7 = int(input("Enter marks for Subject 7: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7
percentage = (total_marks / 700) * 100

print("\n--- Result ---")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")

# if/else ladder
if percentage >= 80:
    grade = 'A'
    print("Result: Pass")
elif percentage >= 70:
    grade = 'B'
    print("Result: Pass")
elif percentage >= 60:
    grade = 'C'
    print("Result: Pass")
elif percentage >= 50:
    grade = 'D'
    print("Result: Pass")
elif percentage >= 40:
    grade = 'E'
    print("Result: Pass")
else:
    grade = 'F'
    print("Result: Fail")

print(f"Grade: {grade}")



# Leap Year
year = int(input("Enter a year: "))

# Nested if/else
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")



# Smaller / Largest Number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# if/else
if num1 > num2:
    print(f"{num1} is the largest number.")
    print(f"{num2} is the smallest number.")
else:
    print(f"{num2} is the largest number.")
    print(f"{num1} is the smallest number.")



# Positive / Negative
num = int(input("Enter a number: "))

# if/elif/else
if num > 0:
    print(f"The number {num} is Positive.")
elif num < 0:
    print(f"The number {num} is Negative.")
else:
    print(f"The number is Zero.")



# Signup / Login
registered_username = ""
registered_password = ""

while True:
    print("\n--- Main Menu ---")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

# if/elif/else
    if choice == '1':
        print("\n--- Signup ---")
        registered_username = input("Enter a new username: ")
        registered_password = input("Create a new password: ")
        print("Signup successful! You can now log in.")
        
    elif choice == '2':
        print("\n--- Login ---")
        if registered_username and registered_password:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            if username == registered_username and password == registered_password:
                print("Login successful! Welcome.")
            else:
                print("Login failed. Invalid username or password.")
        else:
            print("No account found. Please sign up first.")

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")