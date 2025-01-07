def is_palindrome(string):
    string = string.lower().replace(" ", "")  # Case and space insensitive
    return string == string[::-1]

input_string = input("Enter a string to check for palindrome: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
