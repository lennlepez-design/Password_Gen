import random
import string

def generate_password(category, target_len=14):
    # Clean the input category
    base_word = category.lower().replace(" ", "")
    
    # Scrambled substitution pool (15 random options completely unrelated to the original letter)
    # This ensures the final password looks nothing like the input category
    substitution_pool = {
        'a': ['x', '7', '!', 'M', '9', '$', 'q', 'L', '2', '#', 'v', 'R', '_', '5', 'k'],
        'b': ['p', '4', '&', 'Z', '0', '%', 'w', 'H', '1', '*', 'm', 'Q', '-', '8', 'v'],
        'c': ['9', 'r', '#', 'K', '2', '@', 'x', 'P', '7', '$', 'b', 'W', '+', '6', 'j'],
        'd': ['m', '3', '$', 'L', '8', '^', 'q', 'V', '0', '!', 'n', 'Z', '=', '4', 'r'],
        'e': ['w', '8', '!', 'P', '5', '&', 'z', 'M', '3', '*', 'c', 'Y', '_', '9', 'x'],
        'f': ['k', '2', '@', 'H', '7', '%', 'v', 'B', '6', '#', 'p', 'X', '-', '1', 'm'],
        'g': ['q', '6', '$', 'Z', '4', '^', 'r', 'L', '9', '!', 'w', 'N', '+', '3', 'c'],
        'h': ['b', '9', '&', 'V', '1', '*', 'm', 'Q', '8', '@', 'x', 'F', '=', '7', 'p'],
        'i': ['z', '5', '#', 'M', '3', '%', 'p', 'T', '4', '$', 'r', 'D', '_', '0', 'w'],
        'j': ['n', '1', '!', 'K', '6', '&', 'w', 'R', '7', '*', 'c', 'G', '-', '2', 'v'],
        'k': ['x', '7', '@', 'B', '9', '^', 'm', 'P', '2', '#', 'q', 'S', '+', '8', 'l'],
        'l': ['v', '4', '$', 'H', '0', '%', 'r', 'W', '5', '!', 'z', 'A', '=', '3', 'k'],
        'm': ['p', '8', '&', 'L', '3', '*', 'c', 'Y', '1', '@', 'n', 'V', '_', '6', 'q'],
        'n': ['m', '3', '#', 'Z', '7', '^', 'x', 'F', '9', '$', 'w', 'B', '-', '5', 'r'],
        'o': ['q', '9', '!', 'Q', '2', '&', 'p', 'M', '6', '*', 'b', 'X', '+', '1', 'z'],
        'p': ['w', '6', '@', 'V', '8', '%', 'n', 'T', '4', '#', 'r', 'J', '=', '7', 'c'],
        'q': ['k', '2', '$', 'K', '1', '^', 'z', 'R', '0', '!', 'm', 'L', '_', '9', 'p'],
        'r': ['b', '5', '&', 'P', '4', '*', 'w', 'G', '8', '@', 'x', 'S', '-', '3', 'n'],
        's': ['z', '0', '#', 'H', '9', '%', 'c', 'D', '3', '$', 'q', 'W', '+', '2', 'm'],
        't': ['n', '7', '!', 'B', '5', '&', 'r', 'V', '1', '*', 'p', 'Z', '=', '6', 'x'],
        'u': ['x', '4', '@', 'M', '6', '^', 'm', 'Y', '7', '#', 'w', 'A', '_', '8', 'v'],
        'v': ['p', '1', '$', 'L', '3', '%', 'q', 'F', '0', '!', 'z', 'Q', '-', '4', 'r'],
        'w': ['m', '8', '&', 'Z', '2', '*', 'b', 'X', '9', '@', 'n', 'H', '+', '5', 'c'],
        'x': ['q', '3', '#', 'V', '7', '^', 'w', 'T', '5', '$', 'r', 'K', '=', '1', 'p'],
        'y': ['b', '9', '!', 'P', '1', '&', 'x', 'R', '8', '*', 'c', 'M', '_', '7', 'z'],
        'z': ['z', '6', '@', 'K', '4', '%', 'n', 'G', '3', '#', 'm', 'W', '-', '2', 'w']
    }
    
    # Translate the category using the scrambled random options
    transformed_chars = []
    for char in base_word:
        if char in substitution_pool:
            chosen_sub = random.choice(substitution_pool[char])
            transformed_chars.append(chosen_sub)
        else:
            transformed_chars.append(char)
            
    password = "".join(transformed_chars)
    
    # Force the password to be the requested length
    if len(password) >= target_len:
        # If it's longer or equal, cut it off exactly at target_lenght
        return password[:target_len]
    else:
        # If it's shorter, calculate how many characters are missing
        needed_length = target_len - len(password)
        
        # Pool for extra padding characters
        extra_pool = string.ascii_letters + string.digits + "!@#$%^&*-_=+"
        padding = "".join(random.choice(extra_pool) for _ in range(needed_length))
        
        # Combine them to hit the exact length
        password += padding
        return password

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