text = "Hello, World!"
# Using the upper() method to convert the string to uppercase
upper_text = text.upper()
print(upper_text)  # Output: "HELLO, WORLD!"
# Using the lower() method to convert the string to lowercase
lower_text = text.lower()
print(lower_text)  # Output: "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello, world!"
title_text = text.title()
print(title_text)  # Output: "Hello, World!"
# Using the replace() method to replace a substring with another substring
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: "Hello, Python!"
# Using the split() method to split the string into a list of words
split_text = text.split()
print(split_text)  # Output: ['Hello,', 'World!']
lstrip_text = "   Hello, World!   ".lstrip()
print(lstrip_text)  # Output: "Hello, World!   "
rstrip_text = "   Hello, World!   ".rstrip()
print(rstrip_text)  # Output: "   Hello, World!"
# Using the strip() method to remove leading and trailing whitespace    
text_with_whitespace = "   Hello, World!   "
strip_text = text_with_whitespace.strip()
print(strip_text)  # Output: "Hello, World!"
# Using the find() method to find the index of a substring
index = text.find("World")
print(index)  # Output: 7
# Using the len() function to get the length of the string
length = len(text)
print(length)  # Output: 13
find_not_found = text.find("Python")
print(find_not_found)  # Output: -1 (substring not found)
find_text = text.find("world")  # Case-sensitive search
print(find_text)  # Output: 4 (index of the first occurrence of "o")
find_text_m = text.find("World")  # Case-sensitive search
print(find_text_m)  # Output: 7 (index of the first occurrence of "W")

text1 = "Python1234"
is_alpha = text1.isalpha()
print(is_alpha)  # Output: False (because of the digits)
is_alnum = text1.isalnum()
print(is_alnum)  # Output: True (because it contains only letters and digits)
is_digit = text1.isdigit()
print(is_digit)  # Output: False (because there are no digits in the string)
is_space = text1.isspace()
print(is_space)  # Output: False (because there are non-space characters in the string)

print(text.startswith("Hello"))  # Output: True (because the string starts with "Hello")
print(text.endswith("!"))  # Output: True (because the string ends with "!")

print(text.count("o"))  # Output: 2 (because there are two occurrences of "o" in the string)
print(text1.count("Python"))  # Output: 1 (because there is one occurrence of "Python" in the string)

print(text.center(20))  # Output: "   Hello, World!    " (the string is centered within a width of 20 characters)
print(text.center(20, "*"))  # Output: "***Hello, World!****" (the string is centered within a width of 20 characters, using "*" as the fill character) 

print(text.ljust(20))  # Output: "Hello, World!       " (the string is left-justified within a width of 20 characters)
print(text.ljust(20, "-"))  # Output: "Hello, World!-------" (the string is left-justified within a width of 20 characters, using "-" as the fill character)
print(text.rjust(20))  # Output: "       Hello, World!" (the string is right-justified within a width of 20 characters)
print(text.rjust(20, "."))  # Output: ".......Hello, World!" (the string is right-justified within a width of 20 characters, using "." as the fill character)

print(text.zfill(20))  # Output: "0000000Hello, World!" (the string is padded with zeros on the left to fill a width of 20 characters) 

print(ord("H"))  # Output: 72 (the Unicode code point of the character "H")
print(chr(72))  # Output: "H" (the character corresponding to the Unicode code point 72)

