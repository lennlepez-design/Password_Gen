import random
import string
import Module

# user loop
print("Password Generator")
print("Type 'exit' to quit.\n")

while True:
    user_category = input("Enter a category/word: ").strip()
    if user_category.lower() == 'exit':
        break
    if not user_category:
        continue

    user_len_input = input("Enter password length you want: ").strip()
    if user_len_input.lower() == 'exit':
        break
        
    try:
        exact_length = int(user_len_input)
        if exact_length <= 0:
            print("Length must be greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid whole number for length.")
        continue

    # Generate the password
    result = generate_password(user_category, target_len=exact_length)
    
    print(f"\nPassword: {result}")
    print(f"Length:   {len(result)} characters long.")
    print("-" * 40 + "\n")