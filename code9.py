import re

filename = 'code9.txt' 

try:
    with open(filename, 'r') as file:
        content = file.read()
    
    phone_pattern = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
    phone_numbers = re.findall(phone_pattern, content)

    if phone_numbers:
        for number in phone_numbers:
            print(number)
    else:
        print("No valid phone numbers found.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

