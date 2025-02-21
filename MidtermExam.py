#Question 1
a = 10
a = a + 2

print(a*2)

a = 19

print(a+3)

a = a // 2
print(a)



#Question 2

print((3+10**2/2) or 70.0)



#Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)





#Question 4


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome("7489617719749244646336564429479177169847"))
print(palindrome("5485839837501070045005400701057389385845"))
print(palindrome("8025833559061079503003059701609553385208"))
print(palindrome("6593036601359343374664733439531066303956"))

#Question 5
def find_pattern(text):
    """
    Finds all occurrences of words that start with 'C',
    have unlimited letters, and end with 'jeb'.

    :param text: The input text to search in.
    :return: The number of matches found.
    """

    count = 0
    start = 0  # Start searching from the beginning

    while True:
        start = text.find("C", start)  # Find the next occurrence of "C"

        if start == -1:  # No more occurrences of "C"
            break

        end = text.find("jeb", start + 1)  # Look for "jeb" after "C"

        if end != -1:  # Found "jeb"
            if end + 3 <= len(text):  # Ensure "jeb" is a valid end
                count += 1  # Increase count
            start = end + 3  # Move past this match
        else:
            break  # No more occurrences

    return count


# Example Usage
text = "Cxxxxjeb is one match. Another is Ctestjeb but Cnotamatchje and Cwrongje are not."
print(find_pattern(text))






#Question 6
# Lists are mutable
my_list = [1, 2, 3]
print("Original List:", my_list)

# Modifying the list
my_list[0] = 10
print("Modified List:", my_list)

# Original List: [1, 2, 3]
# Modified List: [10, 2, 3]

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Modify the second element
numbers[1] = 20  # This changes the second element from 2 to 20

# Add a new element
numbers.append(6)  # This adds a new element to the end of the list

# Remove an element
numbers.remove(3)  # This removes the number 3 from the list

# After the above operations, the list has been changed:
print(numbers)  # Output: [1, 20, 4, 5, 6]
# Given this, lists has been changes meaning they are mutable

# Strings are immutable
my_string = "hello"

print("Original String:", my_string)

# Attempting to modify the string (will raise an error)
try:
    my_string[0] = 'H'

except TypeError as e:
    print(f"Error: {e}")

# Original String: hello
# Error: 'str' object does not support item assignment

# Define a string
greeting = "Hello, world!"

# Try to change the first character

try:
    greeting[0] = "J"  # This will raise an error, as strings are immutable

except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment

# To change the string, you have to create a new one

greeting = "J" + greeting[1:]

# Now greeting is a new string object:
print(greeting)  # Output: "Jello, world!"




#Question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))  # Generate 10 random numbers

# Iterate over the list using its indices
for i in range(len(random_numbers)):
    num = random_numbers[i]  # Get the number at the current index

    if num > 80:
        # Replace the number with its negative value
        random_numbers[i] = -num
    elif num < 40:
        # Compute the sum of its digits
        digit_sum = sum(int(digit) for digit in str(num))  # Convert to string, sum digits
        random_numbers[i] = digit_sum

# Print the final list after modifications
print("Modified list:", random_numbers)




#Question 8
def is_valid_url(url):
    """
    Checks if the given string is a valid URL without using startswith() or endswith().

    :param url: The string to check
    :return: True if it's a valid URL, False otherwise
    """

    # Step 1: Check if URL starts with "http://" or "https://"
    if len(url) < 8:  # Shortest possible valid URL (http://x.x)
        return False

    # Checking manually for "http://"
    if url[:7] == "http://":
        domain_start = 7  # Position where domain starts
    # Checking manually for "https://"
    elif len(url) >= 8 and url[:8] == "https://":
        domain_start = 8  # Position where domain starts
    else:
        return False  # If neither, it's not a valid web URL

    # Step 2: Ensure there's at least one dot (.) after "//"
    dot_position = -1
    for i in range(domain_start, len(url)):  # Loop through the domain part
        if url[i] == ".":
            dot_position = i
            break  # Stop at the first occurrence of "."

    if dot_position == -1:  # If no dot was found
        return False

    # Step 3: Manually check if URL ends with a valid TLD
    valid_extensions = [".com", ".net", ".org", ".edu", ".gov", ".io"]

    # Extract last 4 characters and compare manually
    last4 = url[-4:]  # Extract last 4 characters
    last3 = url[-3:]  # Extract last 3 characters
    last5 = url[-5:]  # Extract last 5 characters

    for ext in valid_extensions:
        if ext == last4 or ext == last3 or ext == last5:
            return True  # Valid URL if the ending matches

    return False  # If no valid TLD is found


# Testing the function
test_urls = [
    "https://google.com",
    "http://example.net",
    "https://github.io",
    "http://my-site",
    "https://no_extension",
    "https://google.c",
    "www.example.com",
    "https://site.hello"
]

# Running tests
for url in test_urls:
    print(f"{url}: {is_valid_url(url)}")




#Question 9
def days_since_birth(birthday):
    """
    Calculates the number of days that have passed since the given birthday,
    excluding the birth year and the current year.

    :param birthday: The birthday in "DD-MM-YYYY" format (string).
    :return: The number of whole days that have passed.
    """

    # Step 1: Extract the year from the birthday string
    parts = birthday.split("-")  # Split by "-"
    birth_year = int(parts[2])  # Convert birth year to integer

    # Step 2: Define the current year (assuming 2024)
    current_year = 2024  # This would be dynamic in a real-world scenario

    # Step 3: Initialize day counter
    total_days = 0

    # Step 4: Loop through full years between (birth_year + 1) and (current_year - 1)
    for year in range(birth_year + 1, current_year):
        # Normal year has 365 days
        days_in_year = 365

        # Check if it's a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_year += 1  # Leap year has 366 days

        total_days += days_in_year  # Add the year's days to total

    return total_days


# Example Test Cases
print(days_since_birth("22-05-2005"))  # my birthday


