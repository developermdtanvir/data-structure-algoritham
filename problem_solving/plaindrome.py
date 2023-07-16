# TODO: is palindrome 

def is_plaindrome(input_string):
     # Convert the string to lowercase and remove spaces and punctuation
    input_string = input_string.lower()
    input_string = ''.join(char for char in input_string if char.isalnum())

    # Check if the reversed string is equal to the original string
    return input_string == input_string[::-1]

string = str(input("Enter a string:"))

result = is_plaindrome(string)

if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")